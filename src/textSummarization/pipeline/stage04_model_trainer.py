from textSummarization.config.configuration import ConfigurationManager
from textSummarization.components.model_trainer import ModelTrainer
from textSummarization import logger, CustomException
import sys

class ModelTrainingPipeline:
    def __init__(self):
        pass
    
    def main(self):  # Notice the self parameter
        try:
            config = ConfigurationManager()
            model_trainer_config = config.get_model_trainer_config()
            model_trainer = ModelTrainer(config=model_trainer_config)
            model_trainer.train()
        except Exception as e:
            logger.info(f"Error Occurred at {CustomException(e, sys)}")
            raise CustomException(e, sys)









