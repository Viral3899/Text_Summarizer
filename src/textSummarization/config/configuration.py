from textSummarization.constants import *
from textSummarization.utils.common import read_yaml, create_directories
from textSummarization.entity import (DataIngestionConfig)
from textSummarization import logger,CustomException


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
        except Exception as e:
            logger.info(f"Error Occurred at {CustomException(e,sys)}")
            raise CustomException(e, sys)
        
        return data_ingestion_config
