# Example Application - Python Data Pipeline

This is an example of an end-to-end data pipeline built with python, postgresql, and docker meant to demonstrate proficiency in the following:
- Python and SQL syntax and semantics
- Containerization via Docker
- Object-oriented design patterns and concepts
- Design and implementation of relational databases
- Design and implementation of end-to-end data pipelines
- Data transformation and manipulation

## App Setup and Instructions

### Important
- To get the app to run
    - Must add a db.ini file to project directory with section titled "postgresql" with items "host", "database", "username", "password"
    - Must specify username and password to connect to postgres
    - Must download Docker for Mac https://docs.docker.com/get-docker/
- developed on mac OS

### Summary
The code and main app.py script can accomplish the following tasks:
- Install Postgresql from terminal
- Create 'stocks' db from terminal
- Create 'stocks' db schema from terminal (tables, stored procedures, etc... Raw SQL embedded in .py files)
- Create python virtual environment for project
- The app.py is a pipeline that:
    - Retrieves stock data from web apis (1 implemented, but could be scaled to more)
    - Cleans api responses
    - Writes api responses to 'stocks' db tables
- Creata a docker image for app.py and run from the command line

### Install homebrew
```
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

### Install postgresql, connect and create a db
```
brew install postgresql
psql -U {username} -W {password}
postgres
> CREATE DATABASE stocks;
```

### Create virtual environment
```
python -m venv venv
source venv/bin/activate
python -m pip install -r requirements.txt
```

### Create db schema
Raw sql embedded in db_configure.py
```
python db_configure.py
```

### Run app.py
From inside the main directory, run the following command:
```
python app.py
```

### to build and run as a docker image
```
docker build -t companypipeline:latest .
docker run companypipeline
```
