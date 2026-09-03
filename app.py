import os

from flask import Flask, render_template, request, flash, redirect, url_for

app = Flask(__name__)
app.secret_key = os.environ['SECRET_KEY']

united_fixtures = [
    {
        "opponent": "Chelsea",
        "date": "2nd August, 2026",
        "stadium": "Old Trafford",
        "competition":"Premier League"
    },
       {
        "opponent": "Liverpool",
        "date": "7th August, 2026",
        "stadium": "Anfield",
        "competition":"Premier League"
       },
    {
        "opponent": "Brighton",
        "date": "14th August, 2026",
        "stadium": "Amex Stadium",
        "competition":"Premier League"
    },
    {
        "opponent": "West Ham",
        "date": "21st August, 2026",
        "stadium": "Old Trafford",
        "competition":"Premier League"
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


@app.route("/contact", methods=["GET", "POST"])
def contact(): 
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        email = request.form.get("email", "").strip()
        message = request.form.get("message", "").strip()

        errors = []
        if not name:
            errors.append("Please enter your name.")
        if not email:
            errors.append("Please enter your email.")
        if not message:
            errors.append("Please enter message.")

        if errors:
            return render_template("contact.html", errors=errors, name=name, email=email, message=message)
        flash('Thank you for submitting your message!')
        return redirect("/home")
    return render_template('contact.html', errors=errors, name="", email="", message="" )
   




if __name__ == "__main__":
    app.run(debug=True, port=8000)