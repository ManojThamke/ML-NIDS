# 📊 CICIDS2017 Dataset Summary

## ✅ Files Included (8 CSVs):
- Monday-WorkingHours.pcap_ISCX.csv
- Tuesday-WorkingHours.pcap_ISCX.csv
- Wednesday-workingHours.pcap_ISCX.csv
- Thursday-WorkingHours-Morning-WebAttacks.pcap_ISCX.csv
- Thursday-WorkingHours-Afternoon-Infilteration.pcap_ISCX.csv
- Friday-WorkingHours-Morning.pcap_ISCX.csv
- Friday-WorkingHours-Afternoon-PortScan.pcap_ISCX.csv
- Friday-WorkingHours-Afternoon-DDos.pcap_ISCX.csv

## 🧠 Total Features:
- 78 columns per row  
- Includes numerical and categorical features like:
  - `Flow Duration`, `Protocol`, `Src IP`, `Dst IP`, `Packet Length Mean`, etc.
  - Final column: **Label** (e.g., `BENIGN`, `DDoS`, `PortScan`, etc.)

## 🎯 Labels Present:
- BENIGN
- DDoS
- PortScan
- Web Attack (Brute Force, XSS, SQL Injection)
- Infiltration
- DoS (GoldenEye, Hulk, Slowloris, SlowHTTPTest)
- Heartbleed
- Botnet

## ⚠️ Observations:
- Some features have **missing or infinite values**
- A few files are large (~100MB+)
- Label imbalance: e.g., BENIGN vs. others

## 📁 Directory:
Stored at: `data/cicids2017/`
