from flask import Flask, request, jsonify, render_template
import torch
import cv2
import numpy as np
from PIL import Image
import os
import pathlib
temp = pathlib.PosixPath
pathlib.PosixPath = pathlib.WindowsPath
app = Flask(__name__)

# model = torch.hub.load('"C:\Users\rohit\Desktop\lomdu\huh\yolov5"', 'custom', path='C:\Users\rohit\Desktop\lomdu\huh\best.pt', source='local')

# Define paths using raw strings to avoid issues with backslashes
repo_path = r'C:\Users\win 10\Desktop\Unused Files\lom\lomdu\ambulance_detection_yolov5\yolov5'

weights_path = r'C:\Users\win 10\Desktop\Unused Files\lom\lomdu\ambulance_detection_yolov5\best.pt'

# Load the YOLOv5 model
model = torch.hub.load(repo_path, 'custom', path=weights_path, source='local')

# Perform inference (replace 'path_to_image.jpg' with the actual image path)
# results = model('path_to_image.jpg')
# results.show()

@app.route('/')
def home():
    # Render a simple homepage
    return render_template('index.html')

@app.route('/detect', methods=['POST'])
def pollTrafficLight():
    try:
        # Read image from request
        file = request.files['image']
        img = Image.open(file.stream).convert('RGB')
        img = np.array(img)

        # Perform detection
        results = model(img)
        detections = results.xyxy[0].tolist()

        # Check if an ambulance is detected
        ambulance_detected = False
        for *box, conf, cls in detections:
            if conf > 0.80:  # Confidence threshold
                ambulance_detected = True
                break

        return jsonify({"status": "green" if ambulance_detected else "red"})

    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(debug=True)
