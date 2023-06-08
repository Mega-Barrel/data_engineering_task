'''Main method'''

from ETL.extract_tags import get_popular_tags
from ETL.extract_questions import get_questions

def main():
    """Main method to call ETL function"""
    get_popular_tags()
    get_questions()

if __name__ == "__main__":
    main()
