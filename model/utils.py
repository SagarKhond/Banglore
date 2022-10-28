
## utils file
import pickle
import json
import pandas as pd
import numpy as np
import config


class HousePrice():
    def __init__(self,size,bath,balcony,total_squre_fit,area_type,location):
        self.size = size
        self.bath = bath
        self.balcony = balcony
        self.total_squre_fit=total_squre_fit
        
        
        self.area_type="area_type_"+area_type
        self.location="location_"+location
       

    def load_model(self):
        with open(config.MODEL_FILE_PATH, "rb") as f:
            self.model = pickle.load(f)

        with open(config.JSON_FILE_PATH,"r") as f:
            self.json_data = json.load(f)

    def get_predicted_price(self):

        self.load_model()  # Calling load_model method to get model and json_data

        area_type_index = self.json_data['column'].index(self.area_type)
        location_index = self.json_data['column'].index(self.location)
        array = np.zeros(len(self.json_data['column']))

        array[0]=self.size
        array[1]=self.bath
        array[2]=self.balcony
        array[3]=self.total_squre_fit
        

        array[area_type_index]=1
        array[location_index]=1

        print("Test Array -->\n",array)
        predicted_charges = self.model.predict([array])[0]
        print("predicted_car",predicted_charges)
        return np.around(predicted_charges, 2)


if __name__ == "__main__":
    size=13.0
    bath=2.0
    balcony=1.0
    total_squre_fit=2000

    # one hot encoded values
    area_type="Built-up  Area"
    location="Electronic City"
    # area_type_col="area_type_"+area_type
    # site_location_col="site_location_"+site_location


    med_ins = HousePrice(size,bath,balcony,total_squre_fit,area_type,location)
    charges = med_ins.get_predicted_price()
    print()
    print(f"The House Price in Banglore is {charges} Rs-\ Only(Lakh)")