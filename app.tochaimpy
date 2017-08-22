from flask import Flask, jsonify, request
import requests
import time

app = Flask(__name__)

@app.route('/maps', methods=['POST'])
def index():
    data = request.get_json()
    car = data['car']
    id = data ['id']
    r = requests.get('http://iweb2.ituranusa.com/ituranmobileservice/mobileservice.asmx/PlatformSendLocationRequest?UserName=7188641629&Password=uber&strPlatformId='+id+'')
    time.sleep(60)
    l = requests.get('http://iweb2.ituranusa.com/ituranmobileservice/mobileservice.asmx/GetVehicleLocation?UserName=7188641629&Password=uber&strPlatformId='+id+'')

    json_object = l.text
    return json_object




    return jsonify({'Result':'sucsess' , 'car' : car , 'id': id})


if __name__ == "__main__":
    app.run(debug=True)