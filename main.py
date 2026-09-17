import logging

from scripts import downloader

logging.basicConfig(level=logging.INFO, filename='logs.log')
logger = logging.getLogger(__name__)

def main():
    try:
        url = 'erfan4524/e-commerce-sales-data-analysis-and-eda'
        downloader.dataset_download(url=url)
    except Exception as e:
        logger.error(f"Exception occurred at: {e}")
if __name__ == "__main__":
    main()