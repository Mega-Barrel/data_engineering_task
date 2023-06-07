import json
import requests

def get_questions():
    """
    test
    """
    # Check if the request was successful (status code 200)
    base_url = "https://api.stackexchange.com/2.3/questions"
    site = "stackoverflow"
    tagged = 'mysql;python'
    search_filter = '!BRwFZWvJ.iUeCIpDNUB0-1X4lnzhsU'
    key = "8huoT7h0E*jq93tyxr7bLA(("
    access_token = "5*XhzdJioX*ei9gdntMRDw))"

    response = requests.get(
        f"{base_url}?order=desc&sort=creation&tagged={tagged}&site={site}&filter={search_filter}&key={key}&access_token={access_token}",
        timeout=10
    )

    if response.status_code == 200:
        data = response.json()
        with open('data.json', 'w', encoding='utf-8') as response_data:
            json.dump(data, response_data, ensure_ascii=False, indent=4)
    else:
        print("Error occurred while fetching data.")

get_questions()
