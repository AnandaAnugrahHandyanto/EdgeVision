# EdgeVision Repository

**Foundation setup for an edge vision project, providing a Flask API for various image edge detection algorithms, now with a modern web interface.**

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Local Setup (Without Docker)](#local-setup-without-docker)
  - [1. Clone the Repository](#1-clone-the-repository)
  - [2. Create & Activate Virtual Environment](#2-create--activate-virtual-environment)
  - [3. Install Dependencies](#3-install-dependencies)
  - [4. Update app.py (for local network access)](#4-update-apppy-for-local-network-access)
  - [5. Run the Flask Application](#5-run-the-flask-application)
  - [6. Access the Web Interface](#6-access-the-web-interface)
- [API Endpoints](#api-endpoints)
- [Project Structure](#project-structure)
- [Future Enhancements](#future-enhancements)
- [Contributing](#contributing)
- [License](#license)

## Overview
EdgeVision is a Python-based Flask application that offers a web interface and an API for real-time edge detection on images. It supports various algorithms like Canny, Sobel, Prewitt, and Laplacian. The application is designed to be easily deployable and includes a modern, responsive user interface inspired by Material You and glassmorphism design principles.

## Features
- Web-based interface for image upload and processing.
- REST API for programmatic access to edge detection functionalities.
- Supports Canny, Sobel, Prewitt, and Laplacian edge detection algorithms.
- Real-time preview of original and processed images.
- Responsive design for various screen sizes.

## Prerequisites
- Git
- Python 3.8+ (preferably 3.13 as used in `Dockerfile`)
- `pip` (Python package installer)

## Local Setup (Without Docker)

### 1. Clone the Repository
First, clone the repository to your local machine:
```bash
git clone https://github.com/AnandaAnugrahHandyanto/EdgeVision.git
cd EdgeVision
```

### 2. Create & Activate Virtual Environment
It's highly recommended to use a virtual environment to manage project dependencies:
```bash
python3 -m venv venv
source venv/bin/activate
```
You will see `(venv)` in your terminal prompt, indicating the virtual environment is active.

### 3. Install Dependencies
Install all required Python packages from `requirements.txt`.
**Note:** The `requirements.txt` might be missing `Flask` and `Pillow`. Please add them manually to `requirements.txt` if they are not present, then install:
```bash
# In requirements.txt, ensure these lines are present:
# Flask
# Pillow
# numpy>=2.0.0
# opencv-python>=4.10.0
# pydantic>=2.0.0
# requests>=2.31.0
# python-dotenv>=1.0.0

pip install -r requirements.txt
```

### 4. Update app.py (for local network access)
To allow access from devices other than `localhost`, ensure `app.py` binds to `0.0.0.0`. This change has been applied by Savarez.
```python
# In app.py, find the main execution block:
if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)
```

### 5. Run the Flask Application
With the virtual environment active, start the application:
```bash
python app.py
```
You should see output similar to:
```
 * Serving Flask app 'app'
 * Debug mode: off
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
```

### 6. Access the Web Interface
Open your web browser and navigate to:
`http://<YOUR_MACHINE_IP>:5000`
(Replace `<YOUR_MACHINE_IP>` with the actual IP address of your Arch Linux ARM machine, e.g., `http://192.168.1.11:5000`).

## API Endpoints

The core functionality is exposed via a REST API:

**Endpoint:** `/api/process`
**Method:** `POST`
**Description:** Processes an uploaded image using a specified edge detection algorithm.
**Request (multipart/form-data):**
- `file`: (Required) The image file to be processed.
- `filter`: (Optional) The edge detection algorithm to use. Default is `canny`.
  - Accepted values: `canny`, `sobel`, `prewitt`, `laplacian`

**Example cURL Request:**
```bash
# Using Canny filter (default)
curl -X POST -F "file=@your_image.png" http://<YOUR_MACHINE_IP>:5000/api/process > output_canny.png

# Using Sobel filter
curl -X POST -F "file=@your_image.png" -F "filter=sobel" http://<YOUR_MACHINE_IP>:5000/api/process > output_sobel.png
```

**Response:**
- On success: Returns the processed image as `image/png`.
- On error: Returns a JSON object with an `error` message and an appropriate HTTP status code (e.g., 400, 500).

## Project Structure
```
EdgeVision/
├── app.py                     # Main Flask application and API endpoints
├── processor.py               # Core image processing functions (edge detection algorithms)
├── requirements.txt           # Python dependencies
├── Dockerfile                 # Docker build instructions
├── docker-compose.yml         # Docker Compose configuration
├── templates/
│   └── index.html             # Web interface (HTML, CSS, JS) for image upload and display
├── static/                    # (Future: for CSS, JS, images if separated)
├── test_api.py                # Unit tests for the API
└── README.md                  # Project documentation (this file)
```

## Future Enhancements
- Docker deployment instructions for easier production setup.
- Advanced image processing features.
- User authentication and management.
- More robust error handling and input validation.

## Contributing
Feel free to fork the repository, make improvements, and submit pull requests.

## License
[Specify your project's license here, e.g., MIT License]
