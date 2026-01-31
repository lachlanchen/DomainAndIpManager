const listKey = document.getElementById("listKey");
const listType = document.getElementById("listType");
const maskInput = document.getElementById("mask");
const domainsEditor = document.getElementById("domainsEditor");
const customIpsEditor = document.getElementById("customIpsEditor");
const cidrEditor = document.getElementById("cidrEditor");
const output = document.getElementById("output");
const listCount = document.getElementById("listCount");
const outputCount = document.getElementById("outputCount");
const status = document.getElementById("status");
const themeToggle = document.getElementById("themeToggle");
const includeDomains = document.getElementById("includeDomains");
const includeCustomIps = document.getElementById("includeCustomIps");
const includeCidr = document.getElementById("includeCidr");
const outputMode = document.getElementById("outputMode");
const errorBox = document.getElementById("errorBox");
const errorList = document.getElementById("errorList");
const lastOutputCache = new Map();

let lastFullLines = [];
let lastErrors = [];

async function fetchDomainSet(key) {
  if (lastOutputCache.has(key)) {
    return lastOutputCache.get(key);
  }
  const res = await fetch(`/api/list?key=${key}&type=domains`);
  const data = await res.json();
  const domains = (data.lines || [])
    .map((line) => line.trim())
    .filter((line) => line.length > 0 && !line.startsWith("#"));
  const set = new Set(domains);
  lastOutputCache.set(key, set);
  return set;
}

async function fetchList() {
  status.textContent = "Loading...";
  const key = listKey.value;
  const [domainsRes, customIpsRes, cidrRes, maskRes] = await Promise.all([
    fetch(`/api/list?key=${key}&type=domains`),
    fetch(`/api/list?key=${key}&type=custom_ips`),
    fetch(`/api/list?key=${key}&type=cidr`),
    fetch(`/api/mask?key=${key}`),
  ]);
  const domainsData = await domainsRes.json();
  const customIpsData = await customIpsRes.json();
  const cidrData = await cidrRes.json();
  const maskData = await maskRes.json();
  domainsEditor.value = (domainsData.lines || []).join("\n");
  customIpsEditor.value = (customIpsData.lines || []).join("\n");
  cidrEditor.value = (cidrData.lines || []).join("\n");
  maskInput.value = maskData.mask || "30";
  updateCounts();
  await loadLastOutput();
  status.textContent = "Loaded";
}

function updateCounts() {
  const total =
    linesFrom(domainsEditor.value).length +
    linesFrom(customIpsEditor.value).length +
    linesFrom(cidrEditor.value).length;
  listCount.textContent = `${total} lines`;
  outputCount.textContent = `${linesFrom(output.value).length} lines`;
}

function linesFrom(text) {
  return text
    .split(/\r?\n/)
    .map((line) => line.trim())
    .filter((line) => line.length > 0);
}

async function saveList() {
  status.textContent = "Saving...";
  const key = listKey.value;
  const domains = linesFrom(domainsEditor.value);
  const customIps = linesFrom(customIpsEditor.value);
  const cidr = linesFrom(cidrEditor.value);
  await Promise.all([
    fetch("/api/list", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ key, type: "domains", lines: domains }),
    }),
    fetch("/api/list", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ key, type: "custom_ips", lines: customIps }),
    }),
    fetch("/api/list", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ key, type: "cidr", lines: cidr }),
    }),
  ]);
  await fetch("/api/mask", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ key, mask: maskInput.value.trim() }),
  });
  status.textContent = "Saved";
}

async function runLookup() {
  status.textContent = "Running...";
  output.value = "";
  errorList.innerHTML = "";
  errorBox.hidden = true;
  const key = listKey.value;
  const res = await fetch("/api/run", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      key,
      include_domains: includeDomains.checked,
      include_custom_ips: includeCustomIps.checked,
      include_cidr: includeCidr.checked,
      output_mode: outputMode.value,
    }),
  });
  const data = await res.json();
  lastFullLines = data.full_lines || data.lines || [];
  lastErrors = data.errors || [];
  renderOutput();
  if (lastErrors.length > 0) {
    lastErrors.forEach((domain) => {
      const li = document.createElement("li");
      li.textContent = domain;
      errorList.appendChild(li);
    });
    errorBox.hidden = false;
  }
  updateCounts();
  status.textContent = "Completed";
}

async function loadLastOutput() {
  const key = listKey.value;
  const res = await fetch(`/api/last-output?key=${key}`);
  const data = await res.json();
  lastFullLines = data.lines || [];
  lastErrors = [];
  renderOutput();
}

async function renderOutput() {
  const key = listKey.value;
  const domains = await fetchDomainSet(key);
  if (outputMode.value === "ips_only") {
    output.value = lastFullLines.filter((line) => !domains.has(line)).join("\n");
  } else {
    output.value = lastFullLines.join("\n");
  }
  updateCounts();
}

async function copyOutput() {
  await navigator.clipboard.writeText(output.value);
  status.textContent = "Copied";
}

listKey.addEventListener("change", fetchList);
listType.addEventListener("change", fetchList);
domainsEditor.addEventListener("input", updateCounts);
customIpsEditor.addEventListener("input", updateCounts);
cidrEditor.addEventListener("input", updateCounts);
output.addEventListener("input", updateCounts);
themeToggle.addEventListener("click", () => {
  document.body.classList.toggle("dark");
  const isDark = document.body.classList.contains("dark");
  themeToggle.textContent = isDark ? "Dark" : "Light";
});
outputMode.addEventListener("change", renderOutput);

document.getElementById("loadBtn").addEventListener("click", fetchList);
document.getElementById("saveBtn").addEventListener("click", saveList);
document.getElementById("runBtn").addEventListener("click", runLookup);
document.getElementById("copyBtn").addEventListener("click", copyOutput);

fetchList();
