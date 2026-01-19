# ---------------- IMPORTS ----------------
import secrets  # For generating secure random values
import string  # For working with string characters
import re  # For regular expression matching
import math  # For math-related functions
import time  # For time-related functions
import hashlib  # For cryptographic hashing functions

# ---------------- CONSTANTS ----------------
# ANSI color codes for terminal output
RESET = "\033[0m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
RED = "\033[31m"
CYAN = "\033[36m"
BOLD = "\033[1m"
MAGENTA = "\033[35m"

# ---------------- HELPER FUNCTIONS ----------------

def progress_bar(label, duration=1.2, width=30):
    print(f"{CYAN}{label}{RESET}")
    for i in range(width + 1):
        percent = int((i / width) * 100)
        bar = "█" * i + "-" * (width - i)
        print(f"\r[{bar}] {percent}%", end="", flush=True)
        time.sleep(duration / width)
    print("\n")

# ---------------- PASSWORD GENERATION ----------------
def generate_password(length=12):
    all_chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(all_chars) for _ in range(length))
    print(f"{GREEN}✔ Secure password generated using cryptographic randomness.{RESET}")
    return password
    
# ---------------- CALCULATE ENTROPY ----------------
def calculate_entropy(password):
    pool = 0
    if re.search(r"[a-z]", password): pool += 26
    if re.search(r"[A-Z]", password): pool += 26
    if re.search(r"[0-9]", password): pool += 10
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password): pool += 32

    entropy = len(password) * math.log2(pool) if pool > 0 else 0
    return round(entropy, 2)

# ---------------- ATTACK TIME ESTIMATE ----------------

def estimate_crack_time(entropy):
    guesses_per_second = 1e10  # 10 billion guesses/sec (modern GPU attacks)
    seconds = (2 ** entropy) / guesses_per_second

    minutes = seconds / 60
    hours = minutes / 60
    days = hours / 24
    years = days / 365

    if years < 1:
        return f"{YELLOW}{round(days,2)} days{RESET}"
    elif years < 100:
        return f"{GREEN}{round(years,2)} years{RESET}"
    elif years < 1e6:
        return f"{GREEN}{round(years/100,2)} centuries{RESET}"
    else:
        return f"{MAGENTA}{round(years/1e6,2)} million years{RESET}"

# ---------------- PASSWORD STRENGTH ----------------
def password_strength(password):
    """Simplified password strength checker."""
    score = 0
    if len(password) >= 12: score += 2
    if re.search(r"[a-z]", password): score += 1
    if re.search(r"[A-Z]", password): score += 1
    if re.search(r"[0-9]", password): score += 1
    if re.search(r"[!@#$%^&*()]", password): score += 1

    if score >= 6:
        return f"{GREEN}{BOLD}Very Strong{RESET}"
    elif score >= 4:
        return f"{YELLOW}{BOLD}Strong{RESET}"
    elif score >= 2:
        return f"{YELLOW}{BOLD}Moderate{RESET}"
    else:
        return f"{RED}{BOLD}Weak{RESET}"

# ---------------- SECURITY IMPROVEMENT ----------------
def increase_security(password, current_length):
    explanations = []

    # Add complexity based on missing criteria
    extra = ''.join(secrets.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(4))
    password += extra
    explanations.append("Added 4 random characters to increase entropy. "
                        "This makes the password harder to crack using brute-force or dictionary attacks.")

    if not re.search(r"[A-Z]", password):
        password += secrets.choice(string.ascii_uppercase)
        explanations.append("Added an uppercase letter. "
                            "Including uppercase characters prevents simple dictionary-based attacks.")

    if not re.search(r"[0-9]", password):
        password += secrets.choice(string.digits)
        explanations.append("Added a numeric digit. "
                            "Numeric characters increase the complexity, making brute-force attacks much harder.")

    if not re.search(r"[!@#$%^&*()]", password):
        password += secrets.choice("!@#$%^&*()")
        explanations.append("Added a special symbol. "
                            "Symbols greatly increase the possible combinations, mitigating rainbow table attacks.")

    protection_info = (
        f"{MAGENTA}{BOLD}Security Result:{RESET}\n"
        f"{CYAN}Password entropy increased—attackers now need exponentially more guesses.{RESET}"
    )

    return password, explanations, protection_info

