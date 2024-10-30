def generate_key(text, key):
    """Generate a key for Vigenère cipher based on the text length."""
    key = list(key)
    if len(text) == len(key):
        return key
    else:
        for i in range(len(text) - len(key)):
            key.append(key[i % len(key)])
    return ''.join(key)


def encrypt(text, key):
    """Encrypt the text using Vigenère cipher."""
    encrypted_text = ""
    key = generate_key(text, key)
    for i in range(len(text)):
        if text[i].isalpha():  # Check if the character is an alphabet
            shift = ord(key[i].lower()) - ord('a')  # Get shift from the key
            shifted = ord(text[i]) + shift

            if text[i].islower():
                if shifted > ord('z'):
                    shifted -= 26
                encrypted_text += chr(shifted)
            elif text[i].isupper():
                if shifted > ord('Z'):
                    shifted -= 26
                encrypted_text += chr(shifted)
        else:
            encrypted_text += text[i]  # Non-alphabet characters remain unchanged
    return encrypted_text


def decrypt(text, key):
    """Decrypt the text using Vigenère cipher."""
    decrypted_text = ""
    key = generate_key(text, key)
    for i in range(len(text)):
        if text[i].isalpha():  # Check if the character is an alphabet
            shift = ord(key[i].lower()) - ord('a')  # Get shift from the key
            shifted = ord(text[i]) - shift

            if text[i].islower():
                if shifted < ord('a'):
                    shifted += 26
                decrypted_text += chr(shifted)
            elif text[i].isupper():
                if shifted < ord('A'):
                    shifted += 26
                decrypted_text += chr(shifted)
        else:
            decrypted_text += text[i]  # Non-alphabet characters remain unchanged
    return decrypted_text


def main():
    choice = input("Do you want to (E)ncrypt or (D)ecrypt? ").strip().upper()
    text = input("Enter the text: ")
    
    # Ensure the key is alphabetic only
    key = input("Enter the key (alphabets only): ")
    while not key.isalpha():
        print("Invalid key. Please use alphabets only.")
        key = input("Enter the key (alphabets only): ")

    if choice == 'E':
        encrypted = encrypt(text, key)
        print("Encrypted text:", encrypted)
    elif choice == 'D':
        decrypted = decrypt(text, key)
        print("Decrypted text:", decrypted)
    else:
        print("Invalid choice. Please choose 'E' or 'D'.")


if __name__ == "__main__":
    main()
