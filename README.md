# 🔏 Password Genie 🧞  
## Password Generator, Strength Checker & Entropy Analyzer

**Password Genie** is a Python-based security learning tool that generates passwords, evaluates their strength, calculates password entropy, and estimates the time required to crack them using modern attack assumptions. This project demonstrates practical cybersecurity concepts such as **secure randomness, entropy-based strength evaluation, and password attack resistance**.

---

## Features

- **Secure Password Generation**  
  - Generates passwords using *cryptographically secure randomness* via Python’s `secrets` module.

- **Password Strength Evaluation**  
  - Rates passwords as **Weak, Moderate, Strong, or Very Strong** based on length and character diversity.

- **Entropy Calculation**  
  - Calculates password entropy *(randomness)* to quantify resistance against guessing attacks.

- **Crack Time Estimation**  
  - Estimates how long a modern GPU-based attacker would take to crack the password based on entropy.

- **Automatic Password Hardening**  
  - If a password is not rated *Very Strong*, the tool can automatically improve it by increasing entropy and complexity.

- **Interactive CLI Experience**  
  - Users can generate, analyze, and iteratively strengthen passwords in an interactive session.

- **Attack Awareness**  
  - Explains which common password attacks a *very strong* password helps defend against.

---

## Requirements 🧰

This project uses **only Python’s standard library** — no external dependencies required.

Modules used:
- `secrets`
- `string`
- `re`
- `math`
- `time`
- `hashlib`

---

## How to Run ⏯️

1. Clone or download the repository.
2. Ensure Python **3.6+** is installed.
3. Open a terminal and navigate to the project directory.
4. Run:
   ```bash
   python pw-genie.py

## Example Session

```bash
PW Genie: Password Generator & Strength Checker

Enter password length (e.g., 12 for a moderate password): 12
✔ Secure password generated using cryptographic randomness.

Generated password: fT9!kQ2@ZxM#
Strength: Strong

Entropy: 78.2 bits
Estimated time to crack: 4.3 million years

Would you like to improve this password to a very strong level? (y/n): y

Improving password...
[██████████████████████████] 100%

Password successfully hardened!

Final password: \25BQ$MjkaDj5p
Final strength: Very Strong
Final entropy: 91.76 bits
Estimated crack time: 13,295 million years
```

---

## How It Works 🔎
Passwords are evaluated using:

  - Length
  - Character diversity (lowercase, uppercase, digits, symbols)
  - A simplified scoring model designed for educational clarity

---

## Entropy Calculation

Entropy is calculated using:
```bash
entropy = length × log₂(character pool size)
```
Higher entropy corresponds to greater resistance against brute-force and guessing attacks.

---

## Crack Time Estimation ⏳

Crack time is estimated using entropy-based assumptions and simulated modern GPU attack speeds.
These values are approximations, not guarantees.

---

## Security Considerations

- Uses `secrets` instead of `random` for cryptographically secure generation

- Avoids storing or logging passwords

- Encourages long, unique, high-entropy passwords

- Considers real-world password attack models

---

## Contribution 🤝

Contributions are welcome.
Feel free to fork the repository, submit pull requests, or open issues for bugs or feature suggestions.

---


## Learn Something 🧠

- [Python - secrets](https://docs.python.org/3/library/secrets.html)
- [Python - hashlib](https://docs.python.org/3/library/hashlib.html)
- [Python - re, regex](https://docs.python.org/3/library/re.html)
- [Python - strings](https://docs.python.org/3/library/string.html)
- [Python - time](https://docs.python.org/3/library/time.html)
- [Python - math](https://docs.python.org/3/library/math.html)
- [GeeksforGeeks, Generating Strong Passwords](https://www.geeksforgeeks.org/python/generating-strong-password-using-python/)
- [GeeksforGeeks, Password Entropy](https://www.geeksforgeeks.org/computer-networks/password-entropy-in-cryptography/)

---

## Disclaimer ⚠️

This project is intended for educational purposes only.
Do not use generated passwords in production environments without proper security review, organizational approval, and additional protections such as password managers and multi-factor authentication.

---

## License

This project is licensed under the **MIT License** - see the `LICENSE`
 file for details.

---

## .gitignore

This project includes a `.gitignore` file to avoid tracking unnecessary files in the future (e.g., Python bytecode, virtual environments). Be sure to have a similar `.gitignore` if you're working on your own version of the project.

---
