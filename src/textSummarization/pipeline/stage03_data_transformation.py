from textSummarization.config.configuration import ConfigurationManager
from textSummarization.components.data_transforamtion import DataTransformation
from textSummarization import logger, CustomException
import sys

class DataTransformationTrainingPipeline:
    def __init__(self):
        pass
    
    def main(self):  # Notice the self parameter
        try:
            config = ConfigurationManager()
            data_transformation_config = config.get_data_transformation_config()
            data_transformation = DataTransformation(config=data_transformation_config)
            data_transformation.convert()
        except Exception as e:
            logger.info(f"Error Occurred at {CustomException(e, sys)}")
            raise CustomException(e, sys)









