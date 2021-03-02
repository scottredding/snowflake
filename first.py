#!/usr/bin/env python
import snowflake.connector
import os

PASSWORD = os.getenv('SNOWSQL_PWD')
USER = os.getenv('SFAZURE_USER')
ACCOUNT = 'sfpscogs_azure_ps_lab.east-us-2.azure'

conn = snowflake.connector.connect(
    user=USER,
    password=PASSWORD,
    account=ACCOUNT
    session_parameters={
        'QUERY_TAG': 'PYTHON_JOB_FIRST',
    }
)
