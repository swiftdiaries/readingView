from goose import Goose 
import praw
url = raw_input()
g = Goose()
article = g.extract(url=url)
sum = article.cleaned_text
#keypts = article.keypoints
print sum
