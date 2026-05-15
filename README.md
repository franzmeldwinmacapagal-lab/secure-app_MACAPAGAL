# DevSecOps Demo

This repository demonstrates a practical DevSecOps CI/CD pipeline using GitHub Actions.

## Repository Structure

secure-app_MACAPAGAL/

├── app/

│ └── main.py

├── tests/

│ └── test_main.py

├── Dockerfile

├── requirements.txt

└── .github/

└── workflows/

devsecops-pipeline.yml


---

## Features

- Secure Flask microservice
- Input validation and sanitization
- Unit testing with pytest
- Dependency vulnerability scanning
- Static code analysis
- Docker containerization
- Container vulnerability scanning
- Automated CI/CD pipeline with GitHub Actions

---

## Security Tools Used

| Tool | Purpose |
|------|----------|
| Safety | Dependency vulnerability scanning |
| pip-audit | Python package auditing |
| Bandit | Static security analysis |
| Flake8 | Python linting |
| Trivy | Container vulnerability scanning |

---

## CI/CD Pipeline Stages

1. Dependency Vulnerability Scan
2. Static Code Analysis
3. Unit Testing
4. Docker Container Build
5. Container Vulnerability Scan
6. Deployment Simulation

---

## Technologies Used

- Python 3.12
- Flask
- Docker
- GitHub Actions

---

## Sample API Endpoints

### Health Check
GET /health

### Create User
POST /api/user

### Get User
GET /api/user/<id>

---

## Purpose

This project was created for DevSecOps practical training and demonstration purposes, showing both secure development practices and CI/CD security automation.
