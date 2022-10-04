import re
from flask import Flask, jsonify, render_template, request,redirect, url_for
import config
from project_data.utils import milk_grade

app = Flask(__name__)
##########################################################
@app.route('/predict_milk_grade',methods = ['POST','GET'])
def get_milk_quality():
    print("We are using POST method")
    data = request.form
    pH = eval(data['pH'])
    Temprature = eval (data['Temprature'])
    Taste = eval(data['Taste'])
    Odor = eval(data['Odor'])
    Fat = eval (data['Fat'])
    Turbidity = eval (data['Turbidity'])
    Colour = eval (data['Colour'])

    print("pH,Temprature,Taste,Odor,Fat,Turbidity,Colour",pH,Temprature,Taste,Odor,Fat,Turbidity,Colour)
    milk_qua = milk_grade(pH,Temprature,Taste,Odor,Fat,Turbidity,Colour)
    grade =  milk_qua.get_milk_grade()

    return jsonify({"Result": f"Predicted milk grade is : {grade}"})


if __name__ == "__main__":
    app.run(host= '0.0.0.0', port = config.PORT_NUMBER,debug=True)
