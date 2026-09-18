from botocore.exceptions import ClientError
from pathlib import Path
from dotenv import load_dotenv
import boto3
import logging
import os

load_dotenv()

logging.basicConfig(level=logging.INFO, filename='./logs.log', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def upload_file():
    data_path = Path('./data/raw')
    bucket = os.getenv('S3_BUCKET')
    s3_client = boto3.client(
        's3',
        aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
        aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'),
    )
    try:
        for csv in data_path.iterdir():
            if csv.suffix.lower() == '.csv' and not csv.name == 'clean_final_data.csv':
                logger.info(f"CSV found. Filename {csv}. Start uploading...")
                s3_client.upload_file(csv, bucket, f'csv/{csv.name}')
                logger.info("File uploaded")
    except ClientError as e:
        logger.error(f"Upload failed: {e}")