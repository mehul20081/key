
from flask import Flask, jsonify
from datetime import datetime

app = Flask(__name__)

# IPL winners data for the past 5 years (2020-2024 as of current date)
# Adjust years and winners as per actual data
IPL_WINNERS = {
    2024: {"year": 2024, "team": "Kolkata Knight Riders", "captain": "Shreyas Iyer"},
    2023: {"year": 2023, "team": "Chennai Super Kings", "captain": "MS Dhoni"},
    2022: {"year": 2022, "team": "Gujarat Titans", "captain": "Hardik Pandya"},
    2021: {"year": 2021, "team": "Chennai Super Kings", "captain": "MS Dhoni"},
    2020: {"year": 2020, "team": "Mumbai Indians", "captain": "Rohit Sharma"}
}

@app.route('/ipl_winners_past_5_years', methods=['GET'])
def get_ipl_winners():
    current_year = datetime.now().year
    past_5_years_winners = {}

    for year in range(current_year, current_year - 5, -1):
        if year in IPL_WINNERS:
            past_5_years_winners[year] = IPL_WINNERS[year]

    return jsonify(past_5_years_winners)

@app.route('/')
def home():
    return "Welcome to the IPL Winners API! Try /ipl_winners_past_5_years"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True) # debug=True for development, set to False in production