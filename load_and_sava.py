import keras
import os
import json
import sys
import pandas as pd

def model_save(model):
    model.save("my_model.h5")
    
def get_model():
    # Create a simple model.
    inputs = keras.Input(shape=(2,))
    outputs = keras.layers.Dense(1)(inputs)
    model = keras.Model(inputs, outputs)
    model.compile(optimizer="adam", loss="mean_squared_error")
    return model


def model_load():
    model = get_model()
    model.load_weights('my_model.h5')
    return model

def save_result(model,pars):
    answer = model.predict(pars)
          
          
    data1 = {"result" : str(answer[0][0])}
          
          
    with open("result.json",'w') as output_file:
        json.dump(data1,output_file)
    output_file.close()
    

if __name__ == "__main__":
    par1 = int(sys.argv[1])
    par2 = int(sys.argv[2])
    
    # .............
    # depends on model
    model = model_load()
    pars = pd.DataFrame([[par1, par2]])
    save_result(model,pars)
    
    
    
    
    
    




