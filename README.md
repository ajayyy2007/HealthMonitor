# 🐳 HealthMonitor

A containerized website monitoring application built to gain hands-on experience with Docker and Docker Compose.

HealthMonitor allows users to enter a website URL and check its availability through a web interface. The application is divided into separate frontend, backend, and database containers.

---

## 🚀 Project Overview

HealthMonitor is a multi-container application consisting of:

- 🌐 **Frontend** — Nginx serving the web interface
- ⚙️ **Backend** — Python Flask REST API
- 🐘 **Database** — PostgreSQL for storing application data

The entire application is managed using **Docker Compose**.

```text
                    Browser
                       │
                       ▼
              ┌─────────────────┐
              │    Frontend     │
              │      Nginx      │
              │     :8000       │
              └────────┬────────┘
                       │
                       ▼
              ┌─────────────────┐
              │     Backend     │
              │     Flask       │
              │     :5000       │
              └────────┬────────┘
                       │
                       ▼
              ┌─────────────────┐
              │    PostgreSQL   │
              │      :5432      │
              └─────────────────┘

              Docker Compose

              <img width="972" height="493" alt="image" src="https://github.com/user-attachments/assets/e49b949b-2b39-48b6-9565-7fd6ea5b98f5" />

