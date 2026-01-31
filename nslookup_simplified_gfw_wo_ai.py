import dns.resolver

custom_ips = [
    # Keep only public IPs; remove private 10.x addresses to avoid VPN conflicts
    # "167.172.69.107",
    # '104.236.71.191',
    # '161.35.185.30',
    # '164.90.138.10',
    # '158.101.107.181',
    # '150.136.74.51',
    # '45.55.70.87',
    # '167.71.181.51',
]

mask = "32"
cidr = [
    # f"23.102.140.112/{mask}",
    # f"13.66.11.96/{mask}",
    # f"23.98.142.176/{mask}",
    # f"40.84.180.224/{mask}"
]

# List of domains to look up (scoped to ChatGPT, Claude, and Google AI only)
domains = [
  "google.com",
  "www.google.com",
  "google.cn",
  "accounts.google.com",
  "mail.google.com",
  "gmail.com",
  "drive.google.com",
  "docs.google.com",
  "sheets.google.com",
  "slides.google.com",
  "maps.google.com",
  "translate.google.com",
  "photos.google.com",
  "play.google.com",
  "fonts.googleapis.com",
  "fonts.gstatic.com",
  "gstatic.com",
  "googleapis.com",
  "youtube.googleapis.com",

  "youtube.com",
  "www.youtube.com",
  "m.youtube.com",
  "youtu.be",
  "youtube-nocookie.com",
  "googlevideo.com",

  "facebook.com",
  "www.facebook.com",
  "m.facebook.com",
  "fb.com",
  "fbcdn.net",
  "fbsbx.com",
  "messenger.com",
  "whatsapp.com",
  "web.whatsapp.com",
  "api.whatsapp.com",
  "meta.com",

  "instagram.com",
  "www.instagram.com",
  "m.instagram.com",
  "api.instagram.com",
  "cdninstagram.com",

  "twitter.com",
  "www.twitter.com",
  "mobile.twitter.com",
  "api.twitter.com",
  "t.co",
  "x.com",

  "blogger.com",
  "blogspot.com",
  "firebaseio.com",
  "firebase.google.com",
  "chromium.org",
  "android.com",

  "itunes.apple.com",
  "apps.apple.com",
  "music.apple.com",
  "developer.apple.com",

  "bing.com",
  "www.bing.com",
  "github.com",
  "raw.githubusercontent.com",
  "githubusercontent.com",
  "onedrive.live.com",
  "outlook.com",

  "telegram.org",
  "t.me",
  "web.telegram.org",
  "signal.org",
  "snapchat.com",
  "reddit.com",
  "discord.com",
  "discord.gg",

  "netflix.com",
  "twitch.tv",
  "soundcloud.com",
  "vimeo.com",
  "dailymotion.com",

  "dropbox.com",
  "box.com",
  "slack.com",
  "trello.com",
  "notion.so",
  "medium.com",

  "cloudfront.net",
  "fastly.net",
  "akamai.net",
  "edgecastcdn.net",

  "doubleclick.net",
  "googlesyndication.com",
  "google-analytics.com"
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
