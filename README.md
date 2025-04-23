
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
![Frontend](screenshots/frontend.png)

### 📈 Grafana Monitoring Dashboard
![Grafana](screenshots/grafana.png)

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
