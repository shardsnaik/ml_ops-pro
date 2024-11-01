from src.CnnClasifier.pipeline.stage_01_data_ingestion import Data_imgestionTraningPipeline
from src.CnnClasifier.pipeline.stage_02_pre_bse_mdl import pre_bs_mdl
from src.CnnClasifier.pipeline.stage_03_model_training import model_training
from src.CnnClasifier import logger


# if __name__ == '__main__':
#     stage_name = 'Data Ingestion Stage'
#     try:
#         logger.info('f>>>>>>>>> stage {stage_name} started <<<<<<<<')
#         data_ingestion = Data_imgestionTraningPipeline()
#         data_ingestion.main()
#         logger.info(f'>>>>>>>>>> sttage {stage_name} completed... <<<<<<<<<<<<<<')    
#     except Exception as e:
#         logger.exception(e)
#         raise e
    

if __name__ =='__main__':
    stage_name = 'preparing base model'
    try:
        logger.info('f>>>>>>>>> stage {stage_name} started <<<<<<<<')
        run = pre_bs_mdl()
        run.main()
        logger.info(f'>>>>>>>>>> sttage {stage_name} completed... <<<<<<<<<<<<<<')
    except Exception as e:
       raise e
    


# if __name__ == '__main__':
#      stage_name = 'Model training'
#      try:
#         logger.info('f>>>>>>>>>>> stage of  >>>>>>>>')
#         logger.info('f>>>>>>>>>>> MODEL TRAINING STARTED >>>>>>>>')
#         tra = model_training()
#         tra.main()
#         logger.info('f<<<<<<<<<<<<<<< stage of {stage_name} MODEL TRAINING FINISHED<<<<<<<<<<<<<<<<<<<')
#      except Exception as e:
#        raise e