CREATE DATABASE IF NOT EXISTS packt_take_home;

CREATE TABLE IF NOT EXISTS public.popular_tags (
    id serial NOT NULL,
    tag_name CHARACTER VARYING,
    popularity_count BIGINT,
    last_activity_date CHARACTER VARYING,
    PRIMARY KEY (id)
);