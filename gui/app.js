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
const progressBar = document.getElementById("progressBar");

let lastData = null;
let lastOutputLines = [];
let lastErrors = [];

function linesFrom(text) {
  return text
    .split(/\r?\n/)
    .map((line) => line.trim())
    .filter((line) => line.length > 0);
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
  progressBar.classList.add("active");

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
      mask_override: maskInput.value.trim(),
    }),
  });

  const data = await res.json();
  if (data.domains && data.resolved_ips) {
    lastData = {
      domains: data.domains || [],
      resolvedIps: data.resolved_ips || [],
      customIps: data.custom_ips || [],
      cidr: data.cidr || [],
    };
  } else {
    lastData = null;
  }
  lastOutputLines = data.lines || [];
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
  progressBar.classList.remove("active");
}

async function loadLastOutput() {
  const key = listKey.value;
  const res = await fetch(`/api/last-output?key=${key}`);
  const data = await res.json();
  lastOutputLines = data.lines || [];
  lastErrors = [];
  lastData = null;
  renderOutput();
}

function renderOutput() {
  if (!lastData) {
    output.value = lastOutputLines.join("\n");
    updateCounts();
    return;
  }

  const mask = (maskInput.value || "30").trim();
  const lines = [];
  const seen = new Set();

  const addLine = (line) => {
    if (seen.has(line)) return;
    seen.add(line);
    lines.push(line);
  };

  if (includeDomains.checked) {
    if (outputMode.value === "both") {
      lastData.domains.forEach(addLine);
    }
    lastData.resolvedIps.forEach((ip) => addLine(`${ip}/${mask}`));
  }

  if (includeCustomIps.checked) {
    lastData.customIps.forEach((ip) => addLine(`${ip}/${mask}`));
  }

  if (includeCidr.checked) {
    lastData.cidr.forEach(addLine);
  }

  output.value = lines.join("\n");
  updateCounts();
}

async function copyOutput() {
  await navigator.clipboard.writeText(output.value);
  status.textContent = "Copied";
}

listKey.addEventListener("change", fetchList);
listType.addEventListener("change", fetchList);

[domainsEditor, customIpsEditor, cidrEditor].forEach((el) =>
  el.addEventListener("input", updateCounts)
);

output.addEventListener("input", updateCounts);
maskInput.addEventListener("input", renderOutput);
includeDomains.addEventListener("change", renderOutput);
includeCustomIps.addEventListener("change", renderOutput);
includeCidr.addEventListener("change", renderOutput);
outputMode.addEventListener("change", renderOutput);

themeToggle.addEventListener("click", () => {
  document.body.classList.toggle("dark");
  const isDark = document.body.classList.contains("dark");
  themeToggle.textContent = isDark ? "Dark" : "Light";
});

document.getElementById("loadBtn").addEventListener("click", fetchList);
document.getElementById("saveBtn").addEventListener("click", saveList);
document.getElementById("runBtn").addEventListener("click", runLookup);
document.getElementById("copyBtn").addEventListener("click", copyOutput);

fetchList();
