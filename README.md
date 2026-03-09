# ACEest Fitness Gym – Automated CI/CD Pipeline

## Project Overview

This project demonstrates a DevOps-based automated CI/CD pipeline for a simple Fitness Gym web application built using Flask.

The objective of this project is to showcase how modern DevOps tools automate the build, test, and deployment processes.

The pipeline integrates:

* GitHub for version control
* Jenkins for build automation
* Pytest for automated testing
* Docker for containerization

This ensures that every code change is automatically tested and validated before deployment.

---

## Technologies Used

| Technology     | Purpose                    |
| -------------- | -------------------------- |
| Python         | Backend programming        |
| Flask          | Web framework              |
| Pytest         | Unit testing               |
| Docker         | Containerization           |
| Docker Compose | Multi-container management |
| GitHub         | Version control            |
| Jenkins        | CI/CD automation           |

---

## Project Structure

```
ACEest-Fitness-Gym---Automated-CI-CD-Pipeline
│
├── app.py
├── fitness_logic.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── README.md
│
├── tests
│   └── test_fitness_logic.py
│
├── screenshots
│   ├── Jenkins Dashboard.png
│   ├── Jenkins Build Configuration.png
│   ├── Jenkins Console Output.png
│
└── .github
    └── workflows
        └── main.yml
```

---

## Application Description

The Fitness Gym application calculates basic fitness metrics such as BMI.

### Main Components

**app.py**

Flask application responsible for handling web requests and responses.

**fitness_logic.py**

Contains the core logic for performing fitness calculations, separated from the main application to maintain modularity.

**tests/test_fitness_logic.py**

Unit tests written using Pytest to verify that the fitness logic functions correctly.

---

## Setup Instructions

### 1. Clone the Repository

```
git clone https://github.com/SaravananS-Wilp/ACEest-Fitness-Gym---Automated-CI-CD-Pipeline.git
cd ACEest-Fitness-Gym---Automated-CI-CD-Pipeline
```

---

### 2. Install Dependencies

```
pip install -r requirements.txt
```

---

### 3. Run the Application

```
python app.py
```

The application will run at:

```
http://localhost:5000
```

---

## Running Unit Tests

Execute the following command:

```
pytest
```

Expected output:

```
3 passed
```

This confirms that the application logic is functioning correctly.

---

## Docker Containerization

Docker ensures that the application runs consistently across different environments.

### Build Docker Image

```
docker build -t fitness-app .
```

### Run Docker Container

```
docker run -p 5000:5000 fitness-app
```

Now access the application at:

```
http://localhost:5000
```

---

## CI/CD Pipeline Workflow

The automated workflow follows this sequence:

```
Developer pushes code
        ↓
GitHub Repository
        ↓
Jenkins CI Pipeline
        ↓
Install Dependencies
        ↓
Run Pytest Unit Tests
        ↓
Build Docker Image
        ↓
Run Docker Container
```

This ensures every code update is automatically tested and validated.

---

## Jenkins Pipeline Steps

Jenkins automates the following steps:

1. Pull code from GitHub repository
2. Install project dependencies
3. Run automated tests using Pytest
4. Build Docker image
5. Deploy and run the container

If all steps execute successfully, Jenkins marks the build as **SUCCESS**.

---

## Screenshots

Refer to the **screenshots** folder for Jenkins pipeline configuration and build execution screenshots.

---

## Learning Outcomes

Through this project, the following DevOps concepts were implemented:

* Source code management using GitHub
* Automated testing with Pytest
* Containerization using Docker
* Continuous Integration using Jenkins
* CI/CD pipeline design and implementation

---

## Future Improvements

Possible enhancements include:

* Deploying the container to a cloud platform
* Adding Kubernetes orchestration
* Implementing automated production deployment
* Adding monitoring and logging tools
