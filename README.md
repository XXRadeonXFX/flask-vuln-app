# Flask Vulnerable App 🚨

This is a deliberately vulnerable Flask web application created for security training, awareness, and testing security tools and techniques. **Do not deploy this application in a production environment.**

---

## 🧠 Purpose

The project is designed to help users:
- Understand common web vulnerabilities.
- Practice secure coding techniques.
- Test application security scanners and tools.

---

## 📁 Project Structure

```

flask-vuln-app/
│
├── app.py                 # Main Flask application
├── Dockerfile             # Containerization instructions
├── requirements.txt       # Python package dependencies
├── flask-report.json      # Sample scan report (likely from a security tool)
├── contrib/               # Contributions, helpers, or additional configs
├── reports/               # Contains reports/logs from scans or testing

````

---

## 🚀 Getting Started

### Prerequisites
- Docker (recommended)
- Python 3.8+ (if running locally)
- `pip` package manager

---

### 🐳 Run with Docker

```bash
docker build -t flask-vuln-app .
docker run -p 5000:5000 flask-vuln-app
````

Access the app at: [http://localhost:5000](http://localhost:5000)

---

### 🧪 Run Locally

```bash
pip install -r requirements.txt
python app.py
```

---

## ⚠️ Disclaimer

This application contains known vulnerabilities and is meant **only** for educational and testing purposes in **controlled environments**. Use responsibly.

---

## 📄 License

This project is licensed under the MIT License - see the `LICENSE` file for details.

---

## 👨‍💻 Author

Developed by [XXRadeonXFX](https://github.com/XXRadeonXFX)

---

## 📬 Contributing

Contributions, bug reports, and security fixes are welcome via pull requests.

```


