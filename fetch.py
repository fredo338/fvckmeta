import instaloader
import json
from datetime import datetime
import os
import shutil
import time

# Session file in repo root
SESSION_FILE = "session-bat.8797744"

# Instaloader's expected session directory and naming
INSTA_SESSION_DIR = "/tmp/.instaloader-runner"
INSTA_SESSION_NAME = "session-bat.8797744"

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

# Check if session file exists in repo root
if not os.path.exists(SESSION_FILE):
    print(f"Error: Session file '{SESSION_FILE}' not found!")
    exit(1)

# Create instaloader session directory
os.makedirs(INSTA_SESSION_DIR, exist_ok=True)

# Copy session file with the expected naming (session-bat.8797744)
destination = os.path.join(INSTA_SESSION_DIR, f"session-{INSTA_SESSION_NAME}")
shutil.copy(SESSION_FILE, destination)
print(f"Copied session file to {destination}")

# Initialize Instaloader
L = instaloader.Instaloader()

# Load session - pass just the base name without "session-" prefix
L.load_session_from_file(INSTA_SESSION_NAME)

# Dictionary to store posts
all_posts = {}

# Fetch latest 3 posts per account
for account in ACCOUNTS:
    try:
        print(f"Fetching {account}...")
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
        time.sleep(5)  # Wait 5 seconds between accounts
    except Exception as e:
        all_posts[account] = {"error": str(e)}

# Save to posts.json
with open("posts.json", "w", encoding="utf-8") as f:
    json.dump(all_posts, f, ensure_ascii=False, indent=4)

print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Fetched posts for {len(ACCOUNTS)} accounts.")
