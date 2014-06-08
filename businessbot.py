#bot created by /u/bassguitarman

import time
print ('Starting Program...')
import praw
print ('The current date and time is ' + time.strftime("%X"))
print (time.strftime("%X") + ': Imported Successfully!')

# Login in to Reddit and the bot
r = praw.Reddit('BusinessHelpBot by /u/debtfreegoal')
#Replace USERNAME and PASSWORD with applicable values
r.login("USERNAME","PASSWORD")
already_done = set()
#sets keywords
words = ['my business', 'My business', 'My Business', 'My Store', 'My store', 'my store', 'accept DogeCoin', 'Accept DogeCoin', 'accept dogecoin', 'Accept Dogecoin', 'accept Dogecoin', 'vendor', 'Vendor', 'promote', 'Promote', 'advertise', 'Advertise', 'youcanaddmorehere', 'orhere', 'thereisgood', 'orevenrighthere']
prawWords = ['donations', 'Donate', 'They', 'They', 'YOUCANADDMORE']

def search_post():
        print 'starting'
        subreddit = r.get_subreddit('dogecoin')
        #Gathers last 15 posts to /r/dogecoin
        subreddit_submissions = subreddit.get_new(limit=15)
        print 'Looking for a post that meets criteria'
        for submission in subreddit_submissions:
                post_title = submission.title.lower()
                #creates text file to store submissions, in order to prevent double commenting
                obj = open('alreadyseen.txt', 'ab+')
                has_word = any(string in post_title for string in words)
                has_banned = any(string in post_title for string in prawWords)
                link = submission.permalink
                sub_id = submission.id
                if sub_id not in open("alreadyseen.txt").read() and not has_banned and has_word:
                        #ensures the post is not spam
                        if submission.ups>0:
                                if sub_id not in already_done:
                                        print 'post found, commenting'
                                        submission.add_comment('<INSERT COMMENT YOU WOULD LIKE BOT TO SAY>')
                                        already_done.add(sub_id)
                                        obj.write(sub_id + '  ') 
                                        obj.close()
                                        time.sleep(15)
                                        break
#loops comment function
while True:
        search_post()
        print (time.strftime("%X") + ': Going to sleep for four minutes' )
        time.sleep(15)
