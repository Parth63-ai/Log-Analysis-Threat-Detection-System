# Log-Analysis-Threat-Detection-System

## 📌 Overview

This project demonstrates a basic Security Operations Center (SOC) workflow by analyzing system logs to detect suspicious activities such as brute-force attacks.

---

## 🎯 Objectives

- Analyze log files to identify failed login attempts  
- Detect brute-force attack patterns  
- Extract and track suspicious IP addresses  
- Generate alerts for potential threats  

---

## 🛠️ Tools Used

- Python  
- Log File Analysis  
- Basic Networking Concepts  

---

## 📁 Project Structure
Log-Analysis-Project
│
├── log_analysis.py
├── logs.txt
├── README.md
└── screenshots/

---

---

## ⚙️ How It Works

The script reads a log file and:

- Detects lines containing "Failed password"
- Extracts IP addresses from logs
- Counts repeated failed attempts
- Flags IPs exceeding a threshold

---

## 🚨 Detection Output

Example output: Possible brute force attack from 192.168.1.50 (5 attempts)

---

## 🖼️ Screenshots

<img width="608" height="367" alt="Screenshot 2026-03-23 212512" src="https://github.com/user-attachments/assets/85a9a7aa-654b-4187-a7da-3cfccfc435ab" />
<img width="421" height="75" alt="Screenshot 2026-03-23 212334" src="https://github.com/user-attachments/assets/f95edc6c-e9aa-4b0f-b7d0-92017c92567b" />

---

## 🚀 Future Improvements

- Add time-based attack detection  
- Integrate real-time monitoring  
- Use larger real-world datasets  

---

## 💡 Skills Demonstrated

- Log analysis  
- Threat detection  
- Python scripting  
- SOC investigation workflow  

---

## 👨‍💻 Author

Kumar Partha  
Cybersecurity Enthusiast 
