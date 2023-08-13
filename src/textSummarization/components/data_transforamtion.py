from textSummarization import logger,CustomException
from datasets import load_dataset,load_from_disk
import os,sys
from transformers import AutoTokenizer
from textSummarization.config.configuration import DataTransformationConfig




class DataTransformation:
    def __init__(self,config:DataTransformationConfig):
        self.config = config
        self.tokenizer = AutoTokenizer.from_pretrained(self.config.tokenizer_name)
        
    
    
    def convert_examples_to_features(self,example_batch):
        try:
            input_encodings = self.tokenizer(example_batch['dialogue'] , max_length = 1024, truncation = True )


            with self.tokenizer.as_target_tokenizer():
                target_encodings  = self.tokenizer(example_batch['summary'],max_length=1024,truncation=True )

            return {
                'input_ids' : input_encodings['input_ids'],
                'attention_mask': input_encodings['attention_mask'],
                'labels': target_encodings['input_ids']
            }
        except Exception as e:
                    logger.info(f"Error Occurred at {CustomException(e,sys)}")
                    raise CustomException(e, sys)
                
    def convert(self):
        try:
            dataset_samsum = load_from_disk(self.config.data_path)
            dataset_samsum_pt= dataset_samsum.map(self.convert_examples_to_features,batched=True)
            dataset_samsum_pt.save_to_disk(os.path.join(self.config.root_dir, "dataset_samsum"))
        except Exception as e:
                    logger.info(f"Error Occurred at {CustomException(e,sys)}")
                    raise CustomException(e, sys)