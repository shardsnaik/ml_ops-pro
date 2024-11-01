import os
from src.CnnClasifier.entity.config_entity import DataIngestionConig_return_type
from src.CnnClasifier import logger
import gdown
import zipfile
class DataIngestion:
    def __init__(self, config: DataIngestionConig_return_type):
        self.config = config
    
    def download_data(self)->str:
        '''fetch data from url'''

        try:
            dataset_url = self.config.source_URL
            zip_down_dir = self.config.local_data_file
            os.makedirs('artifacts/data_ingestion', exist_ok=True)
            logger.info(f'downloading dataset from url {dataset_url} into file {zip_down_dir}')
            
            file_id = dataset_url.split("/")[-2]
            prefix = 'https://drive.google.com/uc?/export=download&id='
            gdown.download(prefix+file_id,zip_down_dir)

            logger.info(f"Downloaded data from {dataset_url} into file {zip_down_dir}")

        except Exception as e:
            raise e
        
    
    def extract_zip(self):
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok= True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip:
            zip.extractall(unzip_path)
