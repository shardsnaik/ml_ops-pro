import tensorflow as tf
from src.CnnClasifier.cofig.evalution_config import ConfiManeger
from src.CnnClasifier.compo.evalution import Evaluation
from src.CnnClasifier import logger
model = tf.keras.models.load_model('artifacts/training/model.h5')

# model.summary()
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

class eval:
    def __init__(self):
        pass

    def run_pipeline(self):
        
       confi = ConfiManeger()
       evl = confi.get_evaluation_config()
       eval = Evaluation(evl)
       eval.evaluation()
       eval.log_into_mlFlow()


if __name__ == '__main__':
    try:
        logger.info('f>>>>>>>>>>> stage of  >>>>>>>>')
        logger.info('f>>>>>>>>>>> MODEL EVALUATION STARTED >>>>>>>>')
        tra = eval()
        tra.main()
        logger.info('f<<<<<<<<<<<<<<< stage of MODEL EVALUATION WITH ML-FLOW FINISHED<<<<<<<<<<<<<<<<<<<')
    except Exception as d:
       raise d