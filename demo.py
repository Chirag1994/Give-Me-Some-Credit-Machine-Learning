from Give_Me_Some_Credit.components.data_ingestion import DataIngestion
from Give_Me_Some_Credit.config.configuration import Configuration
from Give_Me_Some_Credit.components.data_validation import DataValidation
from Give_Me_Some_Credit.components.data_transformation import DataTransformation
from Give_Me_Some_Credit.components.model_trainer import ModelTrainer

if __name__ == "__main__":
    data_ingestion_config_results = Configuration().get_data_ingestion_config()
    data_ingestion_artifact_results = DataIngestion(
        data_ingestion_config_results
    ).initiate_data_ingestion()
    data_validation_config_results = Configuration().get_data_validation_config()
    data_validation_artifact_results = DataValidation(
        data_validation_config=data_validation_config_results,
        data_ingestion_artifact=data_ingestion_artifact_results,
        data_ingestion_config=data_ingestion_config_results,
    ).initiate_data_validation()
    data_transformation_config_results = (
        Configuration().get_data_transformation_config()
    )
    data_transformation_artifact_results = DataTransformation(
        data_transformation_config=data_transformation_config_results,
        data_ingestion_artifact=data_ingestion_artifact_results,
        data_validation_artifact=data_validation_artifact_results,
    ).initiate_data_transformation()
    model_trainer_config_results = Configuration().get_model_trainer_config()
    model_trainer_artifact_results = ModelTrainer(
        data_transformation_artifact=data_transformation_artifact_results,
        model_trainer_config=model_trainer_config_results,
    ).initiate_model_trainer()
