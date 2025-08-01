
# Brute Force Login with Dynamic CSRF Token

This repository contains a Python script and examples of brute-force attacks against login pages protected with dynamic CSRF tokens. 
The content is intended **strictly for educational purposes**, to demonstrate offensive security techniques and promote secure development practices in web applications.

## 🧠 Purpose

- Teach how CSRF tokens works in web forms
- Demonstrate how to automate authenticated brute-force attacks while respecting tokens and session management
- Help students and professionals understand common attack vectors and how to defend against them

## ⚠️ Legal Disclaimer

> This project is provided **for educational and research purposes only**. Using the techniques demonstrated here on unauthorized systems may violate local laws and regulations. The author **takes no responsibility for any misuse** of the content in this repository.

## 📄 License

This project is licensed under the [MIT License](LICENSE). You are free to use, modify, and distribute it as long as the original copyright
notice is retained.

## 🚀 How to Use

### 🔧 Requirements
- Python 3.x
- `requests` and `beautifulsoup4` libraries:
  ```bash
  pip install requests beautifulsoup4
  ```

### 📥 Download the script
Clone the repository or download the script directly:

```bash
git clone https://github.com/edusantos33/bruteforce_csrf_token.git
cd bruteforce_csrf_token
```

### 🛠 Prepare your wordlists

Example `users.txt`:
```
admin
root
```

Example `passwords.txt` (use `/usr/share/wordlists/rockyou.txt` or similar):
```
123456
admin123
password
```

### ▶️ Run the script

```bash
python3 bruteforce_csrf_token.py \
  --url http://localhost:8088/login.php \
  --userlist users.txt \
  --wordlist /usr/share/wordlists/rockyou.txt \
  --output found.txt
```

If the login is successful, the script will show the result and optionally save it in `found.txt`.

---

**Eduardo Santos**  
Application Security Specialist  
