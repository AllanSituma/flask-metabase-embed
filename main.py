from flask import Flask,render_template
import jwt
import time

METABASE_SITE_URL = ""
METABASE_SECRET_KEY = ""

payload = {
  "resource": {"dashboard": 1},
  "params": {
    
  },
  "exp": round(time.time()) + (60 * 10) # 10 minute expiration
}
token = jwt.encode(payload, METABASE_SECRET_KEY, algorithm="HS256")

url = METABASE_SITE_URL + "/embed/dashboard/" + token


app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template("index.html", iframe=url)
