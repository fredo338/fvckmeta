import instaloader
import json
import os
from datetime import datetime

# Correctly constructing the path for the session file
SESSION_FILE = os.path.join(os.getenv('RUNNER_TEMP', '/tmp'), '.instaloader-runner', 'session-bat.8797744')

# List of Instagram accounts to fetch
ACCOUNTS = [
    "trazim_dom_prodaja",
    "zagrebpride",
    "tunparty",
    "rainbow_ignite",
    "labris_beograd",
    "kolektiv.mana",
    "mornarbeograd",
    "kafesupa",
    "a11inicijativa",
    "kucaumetnica",
    "zene_pustaju",
    "solidarna_kuhinja",
    "ekonomija_darivanja",
    "talas.tirv",
    "wlwartfest",
    "dc.oktobar",
    "kvirkultura"
]

# Initialize Instaloader
L = instaloader.Instaloader()

# Load session from the file
L.load_session_from_file(SESSION_FILE)

# Dictionary to store posts
all_posts = {}

# Fetch latest 3 posts per account
for account in ACCOUNTS:
    try:
        profile = instaloader.Profile.from_username(L.context, account)
        posts_data = []
        count = 0
        for post in profile.get_posts():
            posts_data.append({
                "shortcode": post.shortcode,
                "caption": post.caption,
                "url": f"https://www.instagram.com/p/{post.shortcode}/",
                "date": post.date.strftime("%Y-%m-%d %H:%M:%S")
            })
            count += 1
            if count >= 3:
                break
        all_posts[account] = posts_data
    except Exception as e:
        all_posts[account] = {"error": str(e)}

# Save to posts.json
with open("posts.json", "w", encoding="utf-8") as f:
    json.dump(all_posts, f, ensure_ascii=False, indent=4)

print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Fetched posts for {len(ACCOUNTS)} accounts.")
