# 🚑 Ambulance Detection System using YOLOv5 + Google Maps

A real-time computer vision system that detects ambulances using a fine-tuned YOLOv5 model and helps locate the nearest hospitals through Google Maps integration.

Built as a practical emergency-response prototype combining AI inference, geolocation, and mapping services.

---

## 👤 Author

**Mithul Narayana S**  
🔗 LinkedIn: https://www.linkedin.com/in/mithul-narayana-7169a4281/

---

## 🎯 Project Highlights

- ✅ Fine-tuned YOLOv5 model for ambulance detection  
- 🎥 Works on video streams / webcam  
- 📍 Retrieves current location  
- 🏥 Finds nearest hospitals based on user input  
- 🗺️ Google Maps API integration  
- ⚡ Real-time inference pipeline  
- 💼 applied AI project(For Recruiters)

---

## 🧠 Use Case

This system can assist:

- Traffic management systems  
- Smart city emergency routing  
- Ambulance priority signals  
- Healthcare dispatch monitoring  
- Road surveillance automation

---

## 🛠️ Tech Stack

- Python 3.9+
- PyTorch
- YOLOv5
- OpenCV
- Google Maps API
- HTML / JavaScript (frontend map view)
- REST API (optional backend integration)

---

## 📂 Project Structure

ambulance_detection_yolov5/
│
├── detection.py # Main detection script
├── best.pt # Fine-tuned YOLOv5 weights
├── yolov5/ # YOLOv5 repository
│
├── maps/
│ └── index.html # Google Maps hospital locator UI
│
├── assets/
│ └── samples/ # Sample images / videos
│
├── requirements.txt
└── README.md


---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository

git clone https://github.com/<your-username>/ambulance-detection-yolov5.git
cd ambulance-detection-yolov5


---

### 2️⃣ Create virtual environment

python -m venv venv
venv\Scripts\activate


---

### 3️⃣ Install dependencies

pip install -r requirements.txt


---

### 4️⃣ Google Maps API Key

Add your API key inside `index.html` or your config file:

https://maps.googleapis.com/maps/api/js?key=YOUR_API_KEY&libraries=places


---

## ▶️ Running the Ambulance Detector

From the project root:

python detection.py


---

## 🌍 Hospital Locator (Frontend)

Open:

maps/index.html


Or run using Live Server in VS Code for best results.

Enter a location → view nearby hospitals on Google Maps.

---

## 🧪 Model Training

The YOLOv5 model was fine-tuned on a custom ambulance dataset using transfer learning.

Training included:

- Custom labeled dataset
- Data augmentation
- Hyperparameter tuning
- Validation mAP monitoring

---

## 📈 Future Improvements

- 🔄 Automatic traffic signal prioritization
- 📡 IoT camera integration
- 📊 Dashboard analytics
- ☁️ Cloud deployment
- 📱 Mobile app version
- 🛰️ Live GPS feed from ambulances

---

## ⭐ Why This Project Stands Out

This is a complete applied-AI system:

Detection ➝ Location ➝ Decision Support

Perfect for roles in:

- Computer Vision
- AI Engineering
- Smart City Systems
- Autonomous Surveillance
- Healthcare Tech

---

## 📜 License

This project is for educational and research purposes.
