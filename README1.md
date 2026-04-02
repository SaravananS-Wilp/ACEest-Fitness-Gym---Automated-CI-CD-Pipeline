# ACEest Fitness Gym – Automated CI/CD Pipeline

## Project Overview

This project demonstrates a DevOps-based automated CI/CD pipeline for a simple Fitness Gym application built using Flask.
The objective of this project is to showcase how modern DevOps tools can automate the build, test, and deployment processes.

The project integrates:

* GitHub for version control
* Automated testing using Pytest
* Docker containerization
* CI pipeline using GitHub Actions
* Build automation using Jenkins

This pipeline ensures that every code change is automatically tested and validated before deployment.

# Technologies Used

| Technology     | Purpose                  |
| -------------- | ------------------------ |
| Python         | Backend programming      |
| Flask          | Web framework            |
| Pytest         | Unit testing             |
| Docker         | Containerization         |
| GitHub         | Version control          |
| GitHub Actions | Continuous Integration   |
| Jenkins        | Automated build pipeline |

# Project Structure

```
ACEest-Fitness-Gym---Automated-CI-CD-Pipeline
│
├── app.py
├── fitness_logic.py
├── requirements.txt
├── Dockerfile
├── README.md
│
├── tests
│   └── test_fitness_logic.py
│
└── .github
    └── workflows
        └── ci.yml
```

# Application Description

The Fitness Gym application provides simple functionality to calculate and evaluate basic fitness metrics.

### Main Components

app.py

Flask application that handles HTTP requests and responses.

fitness_logic.py

Contains the core fitness calculation logic separated from the main application to maintain modularity.

tests/test_fitness_logic.py

Unit tests written using Pytest to verify that the fitness logic works correctly.

# Setup Instructions

## 1. Clone the Repository

```
git clone https://github.com/SaravananS-Wilp/ACEest-Fitness-Gym---Automated-CI-CD-Pipeline.git
cd ACEest-Fitness-Gym---Automated-CI-CD-Pipeline
```

## 2. Install Dependencies

Make sure Python and pip are installed.

```
pip install -r requirements.txt
```

---

## 3. Run the Flask Application

```
python app.py
```

The application will run on:

```
http://localhost:5000
```


# Running Unit Tests

Unit tests are implemented using Pytest.

Run the following command:

```
pytest
```

Expected output:

```
3 passed
```

This confirms that the application logic is functioning correctly.

# Docker Containerization

The application is containerized using Docker to ensure portability and consistent deployment.

## Build Docker Image

```
docker build -t fitness-app .
```

## Run Docker Container


docker run -p 5000:5000 fitness-app
```

Now access the application at:

```
http://localhost:5000
```


# Continuous Integration with GitHub Actions

The project uses GitHub Actions to automatically run the CI pipeline whenever code is pushed to the repository.

The workflow file is located at:

```
.github/workflows/ci.yml
```

### CI Pipeline Steps

1. Checkout repository code
2. Install Python dependencies
3. Run Pytest unit tests
4. Build Docker image
5. Run Docker container

If all steps pass successfully, the pipeline shows a green check mark.

# Jenkins Build Integration

Jenkins is used as a build automation tool to pull the project from GitHub and execute the build steps.

## Jenkins Pipeline Steps

1. Pull code from GitHub repository
2. Install project dependencies
3. Execute build commands
4. Validate successful build

Jenkins automatically marks the job as SUCCESS if all steps complete without errors.

# CI/CD Pipeline Workflow

The automated workflow follows this sequence:

```
Developer pushes code
        ↓
GitHub Repository
        ↓
GitHub Actions CI Pipeline
        ↓
Run Pytest Tests
        ↓
Build Docker Image
        ↓
Jenkins Build Execution
        ↓
Build Success
```

This ensures every code update is automatically tested and validated.

# Learning Outcomes

Through this project, the following DevOps concepts were implemented:

* Source code management with GitHub
* Automated testing with Pytest
* Containerization using Docker
* Continuous Integration using GitHub Actions
* Build automation using Jenkins
* CI/CD pipeline design and implementation

# Future Improvements

Possible enhancements include:

* Deploying the container to a cloud platform
* Adding Kubernetes orchestration
* Implementing automated deployment
* Adding monitoring and logging tools
