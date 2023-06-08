""" File to handle Question pre-processing steps"""
from time import strftime, localtime
import os

import re
import requests
from dotenv import load_dotenv
from ETL.extract_users import get_user_details
from ETL.load_pg_process_data import PGInsertData

def get_questions():
    """
    Function to get Questions for pre-defined tags - {mysql and python}
    """
    load_dotenv()
    # Check if the request was successful (status code 200)
    base_url = "https://api.stackexchange.com/2.3/questions"
    site = "stackoverflow"
    tagged = 'mysql;python'
    search_filter = '!BRwFZWvJ.iUeCIpDNUB0-1X4lnzhsU'
    key = os.environ.get('key')
    access_token = os.environ.get('access_token')
    page_size=30
    fromdate = 1682899200
    todate = 1685491200
    regex = re.compile('<.*?>|&([a-z0-9]+|#[0-9]{1,6}|#x[0-9a-f]{1,6});') 

    response = requests.get(
        f"{base_url}?pagesize={page_size}&order=desc&sort=creation&tagged={tagged}&site={site}&filter={search_filter}&fromdate={fromdate}&todate={todate}&key={key}&access_token={access_token}",
        timeout=10
    )

    if response.status_code == 200:
        data = response.json()
        items = data['items']

        for item in items:
            tags = item['tags']
            user_id = item['owner']['user_id']
            # Save user data to PG Table
            get_user_details(user_id)

            comment_count = item['comment_count']
            is_answered = item['is_answered']
            view_count = item['view_count']
            answer_count = item['answer_count']
            score = item['score']
            last_activity_date = strftime('%Y-%m-%d %H:%M:%S', localtime(item['last_activity_date']))
            last_edit_date = strftime('%Y-%m-%d %H:%M:%S', localtime(item['last_edit_date'])) if 'last_edit_date' in item else strftime('%Y-%m-%d %H:%M:%S', localtime(0000000000))
            question_id = item['question_id']
            link = item['link']
            title = item['title']
            body = item['body']
            clean_body = re.sub(regex, '', body)

            data = (
                user_id,
                comment_count,
                is_answered,
                view_count,
                answer_count,
                score,
                last_activity_date,
                last_edit_date,
                question_id,
                link,
                title,
                clean_body,
                tags
            )
            # Load
            question_data = PGInsertData()
            question_data.insert_questions_data(data=data)
    else:
        print("Error occurred while fetching Comments data.")
