from flask import Flask,render_template
import jwt
import time

METABASE_SITE_URL = "http://digicow-bi.us-east-1.elasticbeanstalk.com"
METABASE_SECRET_KEY = "ec2db55539505aa56e66e5a4dc836d9d25707e46563ecee874a4fb6cce51b232"

payload = {
  "resource": {"dashboard": 1},
  "params": {
    
  },
  "exp": round(time.time()) + (60 * 10) # 10 minute expiration
}
token = jwt.encode(payload, METABASE_SECRET_KEY, algorithm="HS256")

url = METABASE_SITE_URL + "/embed/dashboard/" + token.decode("utf8")


app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template("index.html", iframe=url)
