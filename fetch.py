import instaloader
import json

USERNAME = "bat.8797744"
PASSWORD = "FvkMeta33"

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

MAX_POSTS_PER_ACCOUNT = 3
MAX_TOTAL_POSTS = 60  # keeps file small & safe

L = instaloader.Instaloader(
    download_pictures=False,
    download_videos=False,
    download_comments=False,
    save_metadata=False
)

L.login(USERNAME, PASSWORD)

posts_data = []

for username in ACCOUNTS:
    try:
        profile = instaloader.Profile.from_username(L.context, username)

        count = 0
        for post in profile.get_posts():
            posts_data.append({
                "account": username,
                "caption": post.caption,
                "image_url": post.url,
                "date": str(post.date)
            })

            count += 1
            if count >= MAX_POSTS_PER_ACCOUNT:
                break

    except Exception as e:
        print(f"Error with {username}: {e}")

# Sort newest first
posts_data.sort(key=lambda x: x["date"], reverse=True)

# Limit total posts
posts_data = posts_data[:MAX_TOTAL_POSTS]

with open("posts.json", "w") as f:
    json.dump(posts_data, f)

print("Finished successfully.")
