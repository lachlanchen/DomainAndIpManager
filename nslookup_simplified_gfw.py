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
  "www.google.cn",

  "google.com.hk",
  "www.google.com.hk",
  "google.hk",
  "www.google.hk",

  "accounts.google.com",
  "myaccount.google.com",
  "support.google.com",
  "policies.google.com",
  "safety.google",

  "mail.google.com",
  "gmail.com",
  "inbox.google.com",

  "drive.google.com",
  "docs.google.com",
  "sheets.google.com",
  "slides.google.com",
  "forms.google.com",

  "calendar.google.com",
  "meet.google.com",
  "chat.google.com",

  "maps.google.com",
  "news.google.com",
  "translate.google.com",
  "photos.google.com",
  "keep.google.com",
  "sites.google.com",
  "contacts.google.com",
  "books.google.com",
  "scholar.google.com",

  "play.google.com",
  "developers.google.com",
  "developer.android.com",
  "android.com",
  "www.android.com",

  "googleapis.com",
  "www.googleapis.com",
  "storage.googleapis.com",
  "lh3.googleusercontent.com",
  "googleusercontent.com",
  "gstatic.com",
  "fonts.googleapis.com",
  "fonts.gstatic.com",
  "ajax.googleapis.com",
  "clients2.google.com",
  "clients4.google.com",
  "dl.google.com",
  "update.googleapis.com",
  "crl.pki.goog",

  "youtube.com",
  "www.youtube.com",
  "m.youtube.com",
  "youtu.be",
  "youtube-nocookie.com",
  "ytimg.com",
  "i.ytimg.com",
  "googlevideo.com",
  "youtube.googleapis.com",
  "youtubei.googleapis.com",

  "facebook.com",
  "www.facebook.com",
  "m.facebook.com",
  "fb.com",
  "fb.me",
  "messenger.com",
  "m.me",
  "fbcdn.net",
  "fbsbx.com",
  "facebook.net",
  "graph.facebook.com",

  "instagram.com",
  "www.instagram.com",
  "m.instagram.com",
  "api.instagram.com",
  "cdninstagram.com",

  "whatsapp.com",
  "www.whatsapp.com",
  "web.whatsapp.com",
  "api.whatsapp.com",
  "static.whatsapp.net",

  "meta.com",
  "www.meta.com",

  "twitter.com",
  "www.twitter.com",
  "mobile.twitter.com",
  "api.twitter.com",
  "pbs.twimg.com",
  "video.twimg.com",
  "t.co",
  "x.com",
  "www.x.com",

  "telegram.org",
  "t.me",
  "web.telegram.org",
  "api.telegram.org",

  "reddit.com",
  "www.reddit.com",
  "redd.it",
  "old.reddit.com",

  "discord.com",
  "www.discord.com",
  "discord.gg",
  "cdn.discordapp.com",
  "media.discordapp.net",

  "netflix.com",
  "www.netflix.com",
  "nflxvideo.net",
  "nflximg.net",
  "nflxext.com",
  "nflxso.net",

  "twitch.tv",
  "www.twitch.tv",
  "ttvnw.net",

  "soundcloud.com",
  "www.soundcloud.com",

  "vimeo.com",
  "www.vimeo.com",
  "player.vimeo.com",

  "dropbox.com",
  "www.dropbox.com",
  "dropboxusercontent.com",

  "box.com",
  "www.box.com",

  "slack.com",
  "www.slack.com",
  "slack-edge.com",
  "slack-imgs.com",

  "notion.so",
  "www.notion.so",
  "notion.site",

  "medium.com",
  "www.medium.com",

  "github.com",
  "www.github.com",
  "api.github.com",
  "raw.githubusercontent.com",
  "githubusercontent.com",
  "githubassets.com",

  "cloudfront.net",
  "fastly.net",
  "akamai.net",
  "akamaiedge.net",
  "edgecastcdn.net",

  "doubleclick.net",
  "googlesyndication.com",
  "google-analytics.com",
  "googletagmanager.com",
  "googletagservices.com"
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
