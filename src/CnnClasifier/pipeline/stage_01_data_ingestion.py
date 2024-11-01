from src.CnnClasifier.cofig.configuration import ConfigurationManger
from src.CnnClasifier.compo.data_inges import DataIngestion
from src.CnnClasifier import logger

stage_name = 'Data Ingestion stage'

class Data_imgestionTraningPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManger()
        data_inges_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config= data_inges_config)
        data_ingestion.download_data()
        data_ingestion.extract_zip()
    
if __name__ == '__main__':
    try:
        logger.info('f>>>>>>>>> stage {stage_name} started <<<<<<<<')
        run = Data_imgestionTraningPipeline()
        run.main()
        logger.info(f'>>>>>>>>>> sttage {stage_name} completed... <<<<<<<<<<<<<<')    
    except Exception as e:
        logger.exception(e)
        raise e