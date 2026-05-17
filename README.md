Project — DevSecOps CI/CD Pipeline
Overview
This project implements a complete DevSecOps CI/CD pipeline using GitHub Actions, Docker, AWS EC2, and HashiCorp Vault. The objective was to automate application deployment while integrating security controls across the CI/CD lifecycle.
The pipeline performs security scanning, Docker image creation, multi-environment deployment, and secret management.

Technologies Used
•	GitHub Actions
•	Docker
•	AWS EC2
•	Python Flask
•	HashiCorp Vault
•	Terraform

Features Implemented
CI/CD Automation
•	Automatic pipeline trigger on code push
•	Docker image build automation
•	Automated deployment to multiple environments
Security Controls
SAST Scan
Tool: Bandit
Dependency Scan
Tool: Safety
Secret Scan
Tool: Gitleaks
IaC Validation
Terraform security validation for infrastructure configurations.

Secrets Management
HashiCorp Vault was used for centralized secret management.
Secrets Stored:
•	EC2 credentials
•	Application secrets
•	Deployment credentials
Example:
vault kv put secret/app db_user="admin" db_password="DevSec@123"

Deployment Environments
Environment	Port
Dev	5000
Staging	5001
Production	5002
All environments were deployed automatically using Docker containers.

Deployment Flow
Developer Pushes Code ↓ GitHub Actions Pipeline Triggered ↓ Security Scans Executed ↓ Docker Image Build ↓ Vault Secret Validation ↓ Automated EC2 Deployment ↓ Dev → Staging → Production

Project Structure
project5-devsecops-pipeline/
│
├── .github/workflows/pipeline.yml
├── app/app.py
├── terraform/main.tf
├── Dockerfile
├── requirements.txt
└── README.md

Verification Commands
Verify Containers
docker ps
Verify Application
curl http://<EC2_PUBLIC_IP>:5000
curl http://<EC2_PUBLIC_IP>:5001
curl http://<EC2_PUBLIC_IP>:5002

Key Learnings
•	DevSecOps lifecycle implementation
•	CI/CD automation using GitHub Actions
•	Docker containerization
•	AWS EC2 deployment
•	Security scanning techniques
•	HashiCorp Vault secret management
•	Multi-environment deployment workflows

Future Improvements
•	Kubernetes deployment
•	Jenkins integration
•	Vault AppRole authentication
•	Trivy container scanning
•	Monitoring using Prometheus and Grafana

Author
Shreyashi Shree
