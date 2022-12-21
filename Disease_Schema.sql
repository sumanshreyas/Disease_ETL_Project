-- Table: public.asthma

-- DROP TABLE IF EXISTS public.asthma;

CREATE TABLE IF NOT EXISTS public.asthma
(
    _id character varying(200) COLLATE pg_catalog."default",
    yearstart integer,
    yearend integer,
    locationabbr character varying(200) COLLATE pg_catalog."default",
    locationdesc character varying(200) COLLATE pg_catalog."default",
    datasource character varying(200) COLLATE pg_catalog."default",
    topic character varying(200) COLLATE pg_catalog."default",
    question character varying(200) COLLATE pg_catalog."default",
    response character varying(200) COLLATE pg_catalog."default",
    datavalueunit character varying(200) COLLATE pg_catalog."default",
    datavaluetype character varying(200) COLLATE pg_catalog."default",
    datavalue double precision,
    datavaluealt double precision,
    datavaluefootnotesymbol character varying(200) COLLATE pg_catalog."default",
    datavaluefootnote character varying(200) COLLATE pg_catalog."default",
    lowconfidencelimit double precision,
    highconfidencelimit double precision,
    stratificationcategory1 character varying(200) COLLATE pg_catalog."default",
    stratification1 character varying(200) COLLATE pg_catalog."default",
    stratificationcategory2 character varying(200) COLLATE pg_catalog."default",
    stratification2 character varying(200) COLLATE pg_catalog."default",
    stratificationcategory3 character varying(200) COLLATE pg_catalog."default",
    stratification3 character varying(200) COLLATE pg_catalog."default",
    responseid character varying(200) COLLATE pg_catalog."default",
    locationid character varying(200) COLLATE pg_catalog."default",
    topicid character varying(200) COLLATE pg_catalog."default",
    questionid character varying(200) COLLATE pg_catalog."default",
    datavaluetypeid character varying(200) COLLATE pg_catalog."default",
    stratificationcategoryid1 character varying(200) COLLATE pg_catalog."default",
    stratificationid1 character varying(200) COLLATE pg_catalog."default",
    stratificationcategoryid2 character varying(200) COLLATE pg_catalog."default",
    stratificationid2 character varying(200) COLLATE pg_catalog."default",
    stratificationcategoryid3 character varying(200) COLLATE pg_catalog."default",
    stratificationid3 character varying(200) COLLATE pg_catalog."default"
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.asthma
    OWNER to dap;

-- Table: public.diabetes

-- DROP TABLE IF EXISTS public.diabetes;

CREATE TABLE IF NOT EXISTS public.diabetes
(
    _id character varying(200) COLLATE pg_catalog."default",
    yearstart integer,
    yearend integer,
    locationabbr character varying(200) COLLATE pg_catalog."default",
    locationdesc character varying(200) COLLATE pg_catalog."default",
    datasource character varying(200) COLLATE pg_catalog."default",
    topic character varying(200) COLLATE pg_catalog."default",
    question character varying(200) COLLATE pg_catalog."default",
    response character varying(200) COLLATE pg_catalog."default",
    datavalueunit character varying(200) COLLATE pg_catalog."default",
    datavaluetype character varying(200) COLLATE pg_catalog."default",
    datavalue double precision,
    datavaluealt double precision,
    datavaluefootnotesymbol character varying(200) COLLATE pg_catalog."default",
    datavaluefootnote character varying(200) COLLATE pg_catalog."default",
    lowconfidencelimit double precision,
    highconfidencelimit double precision,
    stratificationcategory1 character varying(200) COLLATE pg_catalog."default",
    stratification1 character varying(200) COLLATE pg_catalog."default",
    stratificationcategory2 character varying(200) COLLATE pg_catalog."default",
    stratification2 character varying(200) COLLATE pg_catalog."default",
    stratificationcategory3 character varying(200) COLLATE pg_catalog."default",
    stratification3 character varying(200) COLLATE pg_catalog."default",
    responseid character varying(200) COLLATE pg_catalog."default",
    locationid character varying(200) COLLATE pg_catalog."default",
    topicid character varying(200) COLLATE pg_catalog."default",
    questionid character varying(200) COLLATE pg_catalog."default",
    datavaluetypeid character varying(200) COLLATE pg_catalog."default",
    stratificationcategoryid1 character varying(200) COLLATE pg_catalog."default",
    stratificationid1 character varying(200) COLLATE pg_catalog."default",
    stratificationcategoryid2 character varying(200) COLLATE pg_catalog."default",
    stratificationid2 character varying(200) COLLATE pg_catalog."default",
    stratificationcategoryid3 character varying(200) COLLATE pg_catalog."default",
    stratificationid3 character varying(200) COLLATE pg_catalog."default"
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.diabetes
    OWNER to dap;

-- Table: public.mental

-- DROP TABLE IF EXISTS public.mental;

CREATE TABLE IF NOT EXISTS public.mental
(
    _id character varying(200) COLLATE pg_catalog."default",
    yearstart integer,
    yearend integer,
    locationabbr character varying(200) COLLATE pg_catalog."default",
    locationdesc character varying(200) COLLATE pg_catalog."default",
    datasource character varying(200) COLLATE pg_catalog."default",
    topic character varying(200) COLLATE pg_catalog."default",
    question character varying(200) COLLATE pg_catalog."default",
    response character varying(200) COLLATE pg_catalog."default",
    datavalueunit character varying(200) COLLATE pg_catalog."default",
    datavaluetype character varying(200) COLLATE pg_catalog."default",
    datavalue double precision,
    datavaluealt double precision,
    datavaluefootnotesymbol character varying(200) COLLATE pg_catalog."default",
    datavaluefootnote character varying(200) COLLATE pg_catalog."default",
    lowconfidencelimit double precision,
    highconfidencelimit double precision,
    stratificationcategory1 character varying(200) COLLATE pg_catalog."default",
    stratification1 character varying(200) COLLATE pg_catalog."default",
    stratificationcategory2 character varying(200) COLLATE pg_catalog."default",
    stratification2 character varying(200) COLLATE pg_catalog."default",
    stratificationcategory3 character varying(200) COLLATE pg_catalog."default",
    stratification3 character varying(200) COLLATE pg_catalog."default",
    responseid character varying(200) COLLATE pg_catalog."default",
    locationid character varying(200) COLLATE pg_catalog."default",
    topicid character varying(200) COLLATE pg_catalog."default",
    questionid character varying(200) COLLATE pg_catalog."default",
    datavaluetypeid character varying(200) COLLATE pg_catalog."default",
    stratificationcategoryid1 character varying(200) COLLATE pg_catalog."default",
    stratificationid1 character varying(200) COLLATE pg_catalog."default",
    stratificationcategoryid2 character varying(200) COLLATE pg_catalog."default",
    stratificationid2 character varying(200) COLLATE pg_catalog."default",
    stratificationcategoryid3 character varying(200) COLLATE pg_catalog."default",
    stratificationid3 character varying(200) COLLATE pg_catalog."default"
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.mental
    OWNER to dap;

SELECT distinct LocationID, LocationAbbr, LocationDesc
INTO Location
FROM disease
order by locationID asc



SELECT distinct ResponseID, Response
INTO Response
FROM disease
order by ResponseID asc



SELECT distinct DataValueTypeID, DataValueType
INTO DataValueType
FROM disease
order by DataValueTypeID asc



SELECT distinct StratificationCategoryID1, StratificationCategory1
INTO StratificationCategory1
FROM disease
order by StratificationCategoryID1 asc



SELECT distinct StratificationCategoryID2, StratificationCategory2
INTO StratificationCategory2
FROM disease
order by StratificationCategoryID2 asc



SELECT distinct StratificationCategoryID3, StratificationCategory3
INTO StratificationCategory3
FROM disease
order by StratificationCategoryID3 asc



SELECT distinct StratificationID1, Stratification1
INTO Stratification1
FROM disease
order by StratificationID1 asc



SELECT distinct StratificationID2, Stratification2
INTO Stratification2
FROM disease
order by StratificationID2 asc




SELECT distinct StratificationID3, Stratification3
INTO Stratification3
FROM disease
order by StratificationID3 asc



SELECT distinct TopicID, Topic
INTO Topic
FROM disease
order by TopicID asc



SELECT distinct QuestionID, Question
INTO Question
FROM disease
order by QuestionID asc
