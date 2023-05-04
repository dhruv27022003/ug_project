import pickle
import json
import numpy as np

__data_columns = None
__model = None

def get_estimated_depth(Year,Month,Irrigation,Rainfall,Tem,Evaporation):
    try:
        loc_index = __data_columns.index()
    except:
        loc_index = -1
    print("Data recieved") 
    x = np.zeros(len(__data_columns))
    x[0] = Year
    x[1] = Month
    x[2] = Irrigation
    x[3] = Rainfall
    x[4] = Tem
    x[5] = Evaporation
    if loc_index>=0:
        x[loc_index] = 1
    c= __model.predict([x])[0];
    
    print(c)
    print(type(c));
    print("yooo2")
    
    return 40-round(c,2)


def load_saved_artifacts():
    print("loading saved artifacts...start1")
    global  __data_columns
    with open("server/columns.json", "r") as f:
        __data_columns = json.load(f)['data_columns']
    global __model
    if __model is None:
       with open('server/waterdept.pickle', 'rb') as f:
          __model = pickle.load(f)
    print("loading saved artifacts...done")



