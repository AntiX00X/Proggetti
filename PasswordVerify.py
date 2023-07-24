import re

def check_password_strength(password):
    # Controllo la lunghezza della password
    if len(password) < 8:
        return "La password deve essere lunga almeno 8 caratteri."
    
    # Controllo la presenza di caratteri speciali
    if not re.search(r"[!@#$%^&*()_+=\-[\]{};':\"\\|,.<>/?]", password):
        return "La password deve contenere almeno un carattere speciale."
    
    # Controllo la presenza di lettere maiuscole e minuscole
    if not re.search(r"[a-z]", password) or not re.search(r"[A-Z]", password):
        return "La password deve contenere almeno una lettera maiuscola e una minuscola."
    
    # Controllo la presenza di numeri
    if not re.search(r"\d", password):
        return "La password deve contenere almeno un numero."
    
    return "La password è sufficientemente forte."

def main():
    while True:
        password = input("Inserisci una password: ")
        strength = check_password_strength(password)
        print(strength)
        print()

if __name__ == "__main__":
    main()
