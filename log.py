#! python3
from logdb import pop_articles, pop_authors, error_days

articles = pop_articles()
authors = pop_authors()
days = error_days()


def pop_articles_results(results):
    for x in results:
        print('"' + x[0] + '" - ' + str(x[1]) + ' views')


def pop_authors_results(results):
    for x in results:
        print(x[0] + ' - ' + str(x[1]) + ' views')


def error_days_results(results):
    for x in results:
        print(x[0] + ' - ' + str(x[1]) + '% errors')


print('These are the Three most popular articles.')
pop_articles_results(articles)
print('These are the most popular authors.')
pop_authors_results(authors)
print('These are the days that more than 1% of requests led to errors.')
error_days_results(days)
