import logging
import boto3
from pathlib import Path

from scripts import downloader
from scripts import uploader

logging.basicConfig(level=logging.INFO, filename='logs.log', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def main():
    try:
        url = 'erfan4524/e-commerce-sales-data-analysis-and-eda'
        downloader.dataset_download(url=url)
        uploader.upload_file()
    except Exception as e:
        logger.error(f"Exception occurred at: {e}")
if __name__ == "__main__":
    main()