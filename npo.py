import json
import os
import unicodecsv
import re

def toCSV(user_tweets, filename):
	name = filename[:-5] + '.csv'
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
	tweets = []
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
	
		tweets.append([user_id, user_name, tweet_id, tweet_text, user_mentions, urls, hashtags])
	return tweets

def main():
	# open file to read
	path = 'rawdata/'
	for filename in os.listdir(path):
		pattern = re.compile(".+.json")
		if pattern.match(filename):
		# print(filename)
		# f = open(path + filename, 'r')
			with open(path + filename) as f:
					# d = json.load(json_data)
				user_tweets = []
				for line in f:
					if len(line) > 4:
						# print(filename)
						data = json.loads(line)
						user_tweets.extend(getData(data))
				toCSV(user_tweets, filename)
				f.close()


main()
