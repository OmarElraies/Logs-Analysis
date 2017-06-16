# Logs Analysis Project

This Project is part of the Udacity Fullstack Nanodegree curriculum which focus on analyzing data from a web service's logs with practicing command-line and database skills and particularly with a focus on building advanced SQL queries.

## Project Overview
>In this project, you'll work with data that could have come from a real-world web application, with fields representing information that a web server would record, such as HTTP status codes and URL paths. The web server and the reporting tool both connect to the same database, allowing information to flow from the web server into the report.

## Project Summary
A reporting tool that will use information from the database to discover what kind of articles the site's readers like.

## Requirements

  * [Python3](https://www.python.org/)

  * [Vagrant](https://www.vagrantup.com/)

  * [VirtualBox](https://www.virtualbox.org/)


## Usage

  * Download or Clone [fullstack-nanodegree-vm](https://github.com/udacity/fullstack-nanodegree-vm) repository.

  * Download or Clone [Logs-Analysis](https://github.com/OmarElraies/Logs-Analysis) repository.

  * Unzip this file after downloading it put the `reporting_tool.py` file and `newsdata.sql` file in vagrant diretory

  * Launch the Vagrant VM inside the fullstack-nanodegree-vm repository using command:
  ```
    $ vagrant up
  ```

  * Log into this using command:
  ```
    $ vargrant ssh
  ```

  * Change directory to /vagrant
  
  * Load the data and connect to database using command:
  ```
    $ psql -d news -f newsdata.sql
  ```

## Running
  *  Run `python reporting_tool.py`

## Output

  ```
  The most popular three articles of all time:

	"Candidate is jerk, alleges rival" -- 338647 views
	"Bears love berries, alleges bear" -- 253801 views
	"Bad things gone, say good people" -- 170098 views

  The most popular three authors of all time:
  
	Ursula La Multa -- 507594 views
	Rudolf von Treppenwitz -- 423457 views
	Anonymous Contributor -- 170098 views
	Markoff Chaney -- 84557 views

  The days on which more than 1% of requests lead to errors:

	2016-07-17 -- 2.3% errors

  ```
