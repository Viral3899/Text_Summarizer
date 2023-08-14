from textSummarization.config.configuration import ConfigurationManager
from transformers import AutoTokenizer
from transformers import pipeline
from textSummarization import logger, CustomException
import sys


class PredictionPipeline:
    def __init__(self):
        self.config = ConfigurationManager().get_model_evaluation_config()


    
    def predict(self,text):
        try:
            tokenizer = AutoTokenizer.from_pretrained(self.config.tokenizer_path)
            gen_kwargs = {"length_penalty": 0.8, "num_beams":8, "max_length": 128}
            tokenizer = AutoTokenizer.from_pretrained(self.config.tokenizer_path)
            gen_kwargs = {"length_penalty": 0.8, "num_beams":8, "max_length": 128}

            pipe = pipeline("summarization", model=self.config.model_path,tokenizer=tokenizer)

            print("Dialogue:")
            print(text)

            output = pipe(text, **gen_kwargs)[0]["summary_text"]
            print("\nModel Summary:")
            print(output)

            return output
        except Exception as e:
                logger.info(f"Error Occurred at {CustomException(e,sys)}")
                raise CustomException(e, sys)