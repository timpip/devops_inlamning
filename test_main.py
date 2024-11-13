import requests
from main import data_SMHI

def test_API_response():
    URL = f"https://opendata-download-metfcst.smhi.se/api/category/pmp3g/version/2/geotype/point/lon/18.0215/lat/59.3099/data.json"
    response = requests.get(URL)
    #kolla om ok
    code = response.status_code
    assert code == 200, f"Expected status code 200, but got {code}"


def test_unit():
    samlad_data_dict = data_SMHI()
    
    assert samlad_data_dict['provider'].values[0] == "SMHI"