# ---------------- IMPROVE PASSWORD UNTIL VERY STRONG ----------------
def improve_until_very_strong(password, length):
    """Improves the password automatically until it reaches 'Very Strong'."""
    print(f"\n{CYAN}Improving password to a very strong level...{RESET}")
    progress_bar("Improving password strength", 2, 30)  # Added progress bar to show improvement

    while password_strength(password) != f"{GREEN}{BOLD}Very Strong{RESET}":
        password, explanations, info = increase_security(password, length)

    print(f"\n{CYAN}Password is now {GREEN}{BOLD}very strong{RESET} after improvements!")
    
    # Explain what was done to improve the password
    print(f"\n{CYAN}{BOLD}Improvements Made:{RESET}")
    for explanation in explanations:
        print(f"{CYAN}{explanation}{RESET}")
    
    return password
    
# ---------------- INPUT HELPER ----------------
def yes_no_input(prompt):
    while True:
        r = input(prompt).strip().lower()
        if r in ("y", "yes"): return True
        if r in ("n", "no"): return False
        print(f"{RED}Invalid input. Use y/n.{RESET}")

# ---------------- PASSWORD ATTACKS EXPLAINED ----------------

def explain_password_defenses():
    """Explains what types of attacks a very strong password defends against."""
    print(f"\n{CYAN}{BOLD}What Does a Very Strong Password Defend Against?{RESET}")
    
    print(f"{GREEN}1. Brute-Force Attacks{RESET}: {CYAN}A strong password with a mix of letters, numbers, and symbols is harder to crack through brute-force attempts, where every possible combination is tried.")
    input(f"{CYAN}Press Enter to continue...{RESET}")
    
    print(f"\n{YELLOW}2. Dictionary Attacks{RESET}: {CYAN}Password dictionaries are used to guess passwords quickly. A very strong password containing a variety of characters significantly reduces the chance of being guessed.")
    input(f"{CYAN}Press Enter to continue...{RESET}")
    
    print(f"\n{RED}3. Rainbow Table Attacks{RESET}: {CYAN}Using precomputed tables of hash values to reverse hashes into passwords is ineffective against a strong password with proper salting and length.")
    input(f"{CYAN}Press Enter to continue...{RESET}")
    
    print(f"\n{MAGENTA}4. Social Engineering Attacks{RESET}: {CYAN}A strong password is less likely to be guessed based on personal information (like birthdates or names) that may be exploited in social engineering.")
    input(f"{CYAN}Press Enter to continue...{RESET}")
    
    print(f"\n{YELLOW}5. Phishing Attacks{RESET}: {CYAN}Although phishing relies on tricking the user, a very strong password can still make it harder for an attacker to use a stolen password across different platforms.")
    input(f"{CYAN}Press Enter to continue...{RESET}")
    
    print(f"\n{CYAN}In summary, a very strong password greatly reduces the likelihood of a successful attack, especially when used in combination with other security measures like two-factor authentication (2FA).{RESET}")
    input(f"{CYAN}Press Enter to finish...{RESET}")

# ---------------- INTERACTIVE SESSION ----------------
def start_interactive_session():
    print(f"{CYAN}{BOLD}Password Generator & Strength Checker{RESET}\n")
    
    while True:
        # Generate password
        length = int(input("Enter password length (e.g., 12 for a moderate password): "))
        password = generate_password(length)

        print(f"\n{CYAN}Generated password:{RESET} {BOLD}{password}{RESET}")
        print(f"{CYAN}Strength:{RESET} {password_strength(password)}")

        # Calculate and display entropy and attack time
        entropy = calculate_entropy(password)
        attack_time = estimate_crack_time(entropy)
        print(f"\n{CYAN}Entropy:{RESET} {entropy} bits")
        print(f"{CYAN}Estimated time to crack:{RESET} {attack_time}")
        
        # Offer to improve password if not already strong
        if password_strength(password) != f"{GREEN}{BOLD}Very Strong{RESET}":
            if yes_no_input("\nWould you like to improve this password to a very strong level? (y/n): "):
                password = improve_until_very_strong(password, length)
        
        # Show final password, strength, and attack resistance
        print(f"\n{CYAN}Final improved password:{RESET} {BOLD}{password}{RESET}")
        print(f"{CYAN}Final strength:{RESET} {password_strength(password)}")
        
        entropy = calculate_entropy(password)
        attack_time = estimate_crack_time(entropy)
        print(f"\n{CYAN}Final entropy:{RESET} {entropy} bits")
        print(f"{CYAN}Final estimated time to crack:{RESET} {attack_time}")
        
        # After final password is shown, ask if they want to learn more
        if yes_no_input("\nWant to learn more about how very strong passwords defend against particular attacks? (y/n): "):
            explain_password_defenses()

        # Ask if they want to generate a new password or finish
        if not yes_no_input("\nGenerate another password? (y/n): "):
            print(f"\n{GREEN}{BOLD}Session complete. Stay secure!{RESET}")
            break

# ---------------- RUN ----------------
start_interactive_session()
