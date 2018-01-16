# Catalog project
This program was created to run 3 queries against the news database.

## How to get up and running
### Requirements
* python 3
### Create views
`create view total_requests as select to_char(time, 'fmMonth DD, YYYY') as day, count(*) as requests from log group by day;`

`create view total_errors as select to_char(time, 'fmMonth DD, YYYY') as day, count(*) as errors from log where status like '4%' or status like '5%' group by day;`

`create view percent_errors as select r.day, sum(round(100*(cast(e.errors as decimal)/cast(r.requests as decimal)),1)) as total_percent from total_requests r join total_errors e on r.day = e.day group by r.day;`

### Run
* run `python3 log.py'
