# Ride-Hailing GPS Stream Load Test

This repository contains the WebSocket load testing module from our research on modern ride-hailing systems. It is designed to simulate 2,000 concurrent driver GPS WebSocket streams to evaluate the high-concurrency capacity of the distributed serverless architecture.

## 📊 Performance Metrics & Results

After establishing connections, the platform successfully stabilized at approximately **248.37 Requests Per Second (RPS)** with a **0% failure rate** on active streaming. The system demonstrated an exceptional median response time of merely **0.11 ms** and a 99th percentile (P99) latency of strictly **1 ms**, confirming the high-concurrency capability of the AWS serverless container architecture.

📄 **[Click here to view the detailed full Locust load test report (PDF)](locust_test_result.pdf)**

### 📈 System Performance Under Load
![System Performance Under Load](load_test_result.png)

*(Note: Ensure `load_test_result.png` is uploaded to the repository, or replace this line with a drag-and-drop generated link!)*

### 📋 Detailed Locust Load Testing Statistics (Table III)
Below is the empirical validation data recorded during the maximum stress period:

<img width="680" height="114" alt="table_3_stats" src="https://github.com/user-attachments/assets/fe7b4b02-0de2-477b-95f5-a06fe7976013" />

---

## 🛠 Prerequisites (依赖安装)
Ensure you have Python 3 installed. Clean up any existing conflicting websocket libraries and install the required ones:

```bash
pip3 uninstall websocket -y
pip3 install websocket-client websockets
