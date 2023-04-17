import praw
import json

with open("frans_creds.json", "r") as f:
    cred_data = json.load(f)

reddit = praw.Reddit(
    client_id=cred_data["id"],
    client_secret=cred_data["secret"],
    user_agent="FarnsworthBot:v0.7 (by u/FarnsworthBot)",
    username="FarnsworthBot",
    password=cred_data["password"]
)

subreddit = reddit.subreddit("test")
# farns_reply = ("Test reply")

for submission in subreddit.top(limit=500):
    for comm in submission.comments:
        if hasattr(comm,"body"):
            comm_lower = comm.body.lower()
            if "covid" in comm_lower:
                print(submission.title)
                print("************************")
                print(comm.body)
#               comm.reply(farns_reply)