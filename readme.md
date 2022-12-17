# Example Python Application

This is an example of a simple python / postgresql application directory that can perform many tasks.

It is meant to demonstrate proficiency in the following:
- Python syntax and semantics
- Object-oriented design patterns and concepts
- Design and implementation of relational databases
- Data transformation and manipulation
- Design and implementation of end-to-end data pipelines

The code and main app.py script can accomplish the following tasks:
- Install Postgresql from terminal
- Create 'stocks' db from terminal
- Create 'stocks' db schema (tables, stored procedures, etc... Raw SQL embedded in .py files)
- Create python virtual environment for project
- The app.py is a pipeline that:
    - Retrieves stock data from web apis
    - Cleans api responses
    - Writes api responses to 'stocks' db tables

**Important**
- To get the app to run
    - Must add a db.ini file to project directory specifying "host", "database", "username", "password"
- Must specify username and password to connect to postgres
- developed on mac OS


## Install homebrew
```
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

## How to set up PostgreSQL
```
brew install postgresql
psql -U {username} -W {password}
postgres
> CREATE DATABASE stocks;
```


## How to set up the virtual environment

```
python -m venv venv
source venv/bin/activate
python -m pip install -r requirements.txt
```

## How to create DB tables and objects
```
python db_configure.py
```


## How to run the app

From inside the main directory, run the following command:

```
python app.py
```
