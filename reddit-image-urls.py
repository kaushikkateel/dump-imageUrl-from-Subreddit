import praw
import random
import os
import json

json_f = f = open('credentials.json',)
data = json.load(json_f)

r = praw.Reddit(client_id = data["client_id"],
				client_secret = data["client_secret"],
				username = data["username"],
				password = data["password"],
				user_agent = data["user_agent"])


flag = True

while flag:
	subred = input("Enter the subreddit: ")
	try:
			r.subreddits.search_by_name(subred, exact=True)
			flag = False
	except:
			print("wrong subreddit! enter a correct subreddit")

subR = r.subreddit(subred)

lim = int(input("enter the number of links to be dumped: "))

while not flag:
	sortType = input("enter sort type (hot, new, top): ").lower()
	if sortType == "hot":
		posts = subR.hot(limit = lim)
		flag = not flag
	elif sortType == "new":
		posts = subR.new(limit = lim)
		flag = not flag
	elif sortType == "top":
		while not flag:
			sortBy = input("enter sort by (all, hour, day, week, month, year): ").lower()
			if sortBy in ["all","week","month","year","hour", "day"] :
				posts = subR.top(sortBy, limit = lim)
				flag = not flag
			else:
				print("wrong option! enter correct option")	
	else:
		print("wrong option!, enter correct option")



f = open(subred+".txt", "w")
for post in posts:
	if(("jpg" in post.url) or ("png" in post.url) or ("jpeg" in post.url) or(".gif" in post.url)) :
		f.write(post.url)
		f.write("\n")
print("Job done!")
f.close()
