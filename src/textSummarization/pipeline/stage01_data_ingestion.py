from textSummarization.config.configuration import ConfigurationManager
from textSummarization.components.data_ingestion import DataIngestion
from textSummarization import logger, CustomException
import sys

class DataIngestionTrainingPipeline:
    def __init__(self):
        pass
    
    def main(self):  # Notice the self parameter
        try:
            config = ConfigurationManager()
            data_ingestion_config = config.get_data_ingestion_config()
            data_ingestion = DataIngestion(config=data_ingestion_config)
            data_ingestion.download_data_files()
            data_ingestion.extract_zip_file()
        except Exception as e:
            logger.info(f"Error Occurred at {CustomException(e, sys)}")
            raise CustomException(e, sys)

# if __name__ == "__main__":
#     try:
#         logger.info(f'\n\n{"**"*50}\nStarted {STAGE_NAME_INGESTION}\n{"**"*50}\n')
#         data_ingestion = DataIngestionTrainingPipeline()
#         data_ingestion.main()  # Call the main() function without passing arguments
#         logger.info(f'\n\n{"**"*50}\nCompleted {STAGE_NAME_INGESTION}\n{"**"*50}\n\n')
    
#     except Exception as e:
#         logger.info(f"Error Occurred at {CustomException(e, sys)}")
#         raise CustomException(e, sys)







