import os

from flask import Flask, render_template, request, flash, redirect, url_for
from datetime import date

app = Flask(__name__)
app.secret_key = os.environ['SECRET_KEY']

united_fixtures = [
    {"opponent": "Hull City", "date": "2026-08-22", "stadium": "MKM Stadium", "competition": "Premier League"},
    {"opponent": "Ipswich Town", "date": "2026-08-29", "stadium": "Old Trafford", "competition": "Premier League"},
    {"opponent": "Everton", "date": "2026-09-05", "stadium": "Hill Dickinson Stadium", "competition": "Premier League"},
    {"opponent": "Manchester City", "date": "2026-09-12", "stadium": "Old Trafford", "competition": "Premier League"},
    {"opponent": "Fulham", "date": "2026-09-19", "stadium": "Craven Cottage", "competition": "Premier League"},
    {"opponent": "Tottenham Hotspur", "date": "2026-10-10", "stadium": "Old Trafford", "competition": "Premier League"},
    {"opponent": "Leeds United", "date": "2026-10-17", "stadium": "Elland Road", "competition": "Premier League"},
    {"opponent": "AFC Bournemouth", "date": "2026-10-24", "stadium": "Old Trafford", "competition": "Premier League"},
    {"opponent": "Chelsea", "date": "2026-10-31", "stadium": "Stamford Bridge", "competition": "Premier League"},
    {"opponent": "Aston Villa", "date": "2026-11-07", "stadium": "Old Trafford", "competition": "Premier League"},
    {"opponent": "Liverpool", "date": "2026-11-21", "stadium": "Anfield", "competition": "Premier League"},
    {"opponent": "Brentford", "date": "2026-11-28", "stadium": "Old Trafford", "competition": "Premier League"},
    {"opponent": "Newcastle United", "date": "2026-12-02", "stadium": "St James' Park", "competition": "Premier League"},
    {"opponent": "Coventry City", "date": "2026-12-05", "stadium": "Old Trafford", "competition": "Premier League"},
    {"opponent": "Crystal Palace", "date": "2026-12-12", "stadium": "Selhurst Park", "competition": "Premier League"},
    {"opponent": "Arsenal", "date": "2026-12-19", "stadium": "Emirates Stadium", "competition": "Premier League"},
    {"opponent": "Nottingham Forest", "date": "2026-12-26", "stadium": "Old Trafford", "competition": "Premier League"},
    {"opponent": "Sunderland", "date": "2026-12-30", "stadium": "Old Trafford", "competition": "Premier League"},
    {"opponent": "Brighton & Hove Albion", "date": "2027-01-02", "stadium": "Amex Stadium", "competition": "Premier League"},
    {"opponent": "Newcastle United", "date": "2027-01-06", "stadium": "Old Trafford", "competition": "Premier League"},
    {"opponent": "Aston Villa", "date": "2027-01-16", "stadium": "Villa Park", "competition": "Premier League"},
    {"opponent": "Liverpool", "date": "2027-01-23", "stadium": "Old Trafford", "competition": "Premier League"},
    {"opponent": "Brentford", "date": "2027-01-30", "stadium": "Gtech Community Stadium", "competition": "Premier League"},
    {"opponent": "Chelsea", "date": "2027-02-06", "stadium": "Old Trafford", "competition": "Premier League"},
    {"opponent": "Brighton & Hove Albion", "date": "2027-02-10", "stadium": "Old Trafford", "competition": "Premier League"},
    {"opponent": "Nottingham Forest", "date": "2027-02-20", "stadium": "City Ground", "competition": "Premier League"},
    {"opponent": "Arsenal", "date": "2027-02-27", "stadium": "Old Trafford", "competition": "Premier League"},
    {"opponent": "Sunderland", "date": "2027-03-03", "stadium": "Stadium of Light", "competition": "Premier League"},
    {"opponent": "Everton", "date": "2027-03-13", "stadium": "Old Trafford", "competition": "Premier League"},
    {"opponent": "Manchester City", "date": "2027-03-20", "stadium": "Etihad Stadium", "competition": "Premier League"},
    {"opponent": "Hull City", "date": "2027-04-10", "stadium": "Old Trafford", "competition": "Premier League"},
    {"opponent": "Ipswich Town", "date": "2027-04-17", "stadium": "Portman Road", "competition": "Premier League"},
    {"opponent": "Crystal Palace", "date": "2027-04-24", "stadium": "Old Trafford", "competition": "Premier League"},
    {"opponent": "Coventry City", "date": "2027-05-01", "stadium": "Coventry Building Society Arena", "competition": "Premier League"},
    {"opponent": "AFC Bournemouth", "date": "2027-05-08", "stadium": "Vitality Stadium", "competition": "Premier League"},
    {"opponent": "Leeds United", "date": "2027-05-15", "stadium": "Old Trafford", "competition": "Premier League"},
    {"opponent": "Tottenham Hotspur", "date": "2027-05-23", "stadium": "Tottenham Hotspur Stadium", "competition": "Premier League"},
    {"opponent": "Fulham", "date": "2027-05-30", "stadium": "Old Trafford", "competition": "Premier League"},
]


@app.route("/")
def home():
    today = date.today().isoformat()

    upcoming_fixtures = [
        fixture for fixture in united_fixtures
        if fixture ["date"] >= today
    ]

    next_match = min(upcoming_fixtures, key=lambda fixture: fixture["date"],default=None)
    return render_template('home.html')


@app.route("/fixtures", methods=["GET", "POST"])
def fixtures():
    filtered_fixtures = united_fixtures

    search = ""
    date = ""

    if request.method == "POST":
        search = request.form.get("search", "").strip().lower()
        date = request.form.get("date", "").strip()

    if search:
        filtered_fixtures = [
            fixture for fixture in united_fixtures
            if search in fixture["opponent"].lower()
        ]

    if date:
        filtered_fixtures = [
            fixture for fixture in united_fixtures
            if fixture["date"] == date
        ]

    return render_template('fixtures.html', fixtures=filtered_fixtures)


@app.route("/news")
def news():
    return render_template('news.html', news=news)


@app.route("/contact", methods=["GET", "POST"])
def contact(): 
    errors = []

    if request.method == "POST":
        name = request.form.get("name", "").strip()
        email = request.form.get("email", "").strip()
        message = request.form.get("message", "").strip()

        if not name:
            errors.append("Please enter your name.")
        if not email:
            errors.append("Please enter your email.")
        if not message:
            errors.append("Please enter message.")

        if errors:
            return render_template("contact.html", errors=errors, name=name, email=email, message=message)
        flash('Thank you for submitting your message!')
        return redirect(url_for('home'))
    return render_template('contact.html', errors=errors, name="", email="", message="" )
   




if __name__ == "__main__":
    app.run(debug=True, port=8000)