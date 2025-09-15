  Object Detection Microservice

This project implements a **microservice architecture** for object detection using Python and Docker. It consists of two main components:

1. **UI Backend** – Accepts image uploads and forwards them to the AI backend.
2. **AI Backend** – Processes images using OpenCV and provides object detection results in JSON format along with annotated images.

The entire solution is containerized with Docker, making it portable and easy to deploy on any system, even without a GPU.

---

Features

- Image upload via REST API using **FastAPI**.
- Object detection via **Flask** and **OpenCV** (YOLO-style bounding boxes).
- Outputs include:
  - JSON detection results (labels, confidence, bounding boxes).
  - Annotated images with bounding boxes.
- CPU-friendly — works without GPU acceleration.
- Fully containerized with **Docker Compose** for seamless deployment.
- Easy-to-follow documentation and reproducible environment.

---

Project Structure

object_detection_project/
├── ui_backend/
│ ├── Dockerfile
│ ├── requirements.txt
│ └── main.py
├── ai_backend/
│ ├── Dockerfile
│ ├── requirements.txt
│ └── app.py
├── output_image.jpg
├── detection_result.json
├── docker-compose.yml
└── README.md

yaml
Copy code

---

## 🚀 Getting Started

### Prerequisites
- [Docker](https://www.docker.com/get-started) installed on your machine.

### Run the Project

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/object-detection-microservice.git
   cd object-detection-microservice
Build and start the containers:

bash
Copy code
docker-compose up --build
Access the UI backend API at:

bash
Copy code
http://localhost:8000/upload-image
Use tools like Postman or curl to upload images:

bash
Copy code
curl -X POST "http://localhost:8000/upload-image" -F "file=@your-image.jpg"
The API will return a JSON response with detected objects.

📦 Output
Example JSON Response:
json
Copy code
{
  "objects": [
    {
      "label": "person",
      "confidence": 0.87,
      "bbox": [45, 60, 200, 400]
    },
    {
      "label": "dog",
      "confidence": 0.78,
      "bbox": [300, 150, 450, 350]
    }
  ]
}
Annotated Image:
The output image will include bounding boxes and labels drawn around detected objects.

🛠 Technologies Used
Python 3.9

FastAPI for UI API service.

Flask for AI detection service.

OpenCV for image processing and object detection.

Docker and Docker Compose for containerization.

CPU-based processing — no GPU required.

📖 References
YOLOv3 GitHub

FastAPI Documentation

Flask Documentation

OpenCV Python Tutorials

📂 Additional Notes
This project is designed for educational and prototyping purposes.
The AI detection is a simulated version using OpenCV and sample data. For production, integration with real models like YOLOv3 is recommended.

The Docker setup ensures that the solution can be run on different machines without dependency issues.

The AI detection is a simulated version using OpenCV and sample data. For production, integration with real models like YOLOv3 is recommended.

The Docker setup ensures that the solution can be run on different machines without dependency issues.
