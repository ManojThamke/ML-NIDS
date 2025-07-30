# 🛠️ Technical Stack for ML-Based NIDS

## 🔍 Machine Learning (Python)

| Tool         | Purpose                      |
|--------------|------------------------------|
| Python 3.10+ | Base language                |
| pandas       | Data loading and preprocessing |
| scikit-learn | ML models (Isolation Forest, Random Forest) |
| joblib       | Model saving/loading         |
| scapy        | Packet sniffing              |
| pymongo      | MongoDB integration          |

---

## 🌐 Backend (Node.js + Express)

| Tool       | Purpose                      |
|------------|------------------------------|
| Node.js 18+| Backend runtime              |
| Express.js | REST API                     |
| mongoose   | MongoDB ORM                  |
| cors       | Cross-Origin support         |
| dotenv     | Environment variable config  |
| socket.io  | Real-time alerts via WebSocket |

---

## 💻 Frontend (React)

| Tool              | Purpose                      |
|-------------------|------------------------------|
| React 18+         | Frontend framework           |
| axios             | API communication            |
| react-router-dom  | Routing                      |
| recharts          | Charts for protocol stats    |
| tailwindcss       | Styling framework (optional) |

---

## 🧾 Additional Notes

- MongoDB used as primary database for storing alerts and traffic logs.
- MERN architecture ensures separation of concerns between ML, API, and frontend.
- Real-time support via WebSocket planned in Week 7.
