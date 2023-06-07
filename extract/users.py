"""
Extracting user's data from stackexchange /users/{idx} endpoint
"""
import requests

def get_user_details():
    """
    Function to process user's meta-data
    """
    base_url = "https://api.stackexchange.com/2.3/users"
    site = "stackoverflow"
    search_filter = '!)Dgrs*Zf0Ff1-JmanJdiT6bXi*EzQf(OVIVGF7IynBhQeA'
    key = "8huoT7h0E*jq93tyxr7bLA(("
    token = "5*XhzdJioX*ei9gdntMRDw))"
    usr_id = 1642231

    query = f"{base_url}/{usr_id}?key={key}&access_token={token}&filter={search_filter}&site={site}"

    response = requests.get(
        query,
        timeout=10
    )

    if response.status_code == 200:
        data = response.json()
        print(data)
    else:
        print("Error occurred while fetching data.")

get_user_details()
