from main import data_SMHI

def test_API_response():
    df, code, samlad_data_dict = data_SMHI()
    assert code == 200, f"Expected status code 200, but got {code}"


def test_unit():
    df, code, samlad_data_dict = data_SMHI()
    
    assert samlad_data_dict['provider'] == "SMHI"
