from cnnClassification import logger
from cnnClassification.pipeline.stage_01_data_ingestion import DataIngetionTrainingPipeline
from cnnClassification.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline
from cnnClassification.pipeline.stage_03_training import ModelTrainingPipeline
from cnnClassification.pipeline.stage_04_evaluation import EvaluationPipeline


# Stage 01
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


# Stage 3

STAGE_NAME = "Training"

try:
    logger.info(f"*******************")
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = ModelTrainingPipeline()
    obj.main()
    logger.info(f">>>>>> state {STAGE_NAME} completed\n\nx=========x")
except Exception as e:
    logger.exception(e)
    raise e


# Stage 4
STAGE_NAME = "Evaluation stage"
try:
   logger.info(f"*******************")
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
   model_evalution = EvaluationPipeline()
   model_evalution.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")

except Exception as e:
        logger.exception(e)
        raise e