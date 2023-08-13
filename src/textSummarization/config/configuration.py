from textSummarization.constants import *
from textSummarization.utils.common import read_yaml, create_directories
from textSummarization.entity import (
    DataIngestionConfig, DataValidationConfig, DataTransformationConfig, ModelTrainerConfig, ModelEvaluationConfig)
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
        try:
            config = self.config.data_validation
            print(config)
            create_directories([config.root_dir])

            data_validation_config = DataValidationConfig(
                root_dir=config.root_dir,
                STATUS_FILE=config.STATUS_FILE,
                ALL_REQUIRED_FILES=config.ALL_REQUIRED_FILES
            )

            return data_validation_config
        except Exception as e:
            logger.info(f"Error Occurred at {CustomException(e,sys)}")
            raise CustomException(e, sys)

    def get_data_transformation_config(self) -> DataTransformationConfig:
        try:
            config = self.config.data_transformation
            print(config)
            create_directories([config.root_dir])

            data_transformation_config = DataTransformationConfig(
                root_dir=config.root_dir,
                data_path=config.data_path,
                tokenizer_name=config.tokenizer_name,
            )

            return data_transformation_config
        except Exception as e:
            logger.info(f"Error Occurred at {CustomException(e,sys)}")
            raise CustomException(e, sys)

    def get_model_trainer_config(self) -> ModelTrainerConfig:
        try:
            config = self.config.model_trainer
            params = self.params.TrainingArguments
            create_directories([config.root_dir])

            model_trainer_config = ModelTrainerConfig(
                root_dir=config.root_dir,
                data_path=config.data_path,
                model_ckpt=config.model_ckpt,
                num_train_epochs=params.num_train_epochs,
                per_device_train_batch_size=params.per_device_train_batch_size,
                gradient_accumulation_steps=params.gradient_accumulation_steps,
                warmup_steps=params.warmup_steps,
                logging_steps=params.logging_steps,
                eval_steps=params.eval_steps,
                evaluation_strategy=params.evaluation_strategy,
                save_steps=params.save_steps,
                weight_decay=params.weight_decay
            )

            return model_trainer_config
        except Exception as e:
            logger.info(f"Error Occurred at {CustomException(e,sys)}")
            raise CustomException(e, sys)

    def get_model_evaluation_config(self) -> ModelEvaluationConfig:
        try:
            config = self.config.model_trainer
            create_directories([config.root_dir])

            model_evaluation_config = ModelEvaluationConfig(
                root_dir=config.root_dir,
                data_path=config.data_path,
                model_path=config.model_path,
                metric_file_name=config.metric_file_name,
                tokenizer_path=config.tokenizer_path
            )

            return model_evaluation_config
        except Exception as e:
            logger.info(f"Error Occurred at {CustomException(e,sys)}")
            raise CustomException(e, sys)
