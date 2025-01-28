# Importing libraries
import boto3
import os
from dotenv import load_dotenv

# Setting up the environment
load_dotenv()

# Setting up bedrock client
client = boto3.client(service_name = "bedrock-runtime",
                       region_name = "us-east-1",
                       aws_access_key_id = os.environ["aws_access_key_id"],
                       aws_secret_access_key = os.environ["aws_secret_access_key"])