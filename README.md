# earthmarsbot

Find me here: https://twitter.com/earthmarsbot

Twitter bot reporting the distance between Earth and Mars every day at 12:00 GMT.

Just a little side project thrown together based on:

https://annekjohnson.com/blog/2017/06/python-twitter-bot-on-aws-lambda/index.html

because I find it fascinating how much a red dot in the sky moves relative to us.

This project uses (in no particular order):

* [PyEphem](https://rhodesmill.org/pyephem/) for astronimcal calculations
* [TweetPony](tweetpony) for sending tweets
* [Amazon AWS Lambda](https://aws.amazon.com/lambda/) for hosting, scheduling and execution
