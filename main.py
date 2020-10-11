import get_data
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html", link=get_data.get_google_link(get_data.get_articles()[0])[2], name=get_data.get_google_link(get_data.get_articles()[0])[1], date=get_data.get_google_link(get_data.get_articles()[0])[0])

if __name__ == '__main__':
    app.run()
