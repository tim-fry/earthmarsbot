import ephem
import json
import tweetpony

with open('credentials.json') as f:
    credentials = json.loads(f.read())

def generate_message():
    m = ephem.Mars()
    m.compute()
    milmiles = 92.955807;

    text = "Mars is currently %.6f AU (%.1f million miles) from Earth" % (m.earth_distance, m.earth_distance*milmiles)
    print text
    return text

def send_tweet(message):
    api = tweetpony.API(**credentials)
    user = api.user
    print "Hello, @%s!" % user.screen_name

    try:
        api.update_status(status = message)
    except tweetpony.APIError as err:
        print "Oops, something went wrong! Twitter returned error #%i and said: %s" % (err.code, err.description)
    else:
        print "Yay! Your tweet has been sent!"

def lambda_handler(_event_json, _context):
    # Tweet Message
    send_tweet(generate_message())
