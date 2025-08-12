# 🌧 Rain Alert System

A Python-based weather notification tool that checks the upcoming forecast and sends an SMS alert if rain is expected, helping you never forget your umbrella. ☂️  

---

## 🚀 Features
- Fetches location coordinates using the **OpenWeather Geocoding API**.
- Retrieves a short-term weather forecast from **OpenWeather**.
- Detects rainy weather conditions.
- Sends a **Twilio SMS alert** to your phone when rain is predicted.
- Uses **environment variables** to keep your API keys and credentials secure.

---

## 📦 Requirements
Before running the project, ensure you have:
- Python 3.7+
- OpenWeather API Key
- Twilio Account SID & Auth Token
- `.env` file to store credentials securely

---

## ⚙️ Installation
1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/rain-alert.git
   cd rain-alert
