from src.CnnClasifier.constants import *
from src.CnnClasifier.utils.common import read_yaml, create_directories
from src.CnnClasifier.entity.model_training import TrainingConfig
import os

class ConfigManeger:
    def __init__(self,
                 config_filepath = path_of_config,
                 params_filepat = path_of_params):
        self.config =  read_yaml(config_filepath)
        self.params = read_yaml(params_filepat)

        create_directories([self.config.artifacts_root])


    def get_tarinig_config(self) ->TrainingConfig:
        training = self.config.model_training
        prepare_base_model = self.config.prepare_base_model

        params = self.params

        training_data = os.path.join(self.config.data_ingestion.unzip_dir, 'kidney-ct-scan-image')

        create_directories([Path(training.root_dir)])

        tarining_config = TrainingConfig(
            root_dir=Path(training.root_dir),
            trained_model= Path(training.trained_model_path),
            update_base_model_path = Path(prepare_base_model.updated_base_model_path),
            training_data =  Path(training_data),
            prams_epochs= params.EPOCHS,
            params_batch_size= params.BATCH_SIZE,
            params_agumentation= params.AUGMENTATION,
            params_img_size=params.IMG_SIZE

        )
        return tarining_config