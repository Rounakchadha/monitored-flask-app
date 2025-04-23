
# 📊 Monitored Flask App — Real-Time DevOps Dashboard

This project demonstrates a DevOps-style monitoring setup using a Flask application, Prometheus metrics, and Grafana visualization.

---

## 🚀 Features

- Real-time tracking of:
  - ✅ Total requests
  - ⚠️ Exception count
  - ⏱️ Latency buckets
- Prometheus-compatible `/metrics` endpoint
- Grafana dashboard integration
- Interactive frontend to simulate traffic

---

## 📸 Screenshots

### 🔷 Frontend UI
<img width="577" alt="Screenshot 2025-04-16 at 10 14 03 AM" src="https://github.com/user-attachments/assets/465dd49f-62be-4e8b-90fa-86f6b582fa42" />


### 📈 Grafana Monitoring Dashboard

<img width="581" alt="Screenshot 2025-04-16 at 10 14 13 AM" src="https://github.com/user-attachments/assets/180f20a1-85d9-4330-babe-f3ff0e2107a0" />

---

## 🧰 Stack

- Python (Flask)
- Prometheus
- Grafana
- Custom metrics
- HTML/CSS frontend

---

## 🛠️ How to Run

```bash
# Clone repo
git clone https://github.com/YOUR_USERNAME/monitored-flask-app.git
cd monitored-flask-app

# Install dependencies
pip install -r requirements.txt

# Start the app
python app.py
```

Then open:

- `http://localhost:5001` – frontend
- `http://localhost:5001/metrics` – metrics endpoint
- Grafana at `http://localhost:3000`

---

## 👨‍💻 Simulate Usage

Click on:
- ✅ Simulate Request
- ⚠️ Simulate Error
- 📊 View Metrics

---

## 🧠 Learning Outcomes

- Instrumenting a Python app with custom metrics
- Monitoring with Prometheus + Grafana
- Building dashboards for observability

---

> 📦 Built as part of DevOps course submission for [Project #17].
