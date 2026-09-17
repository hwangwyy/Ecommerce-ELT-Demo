import kagglehub
import logging
from pathlib import Path

logging.basicConfig(level=logging.INFO, filename='../logs.log')
logger = logging.getLogger(__name__)

def dataset_download(url, output_dir:str = './data/raw'):
    try:
        if not Path(output_dir).exists():
            logger.info(".data/raw not found. Creating new directory...")
            Path(output_dir).mkdir(parents=True)
        kagglehub.dataset_download(url, output_dir=output_dir)
        logger.info(f"Dataset downloaded at path: {output_dir}")
    except Exception as e:
        logger.error(f"Exception occurred: {e}")