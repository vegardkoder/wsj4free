import get_data
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html", data=get_data.get_google_links(get_data.get_articles()))

if __name__ == '__main__':
    app.run()
