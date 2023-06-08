# Data Engineering Task
Utilizing Stack Exchange Public API to query StackOverflow data.

# Steps to set-up the project

## requirements.txt file
This file contains the packages used to build the application

## Create a env folder
Create a environment folder to download packages required for this app
```text
python -m venv env
```

## Activate the environment
Depending on the OS using either Windows/Mac OS set up the env as follows
```
On windows:
    .\env\Scripts\activate

On Mac:
    source env/bin/activate
```

## Installing packages required for the project
```text
pip install -r requirements.txt
```

## Get access token for stackoverflow API
[How can I quickly get an access token for personal use?](https://stackapps.com/questions/9345/how-can-i-quickly-get-an-access-token-for-personal-use)

## Setup .env file
Create a .env file and add all your credentials inside it
```
key = "Add your stackoverflow Application key"
access_token = "Add your access token after completing above step"
PG_USER = "Add your PG Username"
PG_PW = "Add your PG Password"
PG_HOST = "localhost"
PG_DB = "packt_take_home"
PG_PORT = 5432
```

## How to run the script
```python
# Steps to run the app
Step 1: Download the zip code in you local system

Step 2: Install the packages from requirements.txt file

Step 3: Install the libraries for the application

Step 4: Setup the PostgreSQL instance on your local machine

Step 5: Run the SQL Table Schema on PostgreSQL, you can find Schema under db/table_schema.sql folder

Step 6: Configure the .env file with the credentials of PostgreSQL and Stackoverflow key, and access_token

Step 7: Run the following python command: **python main.py**
```