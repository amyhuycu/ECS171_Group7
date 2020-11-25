import keras
import os
import json
import sys
import panda as pd

def model_save(model):
    model.save("my_model")

def model_load():
    model = keras.models.load_model("my_model")
    return model

def save_result(model,pars):
    answer = model.predict(pars)
    data = [{"result",str(answer)}]
    with open("result.json",'w') as output_file:
        json.dump(data,output_file)
    output_file.close()

if __name__ == "__main__":
    par1 = int(sys.argv[1])
    par2 = int(sys.argv[2])
    
    # .............
    # depends on model
    model = model_load() //pre-trained model
    pars = pd.Series([par1, par2])
    save_result(model,pars)
    
    
    
    
    




