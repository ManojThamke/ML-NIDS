# Network Intrusion Detection System – Scope Document

## 🎯 Project Goal

Develop a Network Intrusion Detection System using Machine Learning to analyze real-time network traffic and visualize alerts in a MERN stack web dashboard.

---

## 🧩 Core Modules

- **Packet Capture Engine:** Captures real-time traffic (Scapy/Pyshark).
- **ML Detection Engine:** Classifies sessions as normal/anomaly using trained models.
- **Alert Storage:** Stores structured alerts in MongoDB.
- **REST API Backend:** Built in Express.js to expose alerts and settings.
- **Web Dashboard:** React UI to view alerts, traffic, and analytics.

---

## ✅ In-Scope Features

- Real-time alert generation
- Visualization dashboard (protocols, anomalies)
- Historical alert logs
- Filter/search by IP, prediction, date
- Manual settings (e.g., thresholds)

---

## ❌ Out-of-Scope Features

- Automatic blocking of IPs or connections
- Role-based access control
- Multi-user collaboration
- Complex distributed data collection

---

## 🎯 Success Criteria

- ✅ Detection accuracy ≥ **90%**
- ✅ Real-time detection latency < **2 seconds**
- ✅ Dashboard updates latency < **3 seconds**
- ✅ Integration of real-time and offline ML models
