import dagshub
import tensorflow as tf
import mlflow
from src.CnnClasifier.cofig.evalution_config import EvaluationConfig
from pathlib import Path
from src.CnnClasifier.utils.common import save_json
from src.CnnClasifier import logging
from urllib.parse import urlparse

model = tf.keras.models.load_model('artifacts/training/model.h5')
dagshub.init(repo_owner='sharadnaik001', repo_name='ml_ops-pro', mlflow=True)


class Evaluation:
    def __init__(self, config: EvaluationConfig):
        self.config = config

    
    def _valid_generator(self):

        datagenerator_kwargs = dict(
            rescale = 1./255,
            validation_split=0.30
        )

        dataflow_kwargs = dict(
            target_size=self.config.params_image_size[:-1],
            batch_size=self.config.params_batch_size,
            interpolation="bilinear"
        )

        valid_datagenerator = tf.keras.preprocessing.image.ImageDataGenerator(
            **datagenerator_kwargs
        )

        self.valid_generator = valid_datagenerator.flow_from_directory(
            directory=self.config.training_data,
            subset="validation",
            shuffle=False,
            **dataflow_kwargs
        )



    @staticmethod
    def load_model(path: Path)-> tf.keras.Model:
        return tf.keras.models.load_model(path)
    
    def evaluation(self):
        self.model  = self.load_model(self.config.path_of_model)
        self._valid_generator()
        self.score = model.evaluate(self.valid_generator)
        self.save_score()

    def save_score(self):
        scores = {"loss": self.score[0], "accuracy": self.score[1]}
        save_json(path=Path("scores.json"), data=scores)



    def log_into_mlFlow(self):

       mlflow.set_registry_uri(self.config.mlflow_uri)
       tracking_url_type_store = urlparse(mlflow.get_tracking_uri()).scheme
       mlflow.end_run()  # End any active run before starting a new one
   
       with mlflow.start_run():
           mlflow.log_params(self.config.all_params)
           mlflow.log_metrics({"loss": self.score[0], "accuracy": self.score[1]})
   
           if tracking_url_type_store != "file":
               # Register the model if not using the 'file' scheme
               try:
                   mlflow.keras.log_model(self.model, "model", registered_model_name="VGG16Model")
               except mlflow.exceptions.MlflowException as e:
                   logging.warning(f"Model registration failed: {str(e)}")
           else:
               # Log model without registering if using a local file store
               mlflow.keras.log_model(self.model, "model")








