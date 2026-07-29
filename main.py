from cnnClassification import logger
from cnnClassification.pipeline.state_01_data_ingestion import DataIngetionTrainingPipeline
from cnnClassification.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline

STAGE_NAME = "Data Ingestion stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    data_ingestion = DataIngetionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>> state {STAGE_NAME} completed\n\nx=========x")
except Exception as e:
        logger.exception(e)
        raise e





## Stage02
STAGE_NAME = "Prepare base model"

try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = PrepareBaseModelTrainingPipeline()
    obj.main()
    logger.info(f">>>>>> state {STAGE_NAME} completed\n\nx=========x")
except Exception as e:
    logger.exception(e)
    raise e

