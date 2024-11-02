from src.CnnClasifier.constants import *
from src.CnnClasifier.utils.common import read_yaml, create_directories, save_json
from src.CnnClasifier import logging
from src.CnnClasifier.entity.evalution_entity import EvaluationConfig

class ConfiManeger:
    
    def __init__(
        self,
        config_filepath = path_of_config,
        params_filepath = path_of_params):
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)

        create_directories([self.config.artifacts_root])

    
    def get_evaluation_config(self) -> EvaluationConfig:
        eval_config = EvaluationConfig(
            path_of_model="artifacts/training/model.h5",
            training_data="artifacts/data_ingestion/kidney-ct-scan-image",
            mlflow_uri="https://dagshub.com/sharadnaik001/ml_ops-pro.mlflow/#/",
            all_params=self.params,
            params_image_size=self.params.IMG_SIZE,
            params_batch_size=self.params.BATCH_SIZE
        )
        return eval_config



