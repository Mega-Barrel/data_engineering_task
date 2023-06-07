"""
Module Establishing connection with stackexchange Tags API Endpoint to get popular tags
"""
import json
import requests

def get_popular_tags():
    """
    Function to get popular tags data
    """

    base_url = "https://api.stackexchange.com/2.3/tags"
    site_name = "stackoverflow"
    page_number = 1
    page_size = 100
    order = 'desc'
    sort = 'popular'
    tfilter = '!6N4UX.)7jZK1X'

    response = requests.get(
        f"{base_url}?page={page_number}&pagesize={page_size}&order={order}&sort={sort}&site={site_name}&filter={tfilter}",
        timeout=10
    )

    if response.status_code == 200:
        data = response.json()
        with open('tags_data.json', 'w', encoding='utf-8') as response_data:
            json.dump(data, response_data, ensure_ascii=False, indent=4)
        # trending_tags = data["items"]
        # for tag in trending_tags:
        #     print(tag)
        #     print()
    else:
        print("Error occurred while fetching data.")

get_popular_tags()
