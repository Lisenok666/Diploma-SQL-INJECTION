from tensorflow.keras import models, layers
import pickle
import os

os.environ["CUDA_VISIBLE_DEVICES"]="-1" 

PATH_MODEL = './lib/cnn.h5' 
PATH_Transform = './lib/vectorizer.pkl'



class SqlInjection: 
    def __init__(self):
        self.transformer = None
        self.clf = None
    
    def load_model(self):
        model = models.Sequential()
        model.add(layers.Conv1D(32, 1, activation = 'relu', input_shape = (1,7711)))
        model.add(layers.Conv1D(32, 1, activation = 'relu'))
        model.add(layers.Flatten())
        model.add(layers.Dense(1, activation = 'sigmoid'))
        model.load_weights(PATH_MODEL)
        self.clf = model
        with open(PATH_Transform, 'rb') as f:
            self.transformer = pickle.load(f)


        

def create_model():
    model = SqlInjection()
    model.load_model()
    return model
