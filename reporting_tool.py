#!/bin/env python2.7
# load the adapter
import psycopg2

# print the most popular articles of all time
def print_popular_articles():

    # Define the connection parameters
    conn_param = "dbname = news"

    # get a connection
    # if a connect cannot be made an exception will be raised here
    conn = psycopg2.connect(conn_param)

    # conn.cursor will return a cursor object
    cursor = conn.cursor()

    # Define the query to execute
    query = '''
	SELECT articles.title, count(*) as views
	FROM articles, log
	where log.path =  CONCAT('/article/', articles.slug)
	and log.status = '200 OK'
	group by articles.title
	order by views desc
	limit 3;
	'''
    # execute our Query
    cursor.execute(query)
    # retrieve the records from the database
    records = cursor.fetchall()

    print "\n" + "The most popular three articles of all time:" + "\n"
    for row in records:
        print "    \"{}\" -- {} views".format(row[0], row[1])
    # close the connection
    conn.close()

# print the most popular article authors of all time
def print_popular_authors():

    # Define the connection parameters
    conn_param = "dbname = news"

    # get a connection
    # if a connect cannot be made an exception will be raised here
    conn = psycopg2.connect(conn_param)

    # conn.cursor will return a cursor object
    cursor = conn.cursor()

    # Define the query to execute
    query = '''
		SELECT authors.name, count(*) as views
		  FROM authors,articles, log
		where log.path =  CONCAT('/article/', articles.slug)
		  and log.status = '200 OK'
		  and articles.author = authors.id
		group by authors.name
		order by views desc limit 4;
	'''
    # execute our Query
    cursor.execute(query)
    # retrieve the records from the database
    records = cursor.fetchall()

    print "\n" + "The most popular three authors of all time:" + "\n"
    for row in records:
        print "    {} -- {} views".format(row[0], row[1])
    # close the connection
    conn.close()


# print days on which more than 1% of requests lead to errors
def print_error_days():

    # Define the connection parameters
    conn_param = "dbname = news"

    # get a connection
    # if a connect cannot be made an exception will be raised here
    conn = psycopg2.connect(conn_param)

    # conn.cursor will return a cursor object
    cursor = conn.cursor()

    # Define the query to execute

    query = '''
	SELECT day, round((error * 1.0/total)*100, 1) as percent
	  from
	    (SELECT date(time) as day,
	    count(case when status='404 NOT FOUND' then 1 else null end) as error,
	    count(*) as total
		from log
		group by day)
		as visits
	where ((error*1.0/total)*100) > 1;
	'''

    # execute our Query
    cursor.execute(query)
    # retrieve the records from the database
    records = cursor.fetchall()

    print "\n" + "The days on which more than 1% of requests lead to errors:" + "\n"
    for row in records:
        print "    {} -- {}% errors \n".format(row[0], row[1])


# print the most popular three articles of all time
print_popular_articles()

# print the most popular article authors of all time
print_popular_authors()

# print days on which more than 1% of requests lead to errors
print_error_days()

