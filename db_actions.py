import pandas
import finsymbols
import regex
import psycopg2
from db_connect import config

def insert_something(sql):
    conn = None
    id = None
    try:
        # read database configuration
        params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # create a new cursor
        cur = conn.cursor()
        # execute the INSERT statement
        cur.execute(sql)
        # get the generated id back
        # id = cur.fetchone()[0]
        # commit the changes to the database
        conn.commit()
        # close communication with the database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

def write_company(data):
    """
    - takes a pandas df of s&p 500 data
    - cleans the data
    - writes it to postgres

    Parameters
    ----------
    - pandas df of s&p 500 data

    Returns
    -------

    """
    # clean the data
    data['symbol'].replace('\s+|\\n', '', regex=True, inplace=True)
    data['company'].replace("'", '"', regex=True, inplace=True)
    data = data.reset_index()

    # upsert the company relation
    for index, row in data.iterrows():
        sql = f'''
        INSERT INTO company 
            (symbol, company, sector, industry, headquarters) 
        VALUES ('{row[1]}', '{row[2]}', '{row[3]}', '{row[4]}', '{row[5]}') 
        ON CONFLICT (symbol) DO NOTHING;
        '''
        insert_something(sql)
    
    # return symbols
    print(data['symbol'])
    return(data['symbol'])

