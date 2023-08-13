from textSummarization.pipeline.stage01_data_ingestion import DataIngestionTrainingPipeline

from textSummarization import logger,CustomException
import sys


STAGE_NAME_INGESTION = 'Data Ingestion Stage'

# try:
#     logger.info(f'\n\n{"**"*50}\nStarted {STAGE_NAME_INGESTION}\n{"**"*50}\n')
#     data_ingestion = DataIngestionTrainingPipeline()
#     data_ingestion.main()
#     logger.info(f'\n\n{"**"*50}\nCompleted {STAGE_NAME_INGESTION}\n{"**"*50}\n\n')
    
# except Exception as e:
#             logger.info(f"Error Occurred at {CustomException(e,sys)}")
#             raise CustomException(e, sys)
        
        
        
        
try:
        logger.info(f'\n\n{"**"*50}\nStarted {STAGE_NAME_INGESTION}\n{"**"*50}\n')
        data_ingestion = DataIngestionTrainingPipeline()
        data_ingestion.main()  # Call the main() function without passing arguments
        logger.info(f'\n\n{"**"*50}\nCompleted {STAGE_NAME_INGESTION}\n{"**"*50}\n\n')
    
except Exception as e:
    logger.info(f"Error Occurred at {CustomException(e, sys)}")
    raise CustomException(e, sys)
