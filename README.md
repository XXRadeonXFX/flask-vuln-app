# Flask Vulnerable App 🚨
**[Latest Data of Vulnerabilities — CVE.org](https://www.cve.org/)**

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

## 🧪 Vulnerability Scan Report (via Trivy)

Trivy was used to scan the container image for known vulnerabilities.

### 🐧 OS-Level Vulnerabilities (Debian 12.11)
| Severity     | Count |
|--------------|-------|
| CRITICAL     | 2     |
| HIGH         | 7     |

#### Notable CVEs:
- **CVE-2025-6965**: SQLite Integer Truncation [🔗](https://avd.aquasec.com/nvd/cve-2025-6965)
- **CVE-2023-45853**: zlib heap-based buffer overflow [🔗](https://avd.aquasec.com/nvd/cve-2023-45853)
- **CVE-2025-4802**: glibc `LD_LIBRARY_PATH` unsafe search [🔗](https://avd.aquasec.com/nvd/cve-2025-4802)

---

### 🐍 Python Package Vulnerabilities

| Package     | CVE ID                 | Severity | Fixed Version |
|-------------|------------------------|----------|----------------|
| Flask       | CVE-2023-38061         | HIGH     | 2.3.2, 2.2.5   |
| requests    | CVE-2018-18074         | HIGH     | 2.20.0         |
| setuptools  | CVE-2022-40897         | HIGH     | 65.5.1         |
| setuptools  | CVE-2024-6345          | HIGH     | 70.0.0         |
| setuptools  | CVE-2025-47273         | HIGH     | 78.1.1         |
| urllib3     | CVE-2019-11324         | HIGH     | 1.24.2         |
| urllib3     | CVE-2023-43804         | HIGH     | 2.0.6, 1.26.17 |

---

### 🔐 Secrets Detected
- A **Stripe Secret Key** was found in `app.py` (line 3).
  - `API_KEY = "sk_test_..."`

⚠️ Secrets should not be hardcoded. Consider using environment variables or a secure vault solution.

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

