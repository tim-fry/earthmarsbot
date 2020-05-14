import ephem
import json
import twitter

with open('credentials.json') as f:
    credentials = json.loads(f.read())

def generate_distance_message():
    m = ephem.Mars()
    m.compute()
    lightseconds = 499.005
    milmiles = 92.955807;

    minutes = int(m.earth_distance*lightseconds) / 60
    seconds = m.earth_distance*lightseconds % 60;

    distance = "#Mars is currently %.6f AU (%.1f million miles) from Earth." % (m.earth_distance, m.earth_distance*milmiles)
    time = "It would take %d minutes, %05.2f seconds for a message to travel that distance." % (minutes, seconds)
    return distance + " " + time

def send_tweet(message):
    api = twitter.Api(**credentials)

    try:
        status = api.PostUpdate(message)
    except TwitterError as err:
        print("Oops, something went wrong! Twitter returned an error: %s" % (err.message))
    else:
        print("Yay! Tweeted: %s" % status.text)

def lambda_handler(_event_json, _context):
    # Tweet Message
    send_tweet(generate_distance_message())
