import instaloader
import json

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

L = instaloader.Instaloader()

posts_data = []

for username in ACCOUNTS:
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
        if count >= 3:
            break

with open("posts.json", "w") as f:
    json.dump(posts_data, f)

print("Finished.")
