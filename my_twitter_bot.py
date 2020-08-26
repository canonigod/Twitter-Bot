import tweepy
import time

print('this is my twitter bot')

# assign the values accordingly 
CONSUMER_KEY = 'S4R9RYUNukDryRmAlcD2d4ATz'
CONSUMER_SECRET = '8qu55C3E8tvUqphZXhIYEYHYXkIJmrgltUveLX1R4XpjJxguX6'
ACCESS_KEY = '768284674418364416-gtLRgByeGC2WeT20of576RrO2RXZmmC'
ACCESS_SECRET = 'NKKOF7V0z0ocsO2S6ROVz74e2lrj24wLEF4kfOh7T6Qhe'

# authorization of consumer key and consumer secret 
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET) 

# set access to user's access key and access secret  
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET) 

# calling the api  
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True) 

# grabbing file
FILE_NAME = 'last_seen_id.txt'

# grabbing id mentions from file
def retrieve_last_seen_id(file_name):
    f_read = open(file_name, 'r')
    last_seen_id = int(f_read.read().strip())
    f_read.close()
    return last_seen_id

# storing id mentions from file
def store_last_seen_id(last_seen_id ,file_name):
    f_write = open(file_name, 'w')
    f_write.write(str(last_seen_id))
    f_write.close()
    return

def reply_to_tweets() :
    print('Retrieving and replying to tweets...') 
    # DEV NOTE: use 1298069208937435138 for testing
    last_seen_id = retrieve_last_seen_id(FILE_NAME)

    # getting mentions
    mentions = api.mentions_timeline()

    # looping through the mentions
    for mention in reversed(mentions) :
        print(str(mention.id) + ' - ' + mention.text)
        last_seen_id = mention.id
        store_last_seen_id(last_seen_id, FILE_NAME)
        if "#hellopython" in mention.text.lower() :
            print('Found #HelloPython')
            print('Responding Back...')
            api.update_status('@' + mention.user.screen_name + '#HelloPython to you too', mention.id)

while True:
    reply_to_tweets()
    time.sleep(15)