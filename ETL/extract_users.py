"""
Extracting user's data from stackexchange /users/{idx} endpoint
"""
from time import strftime, localtime
import requests
from ETL.load_pg_process_data import PGInsertData

def get_user_details(user_id):
    """
    Function to process user's meta-data
    """
    # Extract
    base_url = "https://api.stackexchange.com/2.3/users"
    site = "stackoverflow"
    search_filter = '!)Dgrs*Zf0Ff1-JmanJdiT6bXi*EzQf(OVIVGF7IynBhQeA'
    key = "8huoT7h0E*jq93tyxr7bLA(("
    token = "5*XhzdJioX*ei9gdntMRDw))"
    usr_id = user_id

    query = f"{base_url}/{usr_id}?key={key}&access_token={token}&filter={search_filter}&site={site}"

    response = requests.get(
        query,
        timeout=1000
    )

    # Transform
    if response.status_code == 200:
        data = response.json()
        view_count = data['items'][0]['view_count']
        down_vote_count = data['items'][0]['down_vote_count']
        up_vote_count = data['items'][0]['up_vote_count']
        answer_count = data['items'][0]['answer_count']
        question_count = data['items'][0]['question_count']
        is_employee = data['items'][0]['is_employee']
        reputation = data['items'][0]['reputation'] if 'reputation' in data['items'][0] else 0
        creation_date = strftime('%Y-%m-%d %H:%M:%S', localtime(data['items'][0]['creation_date']))
        user_type = data['items'][0]['user_type']
        user_id = data['items'][0]['user_id']
        accept_rate = data['items'][0]['accept_rate'] if 'accept_rate' in data['items'][0] else 0
        about_me = data['items'][0]['about_me'] if 'about_me' in data['items'][0] else 'No data'
        website_url = data['items'][0]['website_url'] if 'website_url' in data['items'][0] else 'No data'
        display_name = data['items'][0]['display_name']
        location = data['items'][0]['location'] if 'location' in data['items'][0] else 'No data'

        data = (
            view_count,
            down_vote_count,
            up_vote_count,
            answer_count,
            question_count,
            is_employee,
            reputation,
            creation_date,
            user_type,
            user_id,
            accept_rate,
            about_me,
            website_url,
            display_name,
            location
        )

        # Load
        user_data = PGInsertData()
        user_data.insert_user_data(data)
    else:
        print("Error occurred while fetching data.")