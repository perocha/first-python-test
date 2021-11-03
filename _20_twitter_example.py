'''
Example of using Twitter API
'''
from twitter import Twitter, OAuth
import hidden

# Get my credentials that are hidden in file hidden.py that contains a function called oauth
#   def oauth():
#       return {"consumer_key": "<consumer key>",
#           "consumer_secret": "<consumer secret>",
#           "token_key": "<token key>",
#           "token_secret": "<token secret>"}
MY_TWITTER_CREDS = hidden.oauth()

# Authenticate using my secrets
twitter = Twitter(auth=OAuth(MY_TWITTER_CREDS["token_key"],
                MY_TWITTER_CREDS["token_secret"],
                MY_TWITTER_CREDS["consumer_key"],
                MY_TWITTER_CREDS["consumer_secret"]))

# Get your "home" timeline
status_home = twitter.statuses.home_timeline()
# The first 'tweet' in the timeline
print (status_home[0])

# Get a particular friend's timeline
friend = input ("Enter the friend Twitter account: ")
friend_timeline = twitter.statuses.user_timeline(screen_name=friend)
print ("################################")
# Print the first tweet from the friend's timeline
print (friend_timeline[0])

# Update your status
# twitter.statuses.update(status="Trying out changing my status in Twitter using Python")

# Send a direct message
#'''
#twitter.direct_messages.events.new(
#    _json={
#        "event": {
#            "type": "message_create",
#            "message_create": {
#                "target": {
#                    "recipient_id": twitter.users.show(screen_name=friend)["id"]},
#                "message_data": {
#                    "text": "This message was sent with Python!"}}}})
#'''
