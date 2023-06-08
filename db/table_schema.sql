CREATE DATABASE IF NOT EXISTS packt_take_home;

CREATE TABLE IF NOT EXISTS public.tags (
    id serial NOT NULL,
    tag_name CHARACTER VARYING,
    popularity_count BIGINT,
    is_moderator BOOL,
    last_activity_date TIMESTAMP,
    popular_date TIMESTAMP,
    PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS public.user_stats (
    id serial NOT NULL,
    view_count INTEGER,
    down_vote_count INTEGER,
    up_vote_count INTEGER,
    answer_count INTEGER,
    question_count INTEGER,
    is_employee BOOL,
    reputation INTEGER,
    creation_date TIMESTAMP,
    user_type CHARACTER VARYING,
    user_id INTEGER,
    accept_rate INTEGER,
    about_me CHARACTER VARYING,
    website_url CHARACTER VARYING,
    display_name CHARACTER VARYING,
    location CHARACTER VARYING
);

CREATE TABLE IF NOT EXISTS public.questions (
    id serial NOT NULL,
    user_id INTEGER,
    comment_count INTEGER,
    is_answered BOOL,
    view_count INTEGER,
    answer_count INTEGER,
    score INTEGER,
    last_activity_date TIMESTAMP,
    last_edit_date TIMESTAMP,
    question_id INTEGER,
    link CHARACTER VARYING,
    title CHARACTER VARYING,
    body CHARACTER VARYING,
    tags TEXT []
);