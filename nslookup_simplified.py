import dns.resolver

custom_ips = [
    # Keep only public IPs; remove private 10.x addresses to avoid VPN conflicts
    "167.172.69.107",
    '104.236.71.191',
    '161.35.185.30',
    '164.90.138.10',
    '158.101.107.181',
    '150.136.74.51',
    '45.55.70.87',
    '167.71.181.51',
]

mask = "32"
cidr = [
    f"23.102.140.112/{mask}",
    f"13.66.11.96/{mask}",
    f"23.98.142.176/{mask}",
    f"40.84.180.224/{mask}"
]

# List of domains to look up (scoped to ChatGPT, Claude, and Google AI only)
domains = [
    # Google AI
    'gemini.google.com',
    'ai.google.dev',
    'aistudio.google.com',
    'notebooklm.google',
    'notebooklm.google.com',

    # Anthropic / Claude
    'claude.ai',
    'api.claude.ai',
    'a-cdn.anthropic.com',
    's-cdn.anthropic.com',
    'statsig.anthropic.com',  # safe to keep, Claude-specific

    # OpenAI / ChatGPT
    'chat.openai.com',
    'ios.chat.openai.com',
    'android.chat.openai.com',
    'auth.openai.com',
    'auth0.openai.com',
    'platform.openai.com',
    'api.openai.com',
    'cdn.openai.com',
    'cdn.oaistatic.com',
    'oaistatic.com',
    'openai-api.arkoselabs.com',
    'openaiapi-site.azureedge.net',
    'files.oaiusercontent.com',
    'chatgpt.livekit.cloud',
    'tcr9i.chat.openai.com',
    'pay.openai.com',
    'chatgpt.com',
    'openai.com',
]

# Function to get all IPs of a domain
def get_ips(domain):
    try:
        # Get 'A' records for IPv4 addresses
        answers = dns.resolver.resolve(domain, 'A')
        return [answer.to_text() for answer in answers]
    except dns.resolver.NoAnswer:
        return ["No A record found"]
    except dns.resolver.NXDOMAIN:
        return ["No such domain"]
    except Exception as e:
        return [f"Error obtaining IPs for domain {domain}: {e}"]

results = []

# Loop through domains and get their IPs
for domain in domains:
    ips = get_ips(domain)
    # print(f"The IP addresses of {domain} are: {ips}")
    # print(domain)
    results.append(domain)
    # print("\n".join(ips))

# Loop through domains and get their IPs
for domain in domains:
    ips = get_ips(domain)
    # print(f"The IP addresses of {domain} are: {ips}")
    # print(domain)
    # print("\n".join([ip+f"/{mask}" for ip in ips]))
    [results.append(ip+f"/{mask}") for ip in ips]

for ip in custom_ips:
    # print(ip + f"/{mask}")
    results.append (ip + f"/{mask}")

for ip in cidr:
    # print(ip)
    results.append(ip)

def f7(seq):
    seen = set()
    seen_add = seen.add
    return [x for x in seq if not (x in seen or seen_add(x) or x.startswith("No"))]


for ip in f7(results):
    print(ip)
