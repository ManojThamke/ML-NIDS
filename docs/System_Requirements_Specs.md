# 📄 System Requirements Specification (SRS)

## 1. Project Title
**ML-Based Network Intrusion Detection System using Python and MERN Stack**

---

## 2. Functional Requirements

- Detect abnormal network traffic in real time.
- Classify each session as normal or anomaly.
- Store alerts in MongoDB.
- Provide API to fetch alerts and logs.
- Display alert dashboard in browser.
- Support traffic filtering and basic analytics.

---

## 3. Non-Functional Requirements

- **Performance**: Detection latency < 2 seconds.
- **Scalability**: Must handle moderate live traffic (~1000 packets/min).
- **Security**: JWT auth for dashboard (optional).
- **Maintainability**: Modular code with logging and comments.
- **Availability**: System runs reliably without constant human monitoring.

---

## 4. Use Cases

### Admin:
- Start/stop the packet sniffer
- View alerts
- Filter traffic logs
- Change detection thresholds

### System:
- Capture live packets
- Run ML model and classify
- Save alerts
- Push alerts via WebSocket (optional)

---

## 5. Constraints

- Must use Python for detection.
- Must use MongoDB for storage.
- Limited system resources (runs on developer machine).
- No deep packet inspection (only flow metadata used).

---

## 6. Tools & Technologies

- Python (scikit-learn, scapy)
- MERN Stack (MongoDB, Express, React, Node.js)
- VS Code
- GitHub
- MongoDB Compass
