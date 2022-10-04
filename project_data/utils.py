import pickle
import json
import config
import numpy as np

class milk_grade():
    def __init__(self,pH,Temprature,Taste,Odor,Fat,Turbidity,Colour):
        self.pH = pH
        self.Temprature = Temprature
        self.Taste =Taste
        self.Odor = Odor
        self.Fat = Fat
        self.Turbidity = Turbidity
        self.Colour = Colour

    def load_model(self):
        with open(config.MODEL_FILE_PATH,'rb') as f:
            self.model = pickle.load(f)

        with open(config.JSON_FILE_PATH,'r') as f:
            self.json_data = json.load(f)

    

    def get_milk_grade(self):
        self.load_model()
        print("*"*30,self.json_data)
        
        test_array = np.zeros(len(self.json_data['columns']))
        test_array[0] = self.pH
        test_array[1] = self.Temprature
        test_array[2] = self.Taste
        test_array[3] = self.Odor
        test_array[4] = self.Fat
        test_array[5] = self.Turbidity
        test_array[6] = self.Colour

        predicted_milk_grade = self.model.predict([test_array])
        return predicted_milk_grade


      
# if __name__ == "__main__":
#     pH = 8.5
#     Temprature = 48
#     Taste = 0.2
#     Odor = 3.0
#     Fat = 2.5
#     Turbidity = 2
#     Colour = 260.0

#     milk_qua = milk_grade(pH,Temprature,Taste,Odor,Fat,Turbidity,Colour)
#     milk_qua.get_predicted_milk_grade()