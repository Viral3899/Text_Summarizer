import os
import sys
from textSummarization import logger, CustomException
from textSummarization.utils.common import * 
from textSummarization.entity import DataValidationConfig



class DataValidation:
    def __init__(self, config: DataValidationConfig):
        self.config = config
        
    def validate_All_file_exists(self)->bool:
        
        try:
            validation_status = None
            
            all_files_required = os.listdir(os.path.join('artifacts','data_ingestion','samsum_dataset'))
            
            for file in all_files_required:
                if file not in self.config.ALL_REQUIRED_FILES:
                    validation_status = False
                    with open(self.config.STATUS_FILE,'w+') as f:
                        f.write(f"validation status at {get_current_time_stamp} is {validation_status}")
                else:
                    validation_status = True
                    with open(self.config.STATUS_FILE,'w+') as f:
                        f.write(f"validation status at {get_current_time_stamp()} is {validation_status}")
            return validation_status
        
        except Exception as e:
            logger.info(f"Error Occurred at {CustomException(e,sys)}")
            raise CustomException(e, sys)