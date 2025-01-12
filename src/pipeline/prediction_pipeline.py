import sys
import os
import pandas as pd
from src.logger import logging
from src.exception import CustomException
from src.utils import load_object

class PredictPipeline:
    def __init__(self):
        pass
    
    def predict(self, features):
        try:
            preprocessor_path = os.path.join('artifacts','preprocesssor.pkl')
            model_path = os.path.join('artifacts','model.pkl')
            
            preprocessor = load_object(preprocessor_path)
            model=load_object(model_path)
            
            data_scale=preprocessor.transform(features)
            pred = model.predict(data_scale)
            return pred
                    
        except Exception as e:
            logging.info("Exception occured in prediction")
            raise CustomException(e,sys)
        
class CustomData:
    def __init__(self,
                 carat:float,
                 depth:float,
                 table:float,
                 cut:str,
                 color:str,
                 clarity:str):
        
        self.carat = carat
        self.depth = depth
        self.table = table
        self.cut = cut
        self.color = color
        self.clarity = clarity
        
    def get_data_as_dataframe(self):
        try:
            custom_data_input_dict = {
                'carat':[self.carat],
                'depth':[self.depth],
                'table':[self.table],
                'cut':[self.cut],
                'color':[self.color],
                'clarity':[self.clarity]
            }
            df = pd.DataFrame(custom_data_input_dict)
            logging.info('DataFrame Gathered')
            return df
            
        except Exception as e:
            logging.info('Exception Occured in Prediction Pipeline')
            raise CustomException(e,sys)