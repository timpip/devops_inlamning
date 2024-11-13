import requests
from datetime import datetime
import datetime
import streamlit as st
import pandas as pd

def data_SMHI():
    now = datetime.datetime.now()
    lon = 18.0215
    lat = 59.3099
    formatted_datetime = now.strftime('%Y-%m-%d %H:%M:%S')
    URL = f"https://opendata-download-metfcst.smhi.se/api/category/pmp3g/version/2/geotype/point/lon/{lon}/lat/{lat}/data.json"
    response = requests.get(URL)
    #kolla om ok
    code = response.status_code
    SMHIresponse = response.json()

    date = SMHIresponse["timeSeries"][0]["validTime"]
    onlydate = date[:10]

    validTime = SMHIresponse["timeSeries"][0]["validTime"]
    validdate = str(validTime[:10])
    validTimeINT = int(validTime[11:13])
    time = validTimeINT +1

    samlad_data_dict = {}
    #Fyller dict med all våran data till en rad
    for items in SMHIresponse["timeSeries"][0]["parameters"][:25]:
        samlad_data_dict["created"] = formatted_datetime
        samlad_data_dict["longitude"] = SMHIresponse["geometry"]["coordinates"][0][0]
        samlad_data_dict["latitude"] = SMHIresponse["geometry"]["coordinates"][0][1]
        samlad_data_dict["date"] = validdate
        samlad_data_dict["hour"] = time
        

        for items in SMHIresponse["timeSeries"][0]["parameters"][:25]:
            
            if items["name"] == "t":
                
                temp = items["values"][0]
                samlad_data_dict["temperature"] = temp
            
            if items["name"] == "pcat":
                
                prec = items["values"][0]

                if prec <= 0:
                    rain = False

                elif prec > 0:
                    rain = True

        samlad_data_dict["rainOrSnow"] = rain
        samlad_data_dict["provider"] ="SMHI"
        df = pd.DataFrame([samlad_data_dict])
    
    return df, code, samlad_data_dict


def page():
    st.title("Weather checker :sun_with_face::rain_cloud::lightning:")
    global lat, lon
    option = st.selectbox(
    "Choose where to show weather?",
    ("Stockholm", "Kiruna", "Ystad"),    
    )

    st.write("You selected:", option)

    if option == "Kiruna":
        lon = 20.225
        lat = 67.855
    if option == "Stockholm":
        lon = 18.0215
        lat = 59.3099
    if option == "Ystad":
        lon = 13.820
        lat = 55.429
    if st.button('Show weather! :cloud:'):
        st.balloons()
        st.table(data_SMHI())

if __name__ == "__main__":
    page()
