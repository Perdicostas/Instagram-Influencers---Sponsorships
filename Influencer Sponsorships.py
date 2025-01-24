import instaloader
from datetime import datetime
import re

L = instaloader.Instaloader()

username = "INFLUENCER_USERNAME" #Add Influencer's Username

profile = instaloader.Profile.from_username(L.context, username)

start_date = datetime(2022, 10, 1) #Select Date start
end_date = datetime(2024, 10, 31) #Select Date end

posts = list(profile.get_posts())

filtered_posts = [post for post in posts if start_date <= post.date <= end_date]

def has_mentions(post):
    if post.caption:
        mentions = re.findall(r'@\w+', post.caption)
        return bool(mentions)
    return False

mentioned_posts = [post for post in filtered_posts if has_mentions(post)]

for i, post in enumerate(mentioned_posts, start=1):
    print(f"https://www.instagram.com/p/{post.shortcode}/")
  

