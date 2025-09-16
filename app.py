from flask import Flask, request, jsonify
import cv2
import numpy as np

app = Flask(__name__)

@app.route("/detect", methods=["POST"])
def detect():
    file = request.files['file']
    image = cv2.imdecode(np.frombuffer(file.read(), np.uint8), cv2.IMREAD_COLOR)
    h, w, _ = image.shape
    result = {
        "objects": [
            {"label": "person", "confidence": 0.87, "bbox": [int(w*0.1), int(h*0.1), int(w*0.4), int(h*0.8)]},
            {"label": "dog", "confidence": 0.78, "bbox": [int(w*0.6), int(h*0.3), int(w*0.9), int(h*0.7)]}
        ]
    }
    return jsonify(result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
