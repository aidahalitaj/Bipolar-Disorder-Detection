import sys,os
# get old tweets lib
sys.path.append('GetOldTweets-python/')
import got
import tweepy

consumer_key = 'PeyfirPyr57NfUNK1fj5T421C'
consumer_secret = 'ePt3MXl5kVxpGeHqeYNvjOUztm4onuJKooan6iZgsAoa1ORp1m'
access_token = '1527198325-GV8HbhVNfgPes1wfnknZvm1VxJ6mozUg2kZrpSs'
access_token_secret = 'ENTLiTd5bTx3qTyjJtHhyK7J4rADkzR7s60gOid3I5rGE'

count_num = 0

def getUsername(api, userid):
    user = api.get_user(userid) 
    return user.screen_name


def getEachTweet(userID, username, tweet):
    out_format = "{}\t{}\t{}\t{}\n".format(userID, username, str(tweet.date), str(tweet.text.encode('utf-8')))
    return(out_format)
    # Possible entry
    # tweet.id
    # tweet.permalink
    # tweet.username
    # tweet.text
    # tweet.date
    # tweet.retweets
    # tweet.favorites
    # tweet.mentions
    # tweet.hashtags
    # tweet.geo

def getUserIdList():
    # Target_ID <tab> TARGET_ORIGINAL_TWEETS_COUNT  
    with open(YOUR TARGET FILE) as open_file:
        return [(line.split('\t')[0],line.split('\t')[1]) for line in open_file.readlines()]


def main():
    #twitter api setup
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    user_list = getUserIdList()
    for id_num_tuple in user_list[59:]:
        global count_num
        count_num = 0
        userID = id_num_tuple[0]
        try:
            username = getUsername(api,userID)
            print(str(user_list.index(id_num_tuple)+1) + '\t' + username + '\t' + id_num_tuple[1])
        except:
            print('UserID ' + userID + ' is not found on Twitter..')
            continue

        print('Crawling every tweets of ' + username + '..')

        def tweetsToFile(tweets):
            out_folder = 'user_tweets'
            # make sure have output folder
            if not os.path.exists(out_folder):
                os.makedirs(out_folder)
            output_content = ''
            with open(out_folder + '/' + userID,'a') as output_file:
                for tweet in tweets:
                    output_content += getEachTweet(userID, username, tweet)
                output_file.write(output_content)

            global count_num
            count_num += len(tweets)
            print('Total ' + str(count_num) + ' tweets in ' + out_folder + '/' +userID)
            

        tweetCriteria = got.manager.TweetCriteria().setUsername(username).setUntil(YOUR ENDING DATE)
        got.manager.TweetManager.getTweets(tweetCriteria, tweetsToFile, 100)
        print('\n\n')

        

if __name__ == '__main__':

    main()
    
