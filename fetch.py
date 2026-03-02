import instaloader
import os
import json
from datetime import datetime

# Path to the session file (set by GitHub Actions)
SESSION_FILE = os.environ.get("SESSION_PATH", "session-bat.8797744")

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

# Load session from file
L.load_session_from_file(SESSION_FILE)

# Dictionary to store posts
all_posts = {}

# Fetch latest 3 posts from each account
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
            if count >= 3:  # Only latest 3 posts
                break
        all_posts[account] = posts_data
    except Exception as e:
        all_posts[account] = {"error": str(e)}

# Save all posts to posts.json
with open("posts.json", "w", encoding="utf-8") as f:
    json.dump(all_posts, f, ensure_ascii=False, indent=4)

print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Fetched posts for {len(ACCOUNTS)} accounts.")
