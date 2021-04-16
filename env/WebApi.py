from flask import Flask
from flask import jsonify, request

app = Flask(__name__)


@app.route('/GetMaxFloor', methods=['POST'])
def GetMaxFloor():
    floorList = request.json["data"]

    if len(floorList) == 0:
        return jsonify({"error": "Veri boş olamaz!"})

    x = len(floorList)     # Kat Sayısı
    y = len(floorList[0])  # Bina Sayısı
    floor = 0              # Binadaki Toplam Kat Sayısı
    maxFloor = 0           # En Yüksek Kat Sayısı

    for i in floorList:
        if len(i) != y:
            return jsonify({"error": "Bina kat sayıları birbirine eşit olmalı."})
        for j in i:
            if j > 1 or j < 0:
                return jsonify({"error": "Bina katları sadece 0 ve 1 ile temsil edilebilir."})

    for i in range(y):
        floor = 0
        for j in range(x, 0, -1):
            if floorList[j - 1][i] != 1:
                break  # Kat Yoksa çık
            else:
                floor += floorList[j - 1][i]

        if floor > maxFloor:
            maxFloor = floor

    return jsonify({"success": maxFloor})

