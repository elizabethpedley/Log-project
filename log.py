#!/usr/bin/env python3
from logdb import pop_articles, pop_authors, error_days
"""This module cycles through results of database queries to present them in a
 more readable format."""

articles = pop_articles()
authors = pop_authors()
days = error_days()


def pop_articles_results(results):
    """Cycles through a list to present the data in a more readable format."""
    for x in results:
        print('"' + x[0] + '" - ' + str(x[1]) + ' views')


def pop_authors_results(results):
    """Cycles through a list to present the data in a more readable format."""
    for x in results:
        print(x[0] + ' - ' + str(x[1]) + ' views')


def error_days_results(results):
    """Cycles through a list to present the data in a more readable format."""
    for x in results:
        print(x[0] + ' - ' + str(x[1]) + '% errors')


print('These are the Three most popular articles. \n')
pop_articles_results(articles)
print('\nThese are the most popular authors. \n')
pop_authors_results(authors)
print('\nThese are the days that more than 1% of requests led to errors.\n')
error_days_results(days)
