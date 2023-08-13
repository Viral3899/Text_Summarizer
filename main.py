from textSummarization.pipeline.stage01_data_ingestion import DataIngestionTrainingPipeline

from textSummarization.pipeline.stage02_data_validation import DataValidationTrainingPipeline
from textSummarization.pipeline.stage03_data_transformation import DataTransformationTrainingPipeline
from textSummarization.pipeline.stage04_model_trainer import ModelTrainingPipeline



from textSummarization import logger,CustomException
import sys


STAGE_NAME = 'Data Ingestion Stage'

try:
        logger.info(f'\n\n{"**"*50}\nStarted {STAGE_NAME}\n{"**"*50}\n')
        data_ingestion = DataIngestionTrainingPipeline()
        data_ingestion.main()  # Call the main() function without passing arguments
        logger.info(f'\n\n{"**"*50}\nCompleted {STAGE_NAME}\n{"**"*50}\n\n')
    
except Exception as e:
    logger.info(f"Error Occurred at {CustomException(e, sys)}")
    raise CustomException(e, sys)



STAGE_NAME = 'Data Validation Stage'

try:
        logger.info(f'\n\n{"**"*50}\nStarted {STAGE_NAME}\n{"**"*50}\n')
        data_validation = DataValidationTrainingPipeline()
        data_validation.main()  # Call the main() function without passing arguments
        logger.info(f'\n\n{"**"*50}\nCompleted {STAGE_NAME}\n{"**"*50}\n\n')
    
except Exception as e:
    logger.info(f"Error Occurred at {CustomException(e, sys)}")
    raise CustomException(e, sys)


STAGE_NAME= 'Data Transformation Stage'

try:
        logger.info(f'\n\n{"**"*50}\nStarted {STAGE_NAME}\n{"**"*50}\n')
        data_transformation = DataTransformationTrainingPipeline()
        data_transformation.main()  # Call the main() function without passing arguments
        logger.info(f'\n\n{"**"*50}\nCompleted {STAGE_NAME}\n{"**"*50}\n\n')
    
except Exception as e:
    logger.info(f"Error Occurred at {CustomException(e, sys)}")
    raise CustomException(e, sys)


STAGE_NAME= 'Model Trainer Stage'

try:
        logger.info(f'\n\n{"**"*50}\nStarted {STAGE_NAME}\n{"**"*50}\n')
        data_transformation = ModelTrainingPipeline()
        data_transformation.main()  # Call the main() function without passing arguments
        logger.info(f'\n\n{"**"*50}\nCompleted {STAGE_NAME}\n{"**"*50}\n\n')
    
except Exception as e:
    logger.info(f"Error Occurred at {CustomException(e, sys)}")
    raise CustomException(e, sys)
