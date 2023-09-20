import math
from flask import Flask,request,render_template
import joblib
from preprocessor import preprocess
import pandas as pd



app=Flask(__name__)

#loading the model
model=joblib.load('svr-model.joblib')


@app.route('/')
def home():
    return render_template('index.html')



@app.route('/',methods=['POST'])
def predict():
    try:        
         model_data = request.form
         processed_data = preprocess(model_data)
         result = model.predict(pd.DataFrame([processed_data]))
         print(result)
         x=float(math.exp(result))
         y="{:.2f}".format(x)

         return render_template('index.html',results=y)


    except ValueError:
        return render_template('index.html')
   

if __name__=="__main__":
    app.run(debug=True)






