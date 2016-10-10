import json
import os
import unicodecsv

def toCSV(user_tweets):
	name = user_tweets[0][1] + '.csv'
	outputFile = open('csv/' + name, 'wb+')
		# create the csv writer object
	csvwriter = unicodecsv.writer(outputFile)
	# write header
	csvwriter.writerow(["user_id", "user_name", "tweet_id","tweet_text","user_mentions","urls","hashtags"])
	for t in user_tweets:
		csvwriter.writerow(t)
	outputFile.close()
	print(name, 'has', len(user_tweets), 'tweets')

def getData(data):
	for t in data:
		tweet_id = t['id_str']
		tweet_text = t['text']
		urls = (',').join([u['url'] for u in t['entities']['urls']])
		try:
			hashtags = (',').join([h['text'] for h in t['entities']['hashtags']])
		except:
			hashtags = ''
		try:
			user_mentions = (',').join([u['id_str'] for u in t['entities']['user_mentions']])
		except:
			user_mentions = ''
		user_name = t['user']['name']
		user_id = t['user']['id_str']
	
		user_tweets.append([user_id, user_name, tweet_id, tweet_text, user_mentions, urls, hashtags])
	return user_tweets

def main():
	# open file to read
	path = 'rawdata/'
	for filename in os.listdir(path):
		# print(filename)
		# f = open(path + filename, 'r')
		with open(path + filename) as f:
				# d = json.load(json_data)
			for line in f:
				if len(line) > 1:
					data = json.loads(line)
					user_tweets = getData(data)
			toCSV(user_tweets)
			f.close()

user_tweets = []
main()
	# d = json.loads(f.read())
	
		
	
