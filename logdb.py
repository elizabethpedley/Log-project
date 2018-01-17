#!/usr/bin/env python3
import psycopg2
"""logdb.py uses psql to querie the news database to answer 3 questions. """

news = 'dbname=news'


def pop_articles():
    """Returns the 3 most popular articles of all time from news database."""
    db = psycopg2.connect(news)
    c = db.cursor()
    content = "select articles.title, count(*) as views from articles join " \
        "log on log.path like concat('%',articles.slug) group by " \
        "articles.title order by views desc limit 3;"
    c.execute(content)
    return c.fetchall()
    db.close()


def pop_authors():
    """Returns the most popular article authors of all time."""
    db = psycopg2.connect(news)
    c = db.cursor()
    content = "select authors.name, count(*) as views from articles, authors,"\
        " log where authors.id = articles.author and log.path like"\
        " concat('%',articles.slug) group by authors.name order by views desc;"
    c.execute(content)
    return c.fetchall()
    db.close()


def error_days():
    """Returns the days that more than 1 percent of requests led to errors."""
    db = psycopg2.connect(news)
    c = db.cursor()
    content = "select * from percent_errors where total_percent > 1.0;"
    c.execute(content)
    return c.fetchall()
    db.close()
