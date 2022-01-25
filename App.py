from flask import Flask, request, jsonify
import json
import numpy as np
import datetime
import socket
import threading


 
UDP_IP = "0.0.0.0"
UDP_PORT = 65013
BUFFER_SIZE = 128



app = Flask(__name__)

array1 = []
array2 = []

def udpFunc():
    sock = socket.socket(socket.AF_INET, # Internet
                        socket.SOCK_DGRAM) # UDP
    sock.bind((UDP_IP, UDP_PORT))
    conta = 0
    while True:
        data = sock.recvfrom(BUFFER_SIZE)
        if data:           

            row = data[0]
            encoding = 'utf-8'
            stringa = str(row, encoding=encoding)

            arr = stringa.split("@")
            
            array1.append(arr)       
            
            if conta == 49:
                np.savetxt("provacsv.csv",
                    array1,
                    delimiter =", ",
                    fmt ='% s')
                conta = 0
            conta += 1

    sock.close()


#Default route
@app.route("/timestamp",methods=["GET"])
def func():
    #take timestamp in seconds
    ts = str(datetime.datetime.now().timestamp())
    #take microseconds of timestamp in order to have time in format secondsFrom1970.microseconds
    micros = str(datetime.datetime.now().microsecond)
    return (ts, micros)

@app.route("/streaming",methods=["GET"])
def func2():
    thread = threading.Thread(target=udpFunc)
    thread.start()
    return "Streaming partito"

#Route Predict 
@app.route("/predict", methods=["POST"])
def predict():
    #access to data in the post request
    data1 = request.json
    #Transform data in json format
    data1 = json.dumps(data1 )


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

    array2.clear()
    #Return a confirmation status
    return "Tutto ok"

#Flask default configuration
if __name__ == "__main__" :
    #0.0.0.0 is the default location (if the client is not che same machine see the ip of the server)
    app.run(debug=False, host= '0.0.0.0')
    #app.run(port=5000, debug=False)