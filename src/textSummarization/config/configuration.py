from textSummarization.constants import *
from textSummarization.utils.common import read_yaml, create_directories
from textSummarization.entity import (
    DataIngestionConfig, DataValidationConfig)
from textSummarization import logger, CustomException
import sys


class ConfigurationManager:

    def __init__(
            self,
            config_path=CONFIG_FILE_PATH,
            params_file_path=PARAMS_FILE_PATH):
        self.config = read_yaml(config_path)
        self.params = read_yaml(params_file_path)

        create_directories([self.config.artifacts_root])

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        try:
            config = self.config.data_ingestion

            create_directories([config.root_dir])

            data_ingestion_config = DataIngestionConfig(
                root_dir=config.root_dir,
                source_url=config.source_url,
                local_data_file=config.local_data_file,
                unzip_dir=config.unzip_dir
            )

            return data_ingestion_config

        except Exception as e:
            logger.info(f"Error Occurred at {CustomException(e,sys)}")
            raise CustomException(e, sys)

    def get_data_validation_config(self) -> DataValidationConfig:
        config = self.config.data_validation
        print(config)
        create_directories([config.root_dir])

        data_validation_config = DataValidationConfig(
            root_dir=config.root_dir,
            STATUS_FILE=config.STATUS_FILE,
            ALL_REQUIRED_FILES=config.ALL_REQUIRED_FILES
        )

        return data_validation_config