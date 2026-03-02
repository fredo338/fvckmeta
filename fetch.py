import instaloader
import json
from datetime import datetime

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

# Initialize Instaloader and load saved session
L = instaloader.Instaloader()
L.load_session_from_file("session-bat.8797744")

# Dictionary to store posts
all_posts = {}

# Fetch posts
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

# Save to posts.json
with open("posts.json", "w", encoding="utf-8") as f:
    json.dump(all_posts, f, ensure_ascii=False, indent=4)

print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Fetched posts for {len(ACCOUNTS)} accounts.")
