from flask import Flask, request, jsonify
import json
import numpy as np



app = Flask(__name__)

array1 = []
array2 = []

#Default route
@app.route("/",methods=["GET"])
def func():
    return "ciao"

#Route Predict 
@app.route("/predict", methods=["POST"])
def predict():
    #access to data in the post request
    data1 = request.json
    #Transform data in json format
    row = json.loads(data1)["data"]
    #Extract the 50 rows
    arr = row.split("/")
    #Extract the 7 parameters and add it to the matrix
    matr = []
    #Add parameters to the global array
    for i in arr:
        matr.append(i.split("@"))
    
    array1.append(matr)     

    for i in array1:
        for q in i :
            array2.append(q)
    

    np.savetxt("provacsv.csv",
           array2,
           delimiter =", ",
           fmt ='% s')
    #Return a confirmation status
    return "Tutto ok"

#Flask default configuration
if __name__ == "__main__" :
    #0.0.0.0 is the default location (if the client is not che same machine see the ip of the server)
    app.run(debug=False, host= '0.0.0.0')
    #app.run(port=5000, debug=False)