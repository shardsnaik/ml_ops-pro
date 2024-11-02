from src.CnnClasifier.cofig.training_config import ConfigManeger
from src.CnnClasifier.compo.training import Training
from src.CnnClasifier import logger

stage_name = '...Model Training....'

class model_training:
     def __init__(self):
    
          pass
     

     def main(self):
         conf = ConfigManeger()
         training_confi = conf.get_tarinig_config()
         training = Training(config=training_confi)
         training.get_base_model()
         training.train_valid_generator()
         training.train()

if __name__ == '__main__':
     try:
        logger.info('f>>>>>>>>>>> stage of  >>>>>>>>')
        logger.info('f>>>>>>>>>>> MODEL TRAINING STARTED >>>>>>>>')
        tra = model_training()
        tra.main()
        logger.info('f<<<<<<<<<<<<<<< stage of {stage_name} MODEL TRAINING FINISHED<<<<<<<<<<<<<<<<<<<')
     except Exception as e:
       raise e