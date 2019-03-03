from flask import Flask, jsonify
from flask_cors import CORS
import json
import twitter

app = Flask(__name__)
CORS(app)

with open('config.json') as f:
    data = json.load(f)

config = data["config"]

api = twitter.Api(consumer_key=config["key"],
                  consumer_secret=config["secret"],
                  application_only_auth=True)


@app.route('/tweets.json')
def tweets():
    tweets = api.GetSearch(term=config['query'], count=config["count"])
    texts = {"tweets": [{"id": tweet.id, "text": tweet.text} for tweet in tweets]}
    return jsonify(texts)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
