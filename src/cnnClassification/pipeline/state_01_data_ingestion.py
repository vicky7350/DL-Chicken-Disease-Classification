from cnnClassification.config.configuration import ConfigurationManager
from cnnClassification.components.data_ingestion import DataIngestion
from cnnClassification import logger


STAGE_NAME = "Data Ingestion stage"

class DataIngetionTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()



if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = DataIngetionTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> state {STAGE_NAME} completed\n\nx=========x")
    except Exception as e:
        logger.exception(e)
        raise e
        