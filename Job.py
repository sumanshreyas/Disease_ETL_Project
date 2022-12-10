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

DiabetesDataFrame = create_dagster_pandas_dataframe_type(
    name="DiabetesDataFrame",
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


@op(ins={'start': In(bool)}, out=Out(DiabetesDataFrame))
def extract_diabetes(start) -> DiabetesDataFrame:
    conn = MongoClient(mongo_connection_string)
    db = conn["test_database"]
    
    
    #db.diabetes.update_many({}, [{'$set': {'DataValue': {'$toInt': '$DataValue'}}}])
    diabetes = pd.DataFrame(db.diabetes.find({})).dropna(axis=0, how="any")
    #diabetes.dropna(),
    #diabetes.dropna(axis=0),

    conn.close()
    return diabetes

@op(ins={'diabetes': In(DiabetesDataFrame)}, out=Out(None))
def stage_extracted_diabetes(diabetes):
    diabetes.to_csv("staging/diabetes.csv",index=False,sep=",")
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
def load_diabetes(start):
    #logger = get_dagster_logger()
    #diabetes = pd.read_csv("staging/diabetes.csv", sep= ",")
    
    
    con = psycopg2.connect(dbname='Disease', host='localhost', user='dap', password='dap', port=5432)
    cur = con.cursor()
    
    with open('staging/diabetes.csv') as csv_file:
        cur.copy_expert('COPY diabetes FROM STDIN WITH CSV HEADER', csv_file)
        con.commit()
       
    #try:
     #  engine = create_engine(postgres_connection_string,poolclass=NullPool)
        #engine.execute("TRUNCATE diabetes;")
      #  rowcount = diabetes.to_sql(
       #     name="diabetes",
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
def load_dimensions(diabetes):
    return diabetes

@job
def etl():
    load_dimensions(
        diabetes =load_diabetes(
            stage_extracted_diabetes(
                extract_diabetes()
                )
            )
        )
   
      