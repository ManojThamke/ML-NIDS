# 📊 Comparison of Existing NIDS Tools

| Tool     | Packet Capture Method | Detection Technique       | Output Format | Pros                                     | Cons                                  |
|----------|------------------------|----------------------------|---------------|------------------------------------------|---------------------------------------|
| **Snort**    | libpcap (raw packets)     | Signature-based (rules)     | Text/Alert logs | Fast, widely used, real-time             | Limited to known attacks              |
| **Suricata** | AF_PACKET, PF_RING, libpcap | Signature + anomaly hybrid | JSON logs     | Multi-threaded, detailed logs            | Heavy on resources                    |
| **Zeek**     | libpcap                | Behavior-based (scripts)    | TSV/JSON logs | Highly customizable, scriptable         | Harder to configure than Snort        |

---

## 🔁 Key Concepts to Reuse

- Store alerts in **JSON format** (inspired by Suricata)
- Use **modular detection pipeline** (inspired by Zeek)
- Build a **real-time dashboard** to monitor traffic visually (extension of all tools)
- Incorporate both **signature (offline)** and **anomaly-based (real-time)** detection

---

## 🔧 Draft Architecture Sketch

