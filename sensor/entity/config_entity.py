from datetime import datetime
import os
from sensor.constant import training_pipeline


class TrainingPipelineConfig():
    def __init__(self, timestamp: datetime.now()):
        timestamp = timestamp.strftime('%m_%d_%Y_%H_%M_%S')

        self.timestamp = training_pipeline.PIPELINE_NAME
        self.artifact_dir = os.path.join(
            training_pipeline.ARTIFACT_DIR, timestamp)

        self.timestamp: str = timestamp


class DataIngestionConfig():
    def __init__(self, training_pipeline_config: TrainingPipelineConfig):
        self.data_ingestion_dir = os.path.join(
            training_pipeline_config.artifact_dir, training_pipeline.DATA_INGESTION_DIR_NAME)
        self.data_ingestion_dir = os.path.join(
            training_pipeline_config.artifact_dir, training_pipeline.DATA_INGESTION_DIR_NAME)
