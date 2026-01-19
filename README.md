# Password Genie 🧞
## Password Generator & Strength Checker

This Python project allows you to *generate secure passwords, check their strength, calculate their entropy, and estimate the time it would take to crack* them using modern attack techniques. 

---

## Features

- **Password Generation**: Secure passwords are generated using *cryptographic randomness*.
  
- **Password Strength Checker**: A simplified password strength checker rates passwords as *"Weak", "Moderate", "Strong", or "Very Strong".*
  
- **Entropy Calculation**: The entropy **(randomness)** of a password is calculated, which helps estimate how difficult it would be to guess.
  
- **Crack Time Estimate**: Estimates how long it would take a modern GPU to *crack* the password based on its **entropy.**
  
- **Security Improvement**: Automatically improves a password's strength if it is not deemed *"Very Strong"*.
  
- **Interactive Session**: Users can interactively generate passwords, check their strength, and improve them until they meet high security standards.
  
- **Password Attack Explanations**: Explains what types of attacks a very strong password defends against.

---

## Requirements

This project does **not** require any external libraries or dependencies. It uses only Python's built-in libraries, including:
- `secrets`
- `string`
- `re`
- `math`
- `time`
- `hashlib`

---

### How to Run :running:

1. Clone or download the repository.
2. Make sure you have Python installed on your machine (Python 3.6+ recommended).
3. Open a terminal and navigate to the project directory.
4. Run the script:
   ```bash
   python pw-genie.py

---

### Example Session :computer:

Here's an example of what the program does:
```
PW Genie: Password Generator & Strength Checker

Enter password length (e.g., 12 for a moderate password): 1
✔ Secure password generated using cryptographic randomness.

Generated password: \
Strength: Weak

Entropy: 0 bits
Estimated time to crack: 0.0 days

Would you like to improve this password to a very strong level? (y/n): y

Improving password to a very strong level...
Improving password strength
[█-------------------------███████████████████████████] 100%

Password is now very strong after improvements!

Improvements Made:
Added random characters to increase entropy. This makes the password harder to crack using brute-force or dictionary attacks.

Final improved password: \25BQ$MjkaDj5p
Final strength: Very Strong

Final entropy: 91.76 bits
Final estimated time to crack: 13295.53 million years

Want to learn more about how very strong passwords defend against particular attacks? (y/n): y

What Does a Very Strong Password Defend Against?
1. Brute-Force Attacks: A strong password with a mix of letters, numbers, and symbols is harder to crack through brute-force attempts, where every possible combination is tried.
Press Enter to continue...

2. Dictionary Attacks: Password dictionaries are used to guess passwords quickly. A very strong password containing a variety of characters significantly reduces the chance of being guessed.
Press Enter to continue...

3. Rainbow Table Attacks: Using precomputed tables of hash values to reverse hashes into passwords is ineffective against a strong password with proper salting and length.
Press Enter to continue...

4. Social Engineering Attacks: A strong password is less likely to be guessed based on personal information (like birthdates or names) that may be exploited in social engineering.
Press Enter to continue...

5. Phishing Attacks: Although phishing relies on tricking the user, a very strong password can still make it harder for an attacker to use a stolen password across different platforms.
Press Enter to continue...

In summary, a very strong password greatly reduces the likelihood of a successful attack, especially when used in combination with other security measures like two-factor authentication (2FA).
Press Enter to finish...

Generate another password? (y/n): n

Session complete. Stay secure!
```

---

## Features in Detail :mag_right:

**Password Strength**: The password strength checker evaluates the password based on length, character diversity *(lowercase, uppercase, numbers, symbols)*, and a simplified scoring system.

**Entropy Calculation**: Entropy is calculated using the formula: **length * log2(pool_size)**, where the *pool size depends on the character set used in the password.*

**Crack Time Estimate**: Based on entropy, the script *estimates how long* it would take for an attacker using a modern GPU *to crack the password.*

---

## Contribution :fork_and_knife:

Feel free to fork the repository, make changes, and submit pull requests. If you encounter any issues or have suggestions for improvements, please open an issue.

---

>
> **Note**: ⚠️ This project does not store or use any user data, and it is intended solely for educational and personal use in improving password security.

---

## License

This project is licensed under the MIT License - see the LICENSE
 file for details.

---

## .gitignore

This project includes a `.gitignore` file to avoid tracking unnecessary files (e.g., Python bytecode, virtual environments). Be sure to have a similar `.gitignore` if you're working on your own version of the project.

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

## Disclaimer
This project is for educational purposes only.  
Do not use generated passwords in production systems without proper security review.

---

