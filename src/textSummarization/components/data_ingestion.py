import requests
import sys
import os
import zipfile
from textSummarization import logger, CustomException
from textSummarization.utils.common import get_size
from textSummarization.entity import DataIngestionConfig
from pathlib import Path

from textSummarization.utils.common import * 



class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def download_data_files(self):
        try:
            if not os.path.exists(self.config.local_data_file):
                response = requests.get(self.config.source_url)
                if response.status_code == 200:
                    with open(self.config.local_data_file, 'wb') as file:
                        file.write(response.content)
                    logger.info(
                        f"Downloaded data to {self.config.local_data_file} with size of {get_size(Path(self.config.local_data_file))}")
                else:
                    logger.error(
                        f"Failed to download data. HTTP status code: {response.status_code}")
            else:
                logger.info(
                    f"Data file already exists at {self.config.local_data_file} with size of {get_size(Path(self.config.local_data_file))}")
        except Exception as e:
            logger.info(f"Error Occurred at {CustomException(e,sys)}")
            raise CustomException(e, sys)

    def extract_zip_file(self):
        try:
            unzip_dir = self.config.unzip_dir
            os.makedirs(unzip_dir, exist_ok=True)
            with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
                zip_ref.extractall(unzip_dir)
        except Exception as e:
            logger.info(f"Error Occurred at {CustomException(e,sys)}")
            raise CustomException(e, sys)
