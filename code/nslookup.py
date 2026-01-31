from pathlib import Path

import dns.resolver

from list_utils import load_lists, load_mask, unique_preserve, write_output

mask = load_mask(Path(__file__).stem, "24")
domains, custom_ips, cidr = load_lists(Path(__file__).stem)
domains = unique_preserve(domains)

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


output_lines = f7(results)
for ip in output_lines:
    print(ip)

write_output(output_lines, Path(__file__).stem)
