from main import data_SMHI

def test_API_response():
    df, code = data_SMHI()
    assert code == 200, f"Expected status code 200, but got {code}"
