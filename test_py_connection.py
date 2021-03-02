#!/usr/bin/env python
import snowflake.connector
import os

PASSWORD = os.getenv('SNOWSQL_PWD')
USER = os.getenv('SFAZURE_USER')
ACCOUNT = 'sfpscogs_azure_ps_lab.east-us-2.azure'

# Gets the version
ctx = snowflake.connector.connect(
    user=USER,
    password=PASSWORD,
    account=ACCOUNT,
    session_parameters={
        'QUERY_TAG': 'PYTHON_JOB_FIRST'
    }
)
cs = ctx.cursor()
try:
    cs.execute("SELECT current_version()")
    one_row = cs.fetchone()
    print(one_row[0])
finally:
    cs.close()
ctx.close()
