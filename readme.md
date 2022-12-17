# Get Stock Data

This is a python application that does the following:
- Installs Postgresql
- Creates 'stocks' db, creates db objects in db_configure.py
- Gets stock data from different apis
- Cleans and transforms the api responses
- Writes cleaned data to postgres

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
