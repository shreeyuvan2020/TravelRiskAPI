from fastapi import FastAPI, HTTPException
from fastapi.security import APIKeyHeader
from pydantic import BaseModel
import pandas as pd
from typing import List
#Reading the dataset, cleaning it, dropping unnecessary columns, and renaming the columns
fema_data = pd.read_csv('NRI_Table_Counties.csv')
fema_data = fema_data.replace([float('inf'), float('-inf')], None)
fema_data = fema_data.fillna(0)
app = FastAPI()
fema_data.columns = ["OID_","NRI_ID","STATE","STATEABBRV","STATEFIPS","COUNTY","COUNTYTYPE","COUNTYFIPS","STCOFIPS","POPULATION","BUILDVALUE","AGRIVALUE","AREA","RISK_VALUE","RISK_SCORE","RISK_RATNG","RISK_SPCTL","EAL_SCORE","EAL_RATNG","EAL_SPCTL","EAL_VALT","EAL_VALB","EAL_VALP","EAL_VALPE","EAL_VALA","ALR_VALB","ALR_VALP","ALR_VALA","ALR_NPCTL","ALR_VRA_NPCTL","SOVI_SCORE","SOVI_RATNG","SOVI_SPCTL","RESL_SCORE","RESL_RATNG","RESL_SPCTL","RESL_VALUE","CRF_VALUE","Avalanche_EVNTS","Avalanche_AFREQ","Avalanche_EXP_AREA","Avalanche_EXPB","Avalanche_EXPP","Avalanche_EXPPE","Avalanche_EXPT","Avalanche_HLRB","Avalanche_HLRP","Avalanche_HLRR","Avalanche_EALB","Avalanche_EALP","Avalanche_EALPE","Avalanche_EALT","Avalanche_EALS","Avalanche_EALR","Avalanche_ALRB",
"Avalanche_ALRP","Avalanche_ALR_NPCTL","Avalanche_RISKV","Avalanche_RISKS",
"Avalanche_RISKR","Coastal_Flooding_EVNTS","Coastal_Flooding_AFREQ","Coastal_Flooding_EXP_AREA","Coastal_Flooding_EXPB","Coastal_Flooding_EXPP","Coastal_Flooding_EXPPE","Coastal_Flooding_EXPT","Coastal_Flooding_HLRB","Coastal_Flooding_HLRP","Coastal_Flooding_HLRR","Coastal_Flooding_EALB","Coastal_Flooding_EALP","Coastal_Flooding_EALPE","Coastal_Flooding_EALT","Coastal_Flooding_EALS","Coastal_Flooding_EALR","Coastal_Flooding_ALRB","Coastal_Flooding_ALRP","Coastal_Flooding_ALR_NPCTL","Coastal_Flooding_RISKV","Coastal_Flooding_RISKS","Coastal_Flooding_RISKR","Cold_Wave_EVNTS","Cold_Wave_AFREQ","Cold_Wave_EXP_AREA","Cold_Wave_EXPB","Cold_Wave_EXPP","Cold_Wave_EXPPE","Cold_Wave_EXPA","Cold_Wave_EXPT","Cold_Wave_HLRB","Cold_Wave_HLRP","Cold_Wave_HLRA","Cold_Wave_HLRR","Cold_Wave_EALB","Cold_Wave_EALP","Cold_Wave_EALPE","Cold_Wave_EALA",
"Cold_Wave_EALT","Cold_Wave_EALS","Cold_Wave_EALR","Cold_Wave_ALRB","Cold_Wave_ALRP","Cold_Wave_ALRA","Cold_Wave_ALR_NPCTL","Cold_Wave_RISKV","Cold_Wave_RISKS","Cold_Wave_RISKR","Drought_EVNTS","Drought_AFREQ","Drought_EXP_AREA","Drought_EXPA","Drought_EXPT","Drought_HLRA","Drought_HLRR","Drought_EALA","Drought_EALT","Drought_EALS","Drought_EALR","Drought_ALRA","Drought_ALR_NPCTL","Drought_RISKV","Drought_RISKS","Drought_RISKR","Earthquake_EVNTS","Earthquake_AFREQ","Earthquake_EXP_AREA","Earthquake_EXPB","Earthquake_EXPP","Earthquake_EXPPE","Earthquake_EXPT","Earthquake_HLRB","Earthquake_HLRP","Earthquake_HLRR","Earthquake_EALB","Earthquake_EALP","Earthquake_EALPE","Earthquake_EALT","Earthquake_EALS","Earthquake_EALR","Earthquake_ALRB","Earthquake_ALRP","Earthquake_ALR_NPCTL","Earthquake_RISKV","Earthquake_RISKS","Earthquake_RISKR","Hail_EVNTS","Hail_AFREQ","Hail_EXP_AREA","Hail_EXPB","Hail_EXPP","Hail_EXPPE","Hail_EXPA","Hail_EXPT","Hail_HLRB","Hail_HLRP","Hail_HLRA","Hail_HLRR","Hail_EALB","Hail_EALP","Hail_EALPE","Hail_EALA","Hail_EALT","Hail_EALS","Hail_EALR","Hail_ALRB",
"Hail_ALRP","Hail_ALRA","Hail_ALR_NPCTL","Hail_RISKV","Hail_RISKS","Hail_RISKR","Heat_Wave_EVNTS","Heat_Wave_AFREQ","Heat_Wave_EXP_AREA","Heat_Wave_EXPB","Heat_Wave_EXPP","Heat_Wave_EXPPE","Heat_Wave_EXPA","Heat_Wave_EXPT","Heat_Wave_HLRB","Heat_Wave_HLRP","Heat_Wave_HLRA","Heat_Wave_HLRR","Heat_Wave_EALB","Heat_Wave_EALP","Heat_Wave_EALPE","Heat_Wave_EALA","Heat_Wave_EALT","Heat_Wave_EALS","Heat_Wave_EALR","Heat_Wave_ALRB","Heat_Wave_ALRP","Heat_Wave_ALRA","Heat_Wave_ALR_NPCTL","Heat_Wave_RISKV","Heat_Wave_RISKS","Heat_Wave_RISKR","Hurricane_EVNTS","Hurricane_AFREQ","Hurricane_EXP_AREA","Hurricane_EXPB","Hurricane_EXPP","Hurricane_EXPPE","Hurricane_EXPA","Hurricane_EXPT","Hurricane_HLRB","Hurricane_HLRP","Hurricane_HLRA","Hurricane_HLRR","Hurricane_EALB","Hurricane_EALP","Hurricane_EALPE","Hurricane_EALA","Hurricane_EALT","Hurricane_EALS","Hurricane_EALR","Hurricane_ALRB","Hurricane_ALRP","Hurricane_ALRA","Hurricane_ALR_NPCTL","Hurricane_RISKV","Hurricane_RISKS","Hurricane_RISKR","Ice_Storm_EVNTS","Ice_Storm_AFREQ","Ice_Storm_EXP_AREA","Ice_Storm_EXPB","Ice_Storm_EXPP","Ice_Storm_EXPPE","Ice_Storm_EXPT","Ice_Storm_HLRB","Ice_Storm_HLRP","Ice_Storm_HLRR","Ice_Storm_EALB","Ice_Storm_EALP","Ice_Storm_EALPE","Ice_Storm_EALT","Ice_Storm_EALS","Ice_Storm_EALR","Ice_Storm_ALRB","Ice_Storm_ALRP","Ice_Storm_ALR_NPCTL","Ice_Storm_RISKV","Ice_Storm_RISKS","Ice_Storm_RISKR","Landslide_EVNTS","Landslide_AFREQ","Landslide_EXP_AREA","Landslide_EXPB","Landslide_EXPP","Landslide_EXPPE","Landslide_EXPT",
"Landslide_HLRB","Landslide_HLRP","Landslide_HLRR","Landslide_EALB","Landslide_EALP","Landslide_EALPE","Landslide_EALT","Landslide_EALS","Landslide_EALR","Landslide_ALRB","Landslide_ALRP","Landslide_ALR_NPCTL","Landslide_RISKV","Landslide_RISKS","Landslide_RISKR","Lightning_EVNTS","Lightning_AFREQ","Lightning_EXP_AREA","Lightning_EXPB","Lightning_EXPP","Lightning_EXPPE","Lightning_EXPT","Lightning_HLRB","Lightning_HLRP","Lightning_HLRR","Lightning_EALB","Lightning_EALP","Lightning_EALPE","Lightning_EALT","Lightning_EALS","Lightning_EALR","Lightning_ALRB","Lightning_ALRP","Lightning_ALR_NPCTL","Lightning_RISKV","Lightning_RISKS","Lightning_RISKR","Riverine_Flooding_EVNTS","Riverine_Flooding_AFREQ","Riverine_Flooding_EXP_AREA","Riverine_Flooding_EXPB","Riverine_Flooding_EXPP","Riverine_Flooding_EXPPE","Riverine_Flooding_EXPA","Riverine_Flooding_EXPT","Riverine_Flooding_HLRB","Riverine_Flooding_HLRP","Riverine_Flooding_HLRA","Riverine_Flooding_HLRR","Riverine_Flooding_EALB","Riverine_Flooding_EALP","Riverine_Flooding_EALPE","Riverine_Flooding_EALA","Riverine_Flooding_EALT","Riverine_Flooding_EALS","Riverine_Flooding_EALR","Riverine_Flooding_ALRB","Riverine_Flooding_ALRP","Riverine_Flooding_ALRA","Riverine_Flooding_ALR_NPCTL","Riverine_Flooding_RISKV","Riverine_Flooding_RISKS","Riverine_Flooding_RISKR","Strong_Wind_EVNTS","Strong_Wind_AFREQ","Strong_Wind_EXP_AREA","Strong_Wind_EXPB","Strong_Wind_EXPP","Strong_Wind_EXPPE","Strong_Wind_EXPA","Strong_Wind_EXPT","Strong_Wind_HLRB","Strong_Wind_HLRP","Strong_Wind_HLRA","Strong_Wind_HLRR","Strong_Wind_EALB","Strong_Wind_EALP",
"Strong_Wind_EALPE","Strong_Wind_EALA","Strong_Wind_EALT","Strong_Wind_EALS","Strong_Wind_EALR","Strong_Wind_ALRB","Strong_Wind_ALRP","Strong_Wind_ALRA","Strong_Wind_ALR_NPCTL","Strong_Wind_RISKV","Strong_Wind_RISKS","Strong_Wind_RISKR","Tornado_EVNTS","Tornado_AFREQ","Tornado_EXP_AREA","Tornado_EXPB","Tornado_EXPP","Tornado_EXPPE","Tornado_EXPA","Tornado_EXPT","Tornado_HLRB","Tornado_HLRP","Tornado_HLRA","Tornado_HLRR","Tornado_EALB","Tornado_EALP","Tornado_EALPE","Tornado_EALA","Tornado_EALT","Tornado_EALS","Tornado_EALR","Tornado_ALRB","Tornado_ALRP","Tornado_ALRA","Tornado_ALR_NPCTL","Tornado_RISKV","Tornado_RISKS","Tornado_RISKR","Tsunami_EVNTS","Tsunami_AFREQ","Tsunami_EXP_AREA","Tsunami_EXPB","Tsunami_EXPP","Tsunami_EXPPE","Tsunami_EXPT","Tsunami_HLRB","Tsunami_HLRP","Tsunami_HLRR","Tsunami_EALB","Tsunami_EALP","Tsunami_EALPE","Tsunami_EALT","Tsunami_EALS","Tsunami_EALR","Tsunami_ALRB","Tsunami_ALRP","Tsunami_ALR_NPCTL","Tsunami_RISKV","Tsunami_RISKS","Tsunami_RISKR","Volcano_EVNTS","Volcano_AFREQ","Volcano_EXP_AREA","Volcano_EXPB","Volcano_EXPP","Volcano_EXPPE","Volcano_EXPT","Volcano_HLRB","Volcano_HLRP","Volcano_HLRR","Volcano_EALB","Volcano_EALP","Volcano_EALPE","Volcano_EALT","Volcano_EALS","Volcano_EALR","Volcano_ALRB","Volcano_ALRP","Volcano_ALR_NPCTL","Volcano_RISKV","Volcano_RISKS","Volcano_RISKR","Wildfire_EVNTS","Wildfire_AFREQ","Wildfire_EXP_AREA","Wildfire_EXPB","Wildfire_EXPP","Wildfire_EXPPE","Wildfire_EXPA","Wildfire_EXPT","Wildfire_HLRB","Wildfire_HLRP","Wildfire_HLRA",
"Wildfire_HLRR","Wildfire_EALB","Wildfire_EALP","Wildfire_EALPE","Wildfire_EALA","Wildfire_EALT","Wildfire_EALS","Wildfire_EALR","Wildfire_ALRB","Wildfire_ALRP","Wildfire_ALRA","Wildfire_ALR_NPCTL","Wildfire_RISKV","Wildfire_RISKS","Wildfire_RISKR","Winter_Weather_EVNTS","Winter_Weather_AFREQ","Winter_Weather_EXP_AREA","Winter_Weather_EXPB","Winter_Weather_EXPP","Winter_Weather_EXPPE","Winter_Weather_EXPA","Winter_Weather_EXPT","Winter_Weather_HLRB","Winter_Weather_HLRP","Winter_Weather_HLRA","Winter_Weather_HLRR","Winter_Weather_EALB","Winter_Weather_EALP","Winter_Weather_EALPE","Winter_Weather_EALA","Winter_Weather_EALT","Winter_Weather_EALS","Winter_Weather_EALR","Winter_Weather_ALRB","Winter_Weather_ALRP","Winter_Weather_ALRA","Winter_Weather_ALR_NPCTL","Winter_Weather_RISKV","Winter_Weather_RISKS","Winter_Weather_RISKR","NRI_VER"]
fema_data.drop(columns=["OID_","NRI_ID","COUNTYTYPE","COUNTYFIPS","STCOFIPS","POPULATION","BUILDVALUE","AGRIVALUE","AREA","RISK_VALUE","RISK_SPCTL","EAL_SCORE","EAL_RATNG","EAL_SPCTL","EAL_VALT","EAL_VALB","EAL_VALP","EAL_VALPE","EAL_VALA","ALR_VALB","ALR_VALP","ALR_VALA","ALR_VRA_NPCTL","SOVI_SCORE","SOVI_RATNG","SOVI_SPCTL","RESL_SCORE","RESL_RATNG","RESL_SPCTL","RESL_VALUE","CRF_VALUE","Avalanche_EVNTS","Avalanche_AFREQ","Avalanche_EXP_AREA","Avalanche_EXPB","Avalanche_EXPP","Avalanche_EXPPE","Avalanche_EXPT","Avalanche_HLRB","Avalanche_HLRP","Avalanche_HLRR","Avalanche_EALB","Avalanche_EALP","Avalanche_EALPE","Avalanche_EALT","Avalanche_EALS","Avalanche_EALR","Avalanche_ALRB","Avalanche_ALRP","Avalanche_RISKV","Avalanche_RISKS","Avalanche_RISKR","Coastal_Flooding_EVNTS","Coastal_Flooding_AFREQ","Coastal_Flooding_EXP_AREA","Coastal_Flooding_EXPB","Coastal_Flooding_EXPP","Coastal_Flooding_EXPPE",
"Coastal_Flooding_EXPT","Coastal_Flooding_HLRB","Coastal_Flooding_HLRP","Coastal_Flooding_HLRR","Coastal_Flooding_EALB","Coastal_Flooding_EALP","Coastal_Flooding_EALPE","Coastal_Flooding_EALT","Coastal_Flooding_EALS","Coastal_Flooding_EALR","Coastal_Flooding_ALRB","Coastal_Flooding_ALRP","Coastal_Flooding_RISKV","Coastal_Flooding_RISKS","Coastal_Flooding_RISKR","Cold_Wave_EVNTS","Cold_Wave_AFREQ","Cold_Wave_EXP_AREA","Cold_Wave_EXPB","Cold_Wave_EXPP","Cold_Wave_EXPPE","Cold_Wave_EXPA","Cold_Wave_EXPT","Cold_Wave_HLRB","Cold_Wave_HLRP","Cold_Wave_HLRA","Cold_Wave_HLRR","Cold_Wave_EALB","Cold_Wave_EALP","Cold_Wave_EALPE","Cold_Wave_EALA","Cold_Wave_EALT","Cold_Wave_EALS","Cold_Wave_EALR","Cold_Wave_ALRB","Cold_Wave_ALRP","Cold_Wave_ALRA","Cold_Wave_RISKV","Cold_Wave_RISKS","Cold_Wave_RISKR","Drought_EVNTS","Drought_AFREQ","Drought_EXP_AREA","Drought_EXPA","Drought_EXPT","Drought_HLRA","Drought_HLRR","Drought_EALA","Drought_EALT","Drought_EALS","Drought_EALR","Drought_ALRA","Drought_RISKV","Drought_RISKS","Drought_RISKR","Earthquake_EVNTS","Earthquake_AFREQ","Earthquake_EXP_AREA","Earthquake_EXPB","Earthquake_EXPP","Earthquake_EXPPE","Earthquake_EXPT","Earthquake_HLRB","Earthquake_HLRP","Earthquake_HLRR","Earthquake_EALB",
"Earthquake_EALP","Earthquake_EALPE","Earthquake_EALT","Earthquake_EALS","Earthquake_EALR","Earthquake_ALRB","Earthquake_ALRP","Earthquake_RISKV","Earthquake_RISKS","Earthquake_RISKR","Hail_EVNTS","Hail_AFREQ","Hail_EXP_AREA","Hail_EXPB","Hail_EXPP","Hail_EXPPE","Hail_EXPA","Hail_EXPT","Hail_HLRB","Hail_HLRP","Hail_HLRA","Hail_HLRR","Hail_EALB","Hail_EALP","Hail_EALPE","Hail_EALA","Hail_EALT","Hail_EALS","Hail_EALR","Hail_ALRB","Hail_ALRP","Hail_ALRA","Hail_RISKV","Hail_RISKS","Hail_RISKR","Heat_Wave_EVNTS","Heat_Wave_AFREQ","Heat_Wave_EXP_AREA","Heat_Wave_EXPB","Heat_Wave_EXPP","Heat_Wave_EXPPE","Heat_Wave_EXPA","Heat_Wave_EXPT","Heat_Wave_HLRB","Heat_Wave_HLRP","Heat_Wave_HLRA","Heat_Wave_HLRR","Heat_Wave_EALB","Heat_Wave_EALP","Heat_Wave_EALPE","Heat_Wave_EALA","Heat_Wave_EALT","Heat_Wave_EALS","Heat_Wave_EALR","Heat_Wave_ALRB","Heat_Wave_ALRP","Heat_Wave_ALRA","Heat_Wave_RISKV","Heat_Wave_RISKS","Heat_Wave_RISKR","Hurricane_EVNTS","Hurricane_AFREQ","Hurricane_EXP_AREA","Hurricane_EXPB","Hurricane_EXPP","Hurricane_EXPPE","Hurricane_EXPA","Hurricane_EXPT","Hurricane_HLRB","Hurricane_HLRP","Hurricane_HLRA","Hurricane_HLRR","Hurricane_EALB","Hurricane_EALP","Hurricane_EALPE","Hurricane_EALA","Hurricane_EALT","Hurricane_EALS","Hurricane_EALR","Hurricane_ALRB","Hurricane_ALRP","Hurricane_ALRA","Hurricane_RISKV","Hurricane_RISKS","Hurricane_RISKR","Ice_Storm_EVNTS","Ice_Storm_AFREQ","Ice_Storm_EXP_AREA","Ice_Storm_EXPB","Ice_Storm_EXPP","Ice_Storm_EXPPE","Ice_Storm_EXPT","Ice_Storm_HLRB","Ice_Storm_HLRP","Ice_Storm_HLRR","Ice_Storm_EALB","Ice_Storm_EALP","Ice_Storm_EALPE","Ice_Storm_EALT","Ice_Storm_EALS","Ice_Storm_EALR","Ice_Storm_ALRB","Ice_Storm_ALRP","Ice_Storm_RISKV","Ice_Storm_RISKS","Ice_Storm_RISKR","Landslide_EVNTS","Landslide_AFREQ","Landslide_EXP_AREA","Landslide_EXPB","Landslide_EXPP","Landslide_EXPPE","Landslide_EXPT",
"Landslide_HLRB","Landslide_HLRP","Landslide_HLRR","Landslide_EALB","Landslide_EALP","Landslide_EALPE","Landslide_EALT","Landslide_EALS","Landslide_EALR","Landslide_ALRB","Landslide_ALRP","Landslide_RISKV","Landslide_RISKS","Landslide_RISKR","Lightning_EVNTS","Lightning_AFREQ","Lightning_EXP_AREA","Lightning_EXPB","Lightning_EXPP","Lightning_EXPPE","Lightning_EXPT","Lightning_HLRB","Lightning_HLRP","Lightning_HLRR","Lightning_EALB","Lightning_EALP","Lightning_EALPE","Lightning_EALT","Lightning_EALS","Lightning_EALR","Lightning_ALRB","Lightning_ALRP","Lightning_RISKV","Lightning_RISKS","Lightning_RISKR",
"Riverine_Flooding_EVNTS","Riverine_Flooding_AFREQ","Riverine_Flooding_EXP_AREA","Riverine_Flooding_EXPB","Riverine_Flooding_EXPP","Riverine_Flooding_EXPPE","Riverine_Flooding_EXPA","Riverine_Flooding_EXPT","Riverine_Flooding_HLRB","Riverine_Flooding_HLRP","Riverine_Flooding_HLRA","Riverine_Flooding_HLRR","Riverine_Flooding_EALB","Riverine_Flooding_EALP","Riverine_Flooding_EALPE","Riverine_Flooding_EALA","Riverine_Flooding_EALT","Riverine_Flooding_EALS","Riverine_Flooding_EALR","Riverine_Flooding_ALRB","Riverine_Flooding_ALRP","Riverine_Flooding_ALRA","Riverine_Flooding_RISKV","Riverine_Flooding_RISKS","Riverine_Flooding_RISKR","Strong_Wind_EVNTS","Strong_Wind_AFREQ","Strong_Wind_EXP_AREA","Strong_Wind_EXPB","Strong_Wind_EXPP","Strong_Wind_EXPPE","Strong_Wind_EXPA","Strong_Wind_EXPT","Strong_Wind_HLRB","Strong_Wind_HLRP","Strong_Wind_HLRA","Strong_Wind_HLRR","Strong_Wind_EALB","Strong_Wind_EALP","Strong_Wind_EALPE","Strong_Wind_EALA","Strong_Wind_EALT","Strong_Wind_EALS","Strong_Wind_EALR","Strong_Wind_ALRB","Strong_Wind_ALRP","Strong_Wind_ALRA","Strong_Wind_RISKV","Strong_Wind_RISKS","Strong_Wind_RISKR","Tornado_EVNTS","Tornado_AFREQ","Tornado_EXP_AREA","Tornado_EXPB","Tornado_EXPP","Tornado_EXPPE","Tornado_EXPA","Tornado_EXPT","Tornado_HLRB","Tornado_HLRP","Tornado_HLRA","Tornado_HLRR","Tornado_EALB","Tornado_EALP","Tornado_EALPE","Tornado_EALA","Tornado_EALT","Tornado_EALS","Tornado_EALR","Tornado_ALRB","Tornado_ALRP","Tornado_ALRA","Tornado_RISKV","Tornado_RISKS","Tornado_RISKR",
"Tsunami_EVNTS","Tsunami_AFREQ","Tsunami_EXP_AREA","Tsunami_EXPB","Tsunami_EXPP","Tsunami_EXPPE","Tsunami_EXPT","Tsunami_HLRB","Tsunami_HLRP","Tsunami_HLRR","Tsunami_EALB","Tsunami_EALP","Tsunami_EALPE","Tsunami_EALT","Tsunami_EALS","Tsunami_EALR","Tsunami_ALRB","Tsunami_ALRP","Tsunami_RISKV","Tsunami_RISKS","Tsunami_RISKR","Volcano_EVNTS","Volcano_AFREQ","Volcano_EXP_AREA","Volcano_EXPB","Volcano_EXPP","Volcano_EXPPE","Volcano_EXPT","Volcano_HLRB","Volcano_HLRP","Volcano_HLRR","Volcano_EALB","Volcano_EALP","Volcano_EALPE","Volcano_EALT","Volcano_EALS","Volcano_EALR","Volcano_ALRB","Volcano_ALRP","Volcano_RISKV","Volcano_RISKS","Volcano_RISKR","Wildfire_EVNTS","Wildfire_AFREQ","Wildfire_EXP_AREA","Wildfire_EXPB","Wildfire_EXPP","Wildfire_EXPPE","Wildfire_EXPA","Wildfire_EXPT","Wildfire_HLRB","Wildfire_HLRP","Wildfire_HLRA","Wildfire_HLRR","Wildfire_EALB","Wildfire_EALP","Wildfire_EALPE","Wildfire_EALA","Wildfire_EALT","Wildfire_EALS","Wildfire_EALR","Wildfire_ALRB","Wildfire_ALRP","Wildfire_ALRA","Wildfire_RISKV","Wildfire_RISKS","Wildfire_RISKR","Winter_Weather_EVNTS","Winter_Weather_AFREQ","Winter_Weather_EXP_AREA","Winter_Weather_EXPB","Winter_Weather_EXPP","Winter_Weather_EXPPE","Winter_Weather_EXPA","Winter_Weather_EXPT","Winter_Weather_HLRB","Winter_Weather_HLRP","Winter_Weather_HLRA","Winter_Weather_HLRR","Winter_Weather_EALB","Winter_Weather_EALP","Winter_Weather_EALPE","Winter_Weather_EALA","Winter_Weather_EALT","Winter_Weather_EALS","Winter_Weather_EALR","Winter_Weather_ALRB","Winter_Weather_ALRP","Winter_Weather_ALRA","Winter_Weather_RISKV","Winter_Weather_RISKS","Winter_Weather_RISKR","NRI_VER"], inplace=True)
fema_data = fema_data.dropna(subset=['COUNTY', 'STATEABBRV'])
#Helper function that does the actual work of getting the risk
def get_weather_risk(season, county, state):
    county = county.strip().title()
    state = state.strip()
    print(f"County: {county}")
    print(f"State: {state}")
    print(f"FEMA Data Columns: {fema_data.columns}")
    destination_check = fema_data[(fema_data['COUNTY'] == county) & (fema_data['STATEABBRV'] == state)]
    print(f"Destination Check: {destination_check}")
    if destination_check.empty:
        return {"error": f"The destination '{county}, {state}' was not found in the dataset."}

    fema_data_row = destination_check.iloc[0]
    
    risk_info = {
        "county": county,
        "state": state,
        "overall_risk_score": fema_data_row["ALR_NPCTL"]
    }

    # Check the season and append specific weather risks to the dictionary
    if season.lower() == "spring":
        spring_risks = (fema_data_row["Tornado_ALR_NPCTL"] + fema_data_row["Strong_Wind_ALR_NPCTL"] + fema_data_row["Riverine_Flooding_ALR_NPCTL"] + fema_data_row["Wildfire_ALR_NPCTL"] + fema_data_row["Landslide_ALR_NPCTL"] + fema_data_row["Lightning_ALR_NPCTL"] + fema_data_row["Hail_ALR_NPCTL"]) / 7
        risk_info.update({
            "tornado_risk": fema_data_row["Tornado_ALR_NPCTL"],
            "strong_wind_risk": fema_data_row["Strong_Wind_ALR_NPCTL"],
            "riverine_flooding_risk": fema_data_row["Riverine_Flooding_ALR_NPCTL"],
            "wildfire_risk": fema_data_row["Wildfire_ALR_NPCTL"],
            "landslide_risk": fema_data_row["Landslide_ALR_NPCTL"],
            "lightning_risk": fema_data_row["Lightning_ALR_NPCTL"],
            "hail_risk": fema_data_row["Hail_ALR_NPCTL"],
            "season_risk": spring_risks
        })
    
    elif season.lower() == "summer":
        summer_risks = (fema_data_row["Heat_Wave_ALR_NPCTL"] + fema_data_row["Wildfire_ALR_NPCTL"] + fema_data_row["Strong_Wind_ALR_NPCTL"] + fema_data_row["Hurricane_ALR_NPCTL"] + fema_data_row["Lightning_ALR_NPCTL"] + fema_data_row["Tornado_ALR_NPCTL"] + fema_data_row["Hail_ALR_NPCTL"]) / 7
        risk_info.update({
            "heat_wave_risk": fema_data_row["Heat_Wave_ALR_NPCTL"],
            "wildfire_risk": fema_data_row["Wildfire_ALR_NPCTL"],
            "strong_wind_risk": fema_data_row["Strong_Wind_ALR_NPCTL"],
            "hurricane_risk": fema_data_row["Hurricane_ALR_NPCTL"],
            "lightning_risk": fema_data_row["Lightning_ALR_NPCTL"],
            "tornado_risk": fema_data_row["Tornado_ALR_NPCTL"],
            "hail_risk": fema_data_row["Hail_ALR_NPCTL"],
            "season_risk": summer_risks
        })

    elif season.lower() == "fall":
        fall_risks = (fema_data_row["Hurricane_ALR_NPCTL"] + fema_data_row["Strong_Wind_ALR_NPCTL"] + fema_data_row["Wildfire_ALR_NPCTL"] + fema_data_row["Tornado_ALR_NPCTL"] + fema_data_row["Landslide_ALR_NPCTL"] + fema_data_row["Lightning_ALR_NPCTL"] + fema_data_row["Riverine_Flooding_ALR_NPCTL"] + fema_data_row["Coastal_Flooding_ALR_NPCTL"] + fema_data_row["Hail_ALR_NPCTL"]) / 9
        risk_info.update({
            "hurricane_risk": fema_data_row["Hurricane_ALR_NPCTL"],
            "strong_wind_risk": fema_data_row["Strong_Wind_ALR_NPCTL"],
            "wildfire_risk": fema_data_row["Wildfire_ALR_NPCTL"],
            "tornado_risk": fema_data_row["Tornado_ALR_NPCTL"],
            "landslide_risk": fema_data_row["Landslide_ALR_NPCTL"],
            "lightning_risk": fema_data_row["Lightning_ALR_NPCTL"],
            "riverine_flooding_risk": fema_data_row["Riverine_Flooding_ALR_NPCTL"],
            "coastal_flooding_risk": fema_data_row["Coastal_Flooding_ALR_NPCTL"],
            "hail_risk": fema_data_row["Hail_ALR_NPCTL"],
            "season_risk": fall_risks
        })

    elif season.lower() == "winter":
        winter_risks = (fema_data_row["Winter_Weather_ALR_NPCTL"] + fema_data_row["Cold_Wave_ALR_NPCTL"] + fema_data_row["Ice_Storm_ALR_NPCTL"] + fema_data_row["Strong_Wind_ALR_NPCTL"] + fema_data_row["Riverine_Flooding_ALR_NPCTL"] + fema_data_row["Coastal_Flooding_ALR_NPCTL"] + fema_data_row["Avalanche_ALR_NPCTL"] + fema_data_row["Hail_ALR_NPCTL"] + fema_data_row["Earthquake_ALR_NPCTL"]) / 9
        risk_info.update({
            "winter_weather_risk": fema_data_row["Winter_Weather_ALR_NPCTL"],
            "cold_wave_risk": fema_data_row["Cold_Wave_ALR_NPCTL"],
            "ice_storm_risk": fema_data_row["Ice_Storm_ALR_NPCTL"],
            "strong_wind_risk": fema_data_row["Strong_Wind_ALR_NPCTL"],
            "riverine_flooding_risk": fema_data_row["Riverine_Flooding_ALR_NPCTL"],
            "coastal_flooding_risk": fema_data_row["Coastal_Flooding_ALR_NPCTL"],
            "avalanche_risk": fema_data_row["Avalanche_ALR_NPCTL"],
            "hail_risk": fema_data_row["Hail_ALR_NPCTL"],
            "earthquake_risk": fema_data_row["Earthquake_ALR_NPCTL"],
            "season_risk": winter_risks
        })
    else:
        return {"error": "Invalid season. Please choose from 'spring', 'summer', 'fall', or 'winter'."}
    return risk_info
#Creating the endpoints
@app.get("/weather_risk/{county}/{stateabbrv}/{season}")
async def find_risks(county:str, stateabbrv:str, season:str, include_details: bool = True):
    risk_info = get_weather_risk(season, county, stateabbrv)
    if include_details:
        return risk_info
    else:
        return {"county": county, "state": stateabbrv, "overall_risk_score": risk_info["overall_risk_score"], season_risk: risk_info["season_risk"]} 
@app.get("/counties")
async def get_counties():
    return fema_data["COUNTY"].unique().tolist()
@app.get("/states_and_territories")
async def get_states_and_territories():
    return fema_data["STATEABBRV"].unique().tolist()
class TravelRequest(BaseModel):
    county:str
    state:str
    season:str
class MultipleTravelRequest(BaseModel):
    destinations: List[TravelRequest]
@app.post("/custom_travel_risks")
async def create_report(request: MultipleTravelRequest):
    risk_info = []
    for destination in request.destinations:
        risk_info.append(get_weather_risk(destination.season, destination.county, destination.state))
    return {"custom_report":risk_info}


    