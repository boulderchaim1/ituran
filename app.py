from flask import Flask, jsonify, request
import requests
from datetime import datetime
import time
import re
from firebase import firebase
app = Flask(__name__)
db = firebase.FirebaseApplication('https://maps-d75e4.firebaseio.com/')


@app.route('/maps', methods=['POST'])
def index():
    data = request.get_json()
    car = data['car']
    id = data ['id']
    #r = requests.get('http://iweb2.ituranusa.com/ituranmobileservice/mobileservice.asmx/PlatformSendLocationRequest?UserName=7188641629&Password=uber&strPlatformId='+id+'')
    #time.sleep(60)
    l = requests.get('http://iweb2.ituranusa.com/ituranmobileservice/mobileservice.asmx/GetVehicleLocation?UserName=7188641629&Password=uber&strPlatformId='+id+'')
    lat = re.findall("<Lat>(.*?)</Lat>", l.text)
    lon = re.findall("<Lon>(.*?)</Lon>", l.text)
    date = re.findall("<Date>(.*?)</Date>", l.text)
    datej = ''.join(date)
    lonf = float(''.join(lon))
    latf = float(''.join(lat))
    print (latf, lonf, datej)

    data = {"lat": latf,
            'lon': lonf,
            'ituran_id': int(id),
            'last_update': datej,
            'last check': datetime.now()}
    get = db.put("/car", car, data)


    json_object = l.text
    return json_object




    return jsonify({'Result':'sucsess' , 'car' : car , 'id': id})


if __name__ == "__main__":
    app.run(debug=True)