from flask import Flask, request, jsonify
import util

app = Flask(__name__)

@app.route('/get_response', methods=['GET'])
def get_location_names():
    response = jsonify({
        'received': "true"  })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response



@app.route('/predict_depth', methods=['POST'])
def predict_home_depth():
    print("hello request received")
    year = float(request.form['year'])
    month = float(request.form['month'])
    irri = float(request.form['irri'])
    rain = float(request.form['rain'])
    temp = float(request.form['temp'])
    evap = float(request.form['evap'])

    print("hello request received")
    print(month)
    response = jsonify({
       'estimated_depth': util.get_estimated_depth(year,month,irri,rain,temp,evap)
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response






if __name__ == "__main__":
    print("Starting Python Flask Server For Depth depth Prediction...")
    util.load_saved_artifacts()
    app.run(debug=True,port=5000)