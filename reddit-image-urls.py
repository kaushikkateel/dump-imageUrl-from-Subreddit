import praw

#get client information from reddit 
r = praw.Reddit(
		client_id='',
		client_secret= '',
		username= '',
		password= '',
		user_agent=''
	       )

#subreddit name
subR = r.subreddit('aww')

#choose sort type
hot = subR.hot(limit = 200) 
f = open("urls.txt", "a")
for post in hot:
	f.write(post.url)
	f.write("\n")

f.close()
