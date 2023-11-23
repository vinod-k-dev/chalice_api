from functools import wraps
from chalice import Chalice, CognitoUserPoolAuthorizer, NotFoundError, CORSConfig, Response
import boto3
from boto3.dynamodb.conditions import Key, Attr

import json
import uuid
import base64
from datetime import timedelta, date, datetime
import re
from botocore.exceptions import ClientError

app = Chalice(app_name='oxit_api')

dynamodb = boto3.resource('dynamodb')
app.debug = True
