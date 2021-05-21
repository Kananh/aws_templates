#!/usr/bin/env python3
"""
Python Version  : 3.7
* Name          : boilerplate.py
* Description   : Boilerplate python script
* Created       : 26-02-2021
* Usage         : python3 boilerplate.py
"""

__author__ = "Paul Fry"
__version__ = "0.1"

import os
import sys
from datetime import datetime
from time import time
import logging

#import custom modules
import boto3
import urllib.parse

working_dir = os.getcwd()
# Set up a specific logger with our desired output level
logging.basicConfig(format='%(message)s')
logger = logging.getLogger('application_logger')
logger.setLevel(logging.INFO)
# by default, turn off log outputs. But if desired, change this arg to True
#logger.propagate = False

current_dt_obj = datetime.now()
current_date_str = current_dt_obj.strftime('%d-%m-%Y')
current_time_str = current_dt_obj.strftime('%H:%M:%S')
#can use 'current_dt_obj' to get other date parts. E.g. 'current_dt_obj.year'

def main():
    """ Main entry point of the app """
    START_TIME = time()
    logger.debug(f"Function called: main()")
    
    #conn_type = 'YOUR_DB_OPTION'
    #host = 'YOUR_MWAA_AIRFLOW_UI_URL'
    #login = 'YOUR_AWS_ACCESS_KEY_ID'
    #password = 'YOUR_AWS_SECRET_ACCESS_KEY'
    #role_arn = urllib.parse.quote_plus('YOUR_EXECUTION_ROLE_ARN')
    #region_name = 'YOUR_REGION'

    conn_string = '{0}://{1}:{2}@{3}?role_arn={4}&region_name={5}'.format(conn_type, host, login, password, role_arn, region_name)
    print(conn_string)

    logger.debug(f"Function finished: main() finished in {round(time() - START_TIME, 2)} seconds")

    return

if __name__ == '__main__':
    """ This is executed when run from the command line """

    conn_type = sys.argv[1]
    airflow_ui_url = sys.argv[2]
    login = sys.argv[3]
    password = sys.argv[4]
    role_arn = sys.argv[5]
    region_name = sys.argv[6]
    aws_profile = sys.argv[7]

    print(f"conn_type = {conn_type}")
    print(f"airflow_ui_url = {airflow_ui_url}")
    print(f"login = {login}")
    print(f"password = {password}")
    print(f"role_arn = {role_arn}")
    print(f"region_name = {region_name}")

    #main()
