"""Script to insert most popular tags - last month"""

from ETL.load_pg_connector import PGConn

class PGInsertData(PGConn):

    """
    Inherits PG connection object from PGConn class
    """

    def insert_tags_data(self, data):
        """
        Function to insert tags data into table
        
        :param: data -> data to be inserted into tags table
        """
        try:
            query = """
                INSERT INTO public.tags (
                    tag_name,
                    popularity_count,
                    is_moderator,
                    last_activity_date,
                    popular_date
                )   VALUES (
                    %s, %s,
                    %s, %s,
                    %s
                )
            """
            self._cursor.execute(query, data)
            self._db.commit()

            print('Tag Data Inserted successfully!!')
        except Exception as error:
            print("Error Occured while inserting Tag data!")
            print(f"More info on error: {error}")
        finally:
            if self._cursor:
                self._cursor.close()
    
    def insert_questions_data(self, data):
        """
        Function to insert questions data into table
        
        :param: data -> data to be inserted into questions table
        """
        try:
            query = """
                INSERT INTO public.questions (
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
                    body,
                    tags
                )   VALUES (
                    %s, %s, %s, %s,
                    %s, %s, %s, %s,
                    %s, %s, %s, %s,
                    %s
                )
            """
            self._cursor.execute(query, data)
            self._db.commit()

            print('Question Data Inserted successfully!!')
        except Exception as error:
            print("Error Occured while inserting Question data!")
            print(f"More info on error: {error}")
        finally:
            if self._cursor:
                self._cursor.close()

    def insert_user_data(self, data):
        """
        Function to push JSON data to PostgreSQL table
        
        :param: data -> data to be inserted into user_stats table
        """
        try:
            query = """
                INSERT INTO public.user_stats (
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
                ) VALUES (
                    %s, %s, %s,
                    %s, %s, %s,
                    %s, %s, %s,
                    %s, %s, %s,
                    %s, %s, %s
                )
            """
            self._cursor.execute(query, data)
            self._db.commit()
            print('User Data Inserted successfully!!')
        except Exception as error:
            print("Error Occured while inserting User data!")
            print(f"More info on error: {error}")
        finally:
            if self._cursor:
                self._cursor.close()
