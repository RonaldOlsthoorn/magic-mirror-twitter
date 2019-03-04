from flask import Flask, jsonify
from flask_cors import CORS
import json
import twitter

app = Flask(__name__)
CORS(app)

with open('config.json') as f:
    data = json.load(f)

config = data["config"]

api = twitter.Api(consumer_key=config["credentials"]["key"],
                  consumer_secret=config["credentials"]["secret"],
                  application_only_auth=True)


@app.route('/tweets.json')
def tweets():
    if config['specifics']['type'] == 'user_time_line':
        tweets = api.GetUserTimeline(
            screen_name=config["specifics"]["user"],
            count=config["specifics"]["count"])
    elif config['specifics']['type'] == 'query':
        tweets = api.GetSearch(
            term=config["specifics"]['query'],
            count=config["specifics"]["count"])

    texts = {"tweets": [{"id": tweet.id, "text": tweet.text} for tweet in tweets]}
    return jsonify(texts)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
