from src.CnnClasifier.constants import *
from src.CnnClasifier.utils.common import read_yaml, create_directories
from src.CnnClasifier.entity.config_entity import DataIngestionConig_return_type

class ConfigurationManger:
    def __init__(self,
                 config_filepath = path_of_config,
                 params_filepath = path_of_params):
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)
        
        create_directories([self.config.artifacts_root])


    def get_data_ingestion_config(self)-> DataIngestionConig_return_type:
        config = self.config.data_ingestion

        create_directories([config.root_dir])
        data_ingestion_config = DataIngestionConig_return_type(
        root_dir= config.root_dir,
        source_URL=config.source_URL,
        local_data_file= config.local_data_file,
        unzip_dir=config.unzip_dir
    )

        return data_ingestion_config