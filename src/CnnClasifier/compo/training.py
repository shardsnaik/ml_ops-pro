from PIL import Image
from tensorflow.keras.optimizers import Adam
import os
from src.CnnClasifier.entity.model_training import TrainingConfig
import tensorflow as tf 
from pathlib import Path

class Training:
    def __init__(self, config: TrainingConfig):
         self.config = config

    def get_base_model(self):
         self.model = tf.keras.models.load_model(
              self.config.update_base_model_path
         )
    def train_valid_generator(self):
         datagen_kward = dict(
               rescale = 1./255,
            validation_split=0.20
         )

         dataflow_kwards = dict(
              
          #     print(self.config.params_img_size[:, -1]),

              
              target_size = self.config.params_img_size[:-1],
              batch_size = self.config.params_batch_size,
              interpolation = 'bilinear'
         )

         valid_datagen = tf.keras.preprocessing.image.ImageDataGenerator(
              **datagen_kward
         )

         self.valid_generator = valid_datagen.flow_from_directory(
              directory = self.config.training_data,
              subset = 'validation',
              shuffle = False,
              **dataflow_kwards
         )

         if self.config.params_agumentation:
              train_datagenearator = tf.keras.preprocessing.image.ImageDataGenerator(
                   rotation_range=40,
                horizontal_flip=True,
                width_shift_range=0.2,
                height_shift_range=0.2,
                shear_range=0.2,
                zoom_range=0.2,
                **datagen_kward
              )
         else:
              train_datagenearator = valid_datagen


         self.train_generator = train_datagenearator.flow_from_directory(
              directory=self.config.training_data,
                          subset="training",
                          shuffle=True,
                          **dataflow_kwards
         )
    @staticmethod
    def save_model(path: Path, model: tf.keras.Model):
         model.save(path)
        

    def train(self):
     #    self.steps_per_epoch = self.train_generator.samples // self.train_generator.batch_size
     #    self.validation_steps = self.valid_generator.samples // self.valid_generator.batch_size
        optimizer = Adam(learning_rate=0.001)


        self.model.compile(optimizer=optimizer)

        self.model.fit(
             self.train_generator,
             epochs = self.config.prams_epochs,
          #    steps_per_epoch=self.steps_per_epoch
          #    validation_steps=self.validation_steps,
            validation_data = self.valid_generator,
        )

        self.save_model(
             path= self.config.trained_model,
             model= self.model
        )