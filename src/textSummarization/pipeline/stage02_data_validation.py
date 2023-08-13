from textSummarization.config.configuration import ConfigurationManager
from textSummarization.components.data_validation import DataValidation
from textSummarization import logger, CustomException
import sys

class DataValidationTrainingPipeline:
    def __init__(self):
        pass
    
    def main(self):  # Notice the self parameter
        try:
            config = ConfigurationManager()
            data_validation_config = config.get_data_validation_config()
            data_validation = DataValidation(config=data_validation_config)
            data_validation.validate_All_file_exists()
        except Exception as e:
            logger.info(f"Error Occurred at {CustomException(e, sys)}")
            raise CustomException(e, sys)









