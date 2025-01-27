# Travel-Risk-API
# Travel Risk API

This project provides an API for calculating travel risk scores based on season and destination (county and state). It utilizes data from the Federal Emergency Management Agency (FEMA) to assess various natural hazard risks and generate a risk score for each season.

**Key Features:**

* Calculates overall risk scores and detailed risk scores for individual hazards (e.g., tornadoes, hurricanes, wildfires).
* Supports querying risk information for specific counties and states.
* Allows for batch requests to get risk scores for multiple destinations.

**Data and Methodology:**

* The API uses a dataset from FEMA that includes hazard risk information for various counties across the United States.
* The code processes the data, calculates risk scores, and provides a user-friendly interface for accessing the information.
* `ALR_NPCTL` in the dataset stands for **Annualized Loss Rate - National Percentile**. It represents the percentile of the annualized loss due to a particular hazard for non-profit critical infrastructure (e.g., hospitals, schools) within a specific county compared to all other counties in the United States.

**Installation**

1. **Create a virtual environment:**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate 
Install dependencies:
Bash
pip install -r requirements.txt 
 Usage

Run the application:
Bash
uvicorn main:app 
 Endpoints:

/weather_risk/{county}/{stateabbrv}/{season}

Retrieves overall risk score and detailed risk scores for individual hazards for a given county, state, and season.
Parameters:
county: County name (string)
stateabbrv: State abbreviation (string)
season: Season (string, options: 'spring', 'summer', 'fall', 'winter')
include_details: Boolean (optional, default: True). If True, returns detailed risk scores for each hazard.
/counties:

Returns a list of all counties available in the dataset.
/states_and_territories:

Returns a list of all states and territories available in the dataset.
/custom_travel_risks:

Accepts a list of destinations (county, state, season) and returns risk information for each destination.
Requires a JSON request body with a list of TravelRequest objects.
Example Usage:

Get risk for a specific location:

Bash
curl [http://127.0.0.1:8000/weather_risk/Los%20Angeles/CA/summer](http://127.0.0.1:8000/weather_risk/Los%20Angeles/CA/summer)
 Get all counties:

Bash
curl [http://127.0.0.1:8000/counties](http://127.0.0.1:8000/counties)
 Get custom travel risks for multiple destinations:

Bash
curl -X POST -H "Content-Type: application/json" -d '{"destinations": [{"county": "Los Angeles", "state": "CA", "season": "summer"}, {"county": "New York", "state": "NY", "season": "winter"}]}' [http://127.0.0.1:8000/custom_travel_risks](http://127.0.0.1:8000/custom_travel_risks)