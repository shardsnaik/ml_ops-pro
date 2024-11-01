from src.CnnClasifier.entity.prepar_bs_mdl_entity import preparebaseModelConfig
from src.CnnClasifier.constants import *
from src.CnnClasifier.utils.common import read_yaml, create_directories


class ConfigurationManeger:
    def __init__(self,
                 config_filepath = path_of_config,
                 params_filepath = path_of_params):
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)
        create_directories([self.config.artifacts_root])

    def get_prepare_base_model_config(self) ->preparebaseModelConfig:
        config = self.config.prepare_base_model
        create_directories([self.config.artifacts_root])

        prepare_base_model_config = preparebaseModelConfig(
            root_dir=Path(config.root_dir),
                        base_model_path=Path(config.base_model_path),
                        updated_base_model_path=Path(config.updated_base_model_path),
                        params_image_size=self.params.IMG_SIZE,
                        params_learning_rate=self.params.LEARNING_RATE,
                        params_include_top=self.params.INCLUDE_TOP,
                        params_weights=self.params.WEIGHTS,
                        params_classes=self.params.CLASSES
        )

        return prepare_base_model_config