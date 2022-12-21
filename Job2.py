# -*- coding: utf-8 -*-
"""
Created on Sat Dec 10 16:21:32 2022

@author: Suman
"""

import webbrowser
from dagster import job
from extract import *
from transform import *
from load import *
from collections.abc import Mapping
from dagster import op, Out, In, get_dagster_logger

from pymongo import MongoClient
from dagster import op, Out, In, DagsterType
from dagster_pandas import PandasColumn, create_dagster_pandas_dataframe_type
from datetime import datetime
import pandas as pd

mongo_connection_string = "mongodb://dap:dap@127.0.0.1"

mentalDataFrame = create_dagster_pandas_dataframe_type(
    name="mentalDataFrame",
    columns=[
        PandasColumn.string_column("_id" ),
        PandasColumn.integer_column("YearStart",is_required= False ),
        PandasColumn.integer_column("YearEnd"  ),
        PandasColumn.string_column("LocationAbbr"  ),
        PandasColumn.string_column("LocationDesc"  ),
        PandasColumn.string_column("DataSource"  ),
        PandasColumn.string_column("Topic"  ),
        PandasColumn.string_column("Question"  ),
        PandasColumn.string_column("Response"  ),
        PandasColumn.string_column("Response"  ),
        PandasColumn.string_column("DataValueUnit"  ),
        PandasColumn.string_column("DataValueType"  ),
        PandasColumn.float_column("DataValue",is_required= False ),
        PandasColumn.float_column("DataValueAlt"  ),
        PandasColumn.string_column("DataValueFootnoteSymbol"  ),
        PandasColumn.string_column("DatavalueFootnote"  ),
        PandasColumn.float_column("LowConfidenceLimit" ),
        PandasColumn.float_column("HighConfidenceLimit"  ),
        PandasColumn.string_column("StratificationCategory1"  ),
        PandasColumn.string_column("Stratification1"  ),
        PandasColumn.string_column("StratificationCategory2"  ),
        PandasColumn.string_column("Stratification2"  ),
        PandasColumn.string_column("StratificationCategory3"  ),
        PandasColumn.string_column("Stratification3"  ),
        PandasColumn.string_column("ResponseID"  ),
        PandasColumn.integer_column("LocationID"  ),
        PandasColumn.string_column("TopicID"  ),
        PandasColumn.string_column("QuestionID"  ),
        PandasColumn.string_column("DataValueTypeID"  ),
        PandasColumn.string_column("StratificationCategoryID1"  ),
        PandasColumn.string_column("StratificationID1"  ),
        PandasColumn.string_column("StratificationCategoryID2"  ),
        PandasColumn.string_column("StratificationID2"  ),
        PandasColumn.string_column("StratificationCategoryID3"  ),
        PandasColumn.string_column("StratificationID3"  )
        
    ],
)


@op(ins={'start': In(bool)}, out=Out(mentalDataFrame))
def extract_mental(start) -> mentalDataFrame:
    conn = MongoClient(mongo_connection_string)
    db = conn["test_database"]
    
    
    #db.mental.update_many({}, [{'$set': {'DataValue': {'$toInt': '$DataValue'}}}])
    mental = pd.DataFrame(db.mental.find({})).dropna(axis=0, how="any")
    #mental.dropna(),
    #mental.dropna(axis=0),

    conn.close()
    return mental

@op(ins={'mental': In(mentalDataFrame)}, out=Out(None))
def stage_extracted_mental(mental):
    mental.to_csv("staging/mental.csv",index=False,sep=",")
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  9 11:56:27 2022

@author: Suman
"""

from dagster import op, Out, In, get_dagster_logger
from sqlalchemy import create_engine, exc
from sqlalchemy.pool import NullPool
import pandas as pd
import psycopg2
    

postgres_connection_string = "postgresql://dap:dap@127.0.0.1:5432/Disease"

@op(ins={'start': In(None)},out=Out(bool))
def load_mental(start):
    #logger = get_dagster_logger()
    #mental = pd.read_csv("staging/mental.csv", sep= ",")
    
    
    con = psycopg2.connect(dbname='Disease', host='localhost', user='dap', password='dap', port=5432)
    cur = con.cursor()
    
    with open('staging/mental.csv') as csv_file:
        cur.copy_expert('COPY mental FROM STDIN WITH CSV HEADER', csv_file)
        con.commit()
       
    #try:
     #  engine = create_engine(postgres_connection_string,poolclass=NullPool)
        #engine.execute("TRUNCATE mental;")
      #  rowcount = mental.to_sql(
       #     name="mental",
        #    schema="public",
         #   con=engine,
          #  index=False,
           # if_exists="append"
        #)
#        logger.info("%i records loaded" % rowcount)
 #       engine.dispose(close=True)
  #      return rowcount > 0
   # except exc.SQLAlchemyError as error:
    #    logger.error("Error: %s" % error)
        return True

        
@op(out=Out(bool))
def load_dimensions(mental):
    return mental

@job
def etl():
    load_dimensions(
        mental =load_mental(
            stage_extracted_mental(
                extract_mental()
                )
            )
        )
   
      