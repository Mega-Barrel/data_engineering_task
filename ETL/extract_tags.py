"""
Module Establishing connection with stackexchange Tags API Endpoint to get popular tags
"""
from datetime import datetime
from time import strftime, localtime

import requests
from ETL.load_pg_process_data import PGInsertData

def get_popular_tags():
    """
    Function to get popular tags data
    """
    # Extraction
    base_url = "https://api.stackexchange.com/2.3/tags"
    site_name = "stackoverflow"
    page_number = 1
    page_size = 100
    order = 'desc'
    sort = 'popular'
    tfilter = '!6N4UX.)7jZK1X'
    fromdate = 1682899200
    todate = 1685491200

    response = requests.get(
        f"{base_url}?page={page_number}&pagesize={page_size}&fromdate={fromdate}&todate={todate}&order={order}&sort={sort}&site={site_name}&filter={tfilter}"
    )

    # Transformation
    if response.status_code == 200:
        data = response.json()
        trending_tags = data["items"]
        for tag in trending_tags:
            last_activity = strftime('%Y-%m-%d %H:%M:%S', localtime(tag['last_activity_date']))
            is_moderated = tag['is_moderator_only']
            popularity_count = tag['count']
            tag_name = tag['name']
            date = datetime.today().replace(day=1, month=5)

            data = (
                tag_name, popularity_count,
                is_moderated, last_activity,
                date
            )
            # Make a PGInsertData instance
            # Loading
            tag_data = PGInsertData()
            tag_data.insert_tags_data(data)
    else:
        print("Error occurred while fetching data.")
