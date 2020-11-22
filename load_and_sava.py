import keras
import os
import json

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




