from cnnClassification import logger
from cnnClassification.pipeline.state_01_data_ingestion import DataIngetionTrainingPipeline

STAGE_NAME = "Data Ingestion stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    data_ingestion = DataIngetionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>> state {STAGE_NAME} completed\n\nx=========x")
except Exception as e:
        logger.exception(e)
        raise e


