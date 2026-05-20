<h1 align="center">🚀 3-Tier Full Stack DevOps Application</h1>

<h3 align="center">
Frontend + Backend + Database Architecture Integrated with CI/CD Automation
</h3>

🔗 **Documentation**: 
[View Project Docs] 
(https://1drv.ms/w/c/b04ed05d887aa81f/IQBrf_kQBqCXSJV8Vp_bGct2AfyONuDMTKTpPShF_pbdyLk?e=KTHCbo)

<p align="center">
  <img src="images/architecture.png" width="100%">
</p>

---

# 📌 Project Overview

Developed a complete full-stack message storage application using HTML, CSS, JavaScript, Python Flask, and MySQL.

The project follows a modern 3-tier architecture with clear separation between:

- Frontend Layer
- Backend Layer
- Database Layer

The application was integrated with DevOps automation tools to simulate a real-world production deployment workflow.

---

# 🏗️ Architecture

<p align="center">
  <img src="images/architecture.png" width="100%">
</p>

---

# 🚀 Technologies Used

<p align="center">
  <img src="https://skillicons.dev/icons?i=git,github,docker,jenkins,python,mysql,html,css,linux" />
</p>

| Technology | Purpose |
|------------|----------|
| GitHub | Version Control |
| Jenkins | CI/CD Automation |
| Docker | Containerization |
| Python Flask | Backend Development |
| HTML & CSS | Frontend Development |
| MySQL | Database |
| Linux | Deployment Environment |

---

# 💻 Development Process

## 🎨 Frontend Development

- Built responsive user interfaces using HTML and CSS
- Created a clean and user-friendly application layout

---

## ⚙️ Backend Development

- Developed backend APIs using Python Flask
- Managed application logic and request handling
- Connected frontend with database operations

---

## 🗄️ Database Integration

- Used MySQL for storing application data
- Implemented database connectivity with Flask
- Managed records efficiently using SQL queries

---

# 🔄 Version Control

- Managed the complete source code using Git and GitHub
- Maintained repository history and tracked changes
- Followed collaborative development workflow practices

---

# ⚡ CI/CD Automation

Integrated Jenkins to automate the complete software delivery process.

## Jenkins Pipeline Workflow

```text
Developer Push
      ↓
GitHub Repository
      ↓
Jenkins Pipeline Trigger
      ↓
Docker Image Build
      ↓
Container Deployment
      ↓
Application Running
```

---

# 🐳 Containerization

Used Docker and Docker Compose to containerize the entire application.

## Services

- Frontend Container
- Backend Container
- MySQL Database Container

This ensured:
- Consistent deployment
- Environment portability
- Simplified application management

---

# ⚙️ DevOps Implementation

- Automated deployment workflow
- Reduced manual operational tasks
- Improved deployment speed and reliability
- Simulated real-world DevOps practices

---

# 📂 Project Structure

```text
project/
│
├── frontend/
├── backend/
├── database/
├── docker/
├── jenkins/
├── screenshots/
├── images/
└── README.md
```

---

# 📥 Clone Repository

```bash
git clone https://github.com/chandusaigari/project.git
```

---

# 🔧 Git Commands

```bash
git init

git clone https://github.com/chandusaigari/project.git

git branch -M main

git status

git remote add origin https://github.com/your_username/project

git add .

git commit -m "code committed"

git push origin main
```

If your repository already contains files:

```bash
git pull origin main
```

---

# ⚙️ Prerequisites

Make sure the following tools are installed:

- Docker
- Docker Compose
- Jenkins
- Ubuntu/Linux Environment

---

# 🚀 Jenkins Setup

Open Ubuntu terminal and start Jenkins.

After Jenkins starts, access it in browser:

```text
http://localhost:8080
```

<p align="center">
  <img src="images/1.0.png" width="800">
</p>
<p align="center">
  <img src="images/1.1.png" width="800">
</p>

---

# 🔐 Jenkins Dashboard

Login using Jenkins username and password.

 <p align="center">
  <img src="images/1.2.png" width="800">
</p>
<p align="center">
  <img src="images/1.3.png" width="800">
</p>
 
 

---

# 🛠️ Create Jenkins Job

- Click "New Item"
- Enter Job Name
- Select "Pipeline"
  <p align="center">
  <img src="images/1.4.png" width="800">
</p>
<p align="center">
  <img src="images/1.5.png" width="800">
 

---

# 🔗 Configure GitHub Repository

- Select:
  - Pipeline Script from SCM
  - SCM as Git
- Add Repository URL
- Choose main/master branch
</p>
<p align="center">
  <img src="images/1.6.png" width="800">
</p>
<p align="center">
  <img src="images/1.7.png" width="800">
</p>
<p align="center">
  <img src="images/1.8.png" width="800">
</p>

<p align="center">
  <img src="images/1.9.png" width="800">
</p>
 

---

# ▶️ Build Pipeline

Click:

```text
BUILD NOW
```

<p align="center">
  <img src="images/2.1.png" width="800">
</p>
<p align="center">
  <img src="images/2.2.png" width="800">
</p>

---

# 📊 Blue Ocean Visualization

Install the Blue Ocean plugin to visualize pipeline stages.

<p align="center">
  <img src="images/2.5.png" width="800">
</p>

---

# 📜 Console Output

Console output helps identify build failures and errors.

<p align="center">
  <img src="images/2.4.png" width="800">
</p>

---

# 🐳 Docker Permission Fix

If Jenkins cannot access Docker:

```bash
sudo usermod -aG docker jenkins
```

Restart Jenkins after executing the command.

---

# 📦 Running Containers

Check active containers:

```bash
docker ps
```

<p align="center">
  <img src="images/2.6.png" width="800">
</p>

<p align="center">
  <img src="images/2.7.png" width="800">
</p>

---
#  📧 Email Notification

Open Email:

```text
you will recieve a message upon success or Failure
```

<p align="center">
  <img src="images/3.2.png" width="800">
</p>
 
---
#  🐳 Docker Hub

Open DckerHub:

```text
you will recieve a image pushed to your github account
```

<p align="center">
  <img src="images/3.1.png" width="800">
</p>
---

# 🌐 Access Application

Open browser:

```text
http://localhost:5000
```

<p align="center">
  <img src="images/2.8.png" width="800">
</p>
<p align="center">
  <img src="images/2.9.png" width="800">
</p>
---
 

# 📈 Future Scope

## ☸️ Kubernetes Integration

This project can be enhanced using Kubernetes for:

- Auto Scaling
- Load Balancing
- Self Healing
- Production-grade Orchestration

---

## 📊 Monitoring Stack

Future monitoring implementation includes:

- Prometheus for Metrics Collection
- Grafana for Dashboard Visualization

These tools will improve:
- Performance Monitoring
- Resource Tracking
- System Observability

---

# 🎯 Conclusion

This project provided hands-on experience in:

- Full Stack Development
- CI/CD Pipeline Automation
- Docker Containerization
- Jenkins Integration
- DevOps Deployment Practices

It helped in understanding real-world software deployment workflows and production-level automation processes.

---

# 📬 Contact

I am actively seeking opportunities in DevOps and related fields.

If you find this project interesting, I would be grateful for an opportunity to contribute and prove my skills in a professional environment.

## 📧 Reach Me

- Email: chandusaigari6@gmail.com
- Phone: +91-7396618269

---

# 🤝 Contribution

Pull requests are welcome.

---

# 📜 License

MIT License
