from textSummarization.config.configuration import ConfigurationManager
from textSummarization.components.model_evaluation import ModelEvaluation
from textSummarization import logger
from textSummarization import logger, CustomException
import sys


class ModelEvaluationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            config = ConfigurationManager()
            model_evaluation_config = config.get_model_evaluation_config()
            model_evaluation_config = ModelEvaluation(config=model_evaluation_config)
            model_evaluation_config.evaluate()
        except Exception as e:
                logger.info(f"Error Occurred at {CustomException(e,sys)}")
                raise CustomException(e, sys)