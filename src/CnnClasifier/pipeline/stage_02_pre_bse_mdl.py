from src.CnnClasifier.cofig.prepr_bse_mdl_config import ConfigurationManeger
from src.CnnClasifier.compo.prepare_base_model import PreparebaseModel
from src.CnnClasifier import logger


stage_name = 'Preparing BAse Model ...'


class pre_bs_mdl:
    def __init__(self):
        pass


    def main(self):
        confi = ConfigurationManeger()
        prepare_base_model_Config = confi.get_prepare_base_model_config()
        prepare_base_model = PreparebaseModel(prepare_base_model_Config)
        prepare_base_model.get_base_model()
        prepare_base_model.update_base_model()

if __name__ =='__main__':
    try:
        logger.info('f>>>>>>>>> stage {stage_name} started <<<<<<<<')
        run = pre_bs_mdl()
        run.main()
        logger.info(f'>>>>>>>>>> sttage {stage_name} completed... <<<<<<<<<<<<<<')
    except Exception as e:
       raise e