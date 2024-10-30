def generate_key(text, key):
    """Generate a key for Vigenère cipher based on the text length."""
    key = list(key)
    if len(text) == len(key):
        return key
    else:
        for i in range(len(text) - len(key)):
            key.append(key[i % len(key)])
    return ''.join(key)


def encrypt(text, keys):
    """Encrypt the text using multi-layer Vigenère cipher."""
    encrypted_text = text
    for key in keys:
        key = generate_key(encrypted_text, key)
        new_encrypted_text = ""
        for i in range(len(encrypted_text)):
            if encrypted_text[i].isalpha():  # Check if the character is an alphabet
                shift = ord(key[i].lower()) - ord('a')  # Get shift from the key
                shifted = ord(encrypted_text[i]) + shift

                if encrypted_text[i].islower():
                    if shifted > ord('z'):
                        shifted -= 26
                    new_encrypted_text += chr(shifted)
                elif encrypted_text[i].isupper():
                    if shifted > ord('Z'):
                        shifted -= 26
                    new_encrypted_text += chr(shifted)
            else:
                new_encrypted_text += encrypted_text[i]  # Non-alphabet characters remain unchanged
        encrypted_text = new_encrypted_text  # Update the encrypted text for the next layer
    return encrypted_text


def decrypt(text, keys):
    """Decrypt the text using multi-layer Vigenère cipher."""
    decrypted_text = text
    for key in reversed(keys):  # Reverse the keys for decryption
        key = generate_key(decrypted_text, key)
        new_decrypted_text = ""
        for i in range(len(decrypted_text)):
            if decrypted_text[i].isalpha():  # Check if the character is an alphabet
                shift = ord(key[i].lower()) - ord('a')  # Get shift from the key
                shifted = ord(decrypted_text[i]) - shift

                if decrypted_text[i].islower():
                    if shifted < ord('a'):
                        shifted += 26
                    new_decrypted_text += chr(shifted)
                elif decrypted_text[i].isupper():
                    if shifted < ord('A'):
                        shifted += 26
                    new_decrypted_text += chr(shifted)
            else:
                new_decrypted_text += decrypted_text[i]  # Non-alphabet characters remain unchanged
        decrypted_text = new_decrypted_text  # Update the decrypted text for the next layer
    return decrypted_text


def main():
    choice = input("Do you want to (E)ncrypt or (D)ecrypt? ").strip().upper()
    text = input("Enter the text: ")
    
    # Ensure keys are alphabetic only
    keys = input("Enter the keys separated by commas (alphabets only): ")
    keys = [key.strip() for key in keys.split(",")]
    
    for key in keys:
        while not key.isalpha():
            print(f"Invalid key: {key}. Please use alphabets only.")
            keys = input("Enter the keys separated by commas (alphabets only): ")
            keys = [key.strip() for key in keys.split(",")]

    if choice == 'E':
        encrypted = encrypt(text, keys)
        print("Encrypted text:", encrypted)
    elif choice == 'D':
        decrypted = decrypt(text, keys)
        print("Decrypted text:", decrypted)
    else:
        print("Invalid choice. Please choose 'E' or 'D'.")


if __name__ == "__main__":
    main()
