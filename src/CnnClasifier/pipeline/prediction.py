import os
import numpy
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

class PredictionPipeline:
    def __init__(self, filename):
        self.filename = filename


    def predict(self):
        # load model
        model = load_model(os.path.join('artifacts', 'training/model.h5'))
        imagename = self.filename
        test_image  = image.load_img(imagename, target_size = (224, 224))
        test_image = image.img_to_array(test_image)
        test_image = numpy.expand_dims(test_image, axis=0)
        result = numpy.argmax(model.predict(test_image), axis=1)
        print(result)
        if result[0] == 1:
                    prediction = 'Tumor'
                    return [{ "image" : prediction}]
        else:
                    prediction = 'Normal'
                    return [{ "image" : prediction}]


# cld = PredictionPipeline(os.path.join('artifacts\\data_ingestion\\kidney-ct-scan-image\\Normal', 'Normal- (8).jpg'))

# cld.predict()