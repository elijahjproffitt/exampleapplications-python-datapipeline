#!/usr/bin/python
import psycopg2
from db_connect import config

def create_tables():
    """ 
    create tables in the PostgreSQL database
    
    Parameters
    ----------

    Returns
    -------
    """
    commands = (
        """
        CREATE TABLE company (
            symbol varchar(20) UNIQUE NOT NULL
            ,company varchar(100)
            ,sector varchar(50)
            ,industry varchar(100)
            ,headquarters varchar(100)
            ,PRIMARY KEY (symbol)
        );
        """,
    )
    conn = None
    try:
        # read the connection parameters
        params = config()
        # connect to the PostgreSQL server
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        # create table one by one
        for command in commands:
            cur.execute(command)
        # close communication with the PostgreSQL database server
        cur.close()
        # commit the changes
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

def create_procedures():
    """ 
    create procedures in the PostgreSQL database
    
    Parameters
    ----------

    Returns
    -------
    """
    commands = (
        """

        """,
    )
    conn = None
    try:
        # read the connection parameters
        params = config()
        # connect to the PostgreSQL server
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        # create table one by one
        for command in commands:
            cur.execute(command)
        # close communication with the PostgreSQL database server
        cur.close()
        # commit the changes
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


if __name__ == '__main__':
    create_tables()
