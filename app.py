from flask import Flask, render_template, request, flash, redirect, url_for

app = Flask(__name__)

united_fixtures = [
    {
        "opponent": "Chelsea",
        "date": "2nd August, 2026",
        "stadium": "Old Trafford"
    },
       {
        "opponent": "Liverpool",
        "date": "7th August, 2026",
        "stadium": "Anfield"
       },
    {
        "opponent": "Brighton",
        "date": "14th August, 2026",
        "stadium": "Amex Stadium"
    },
    {
        "opponent": "West Ham",
        "date": "21st August, 2026",
        "stadium": "Old Trafford"
    }
]

united_news = [
    {
        "headline": "Manchchester United are all set to start the premier league campaign with three new signings",
        "League": "Premier League"
    },
    {
        "headline": "Manchester United group stage opponents to be revealed next week",
        "League": "Champions League"
    }
]
@app.route("/")
def home():
    return render_template('home.html')


@app.route("/fixtures")
def fixtures():
    return render_template('fixtures.html', fixtures=united_fixtures)


@app.route("/news")
def news():
    return render_template('news.html', news=united_news)


@app.route("/contact", methods=['GET', 'POST'])
def contact():
    if request.method == "POST":
        name = request.form['name']
        email = request.form['email']
        subject = subject.form['subject']
        message = request.form['message']

        flash('Your message has been submitted successfully!')
        return redirect(url_for('home'))
    
    return render_template('contact.html')


@app.route("/hello/<name>")
def hello(name):
    return render_template('hello.html', name=name)



if __name__ == "__main__":
    app.run(debug=True)