from housing.pipeline.pipeline import Pipeline
from housing.exception import HousingException
import logging

def main():
    try:
        pipeline= Pipeline()
        pipeline.run_pipeline()
    except Exception as e:
        logging.error(e)
        
if __name__=="__main__":
    main()