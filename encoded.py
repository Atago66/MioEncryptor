import random
import base64

def generate_key(text, key):
    """Generate a key for Vigenère cipher based on the text length."""
    key = list(key)
    if len(text) == len(key):
        return key
    else:
        for i in range(len(text) - len(key)):
            key.append(key[i % len(key)])
    return ''.join(key)


def apply_additive_shift(text, shift):
    """Apply a simple Caesar shift to each character of the text."""
    shifted_text = ""
    for char in text:
        if char.isalpha():
            shifted = ord(char) + shift
            if char.islower():
                if shifted > ord('z'):
                    shifted -= 26
                elif shifted < ord('a'):
                    shifted += 26
            elif char.isupper():
                if shifted > ord('Z'):
                    shifted -= 26
                elif shifted < ord('A'):
                    shifted += 26
            shifted_text += chr(shifted)
        else:
            shifted_text += char  # Non-alphabet characters remain unchanged
    return shifted_text


def encrypt(text, keys, shift_layers=None, encode_output=True):
    """Encrypt the text using multi-layer Vigenère cipher with optional shift layers and encoding."""
    encrypted_text = text
    for i, key in enumerate(keys):
        # Apply additive shift if specified
        if shift_layers and i in shift_layers:
            encrypted_text = apply_additive_shift(encrypted_text, shift_layers[i])

        # Vigenère encryption
        key = generate_key(encrypted_text, key)
        new_encrypted_text = ""
        for j in range(len(encrypted_text)):
            if encrypted_text[j].isalpha():
                shift = ord(key[j].lower()) - ord('a')
                shifted = ord(encrypted_text[j]) + shift
                if encrypted_text[j].islower():
                    if shifted > ord('z'):
                        shifted -= 26
                    new_encrypted_text += chr(shifted)
                elif encrypted_text[j].isupper():
                    if shifted > ord('Z'):
                        shifted -= 26
                    new_encrypted_text += chr(shifted)
            else:
                new_encrypted_text += encrypted_text[j]
        encrypted_text = new_encrypted_text

    # Final Base64 encoding
    if encode_output:
        encrypted_text = base64.b64encode(encrypted_text.encode()).decode()
    
    return encrypted_text


def is_base64_encoded(data):
    """Check if a string is Base64 encoded."""
    try:
        if base64.b64encode(base64.b64decode(data)).decode() == data:
            return True
    except Exception:
        return False
    return False

def decrypt(text, keys, shift_layers=None, decode_input=True):
    """Decrypt the text using multi-layer Vigenère cipher with optional shift layers and decoding."""
    # Base64 decoding if encoded during encryption
    if decode_input and is_base64_encoded(text):
        text = base64.b64decode(text.encode()).decode()
    
    decrypted_text = text
    for i, key in reversed(list(enumerate(keys))):  # Reverse the order of keys for decryption
        # Vigenère decryption
        key = generate_key(decrypted_text, key)
        new_decrypted_text = ""
        for j in range(len(decrypted_text)):
            if decrypted_text[j].isalpha():
                shift = ord(key[j].lower()) - ord('a')
                shifted = ord(decrypted_text[j]) - shift
                if decrypted_text[j].islower():
                    if shifted < ord('a'):
                        shifted += 26
                    new_decrypted_text += chr(shifted)
                elif decrypted_text[j].isupper():
                    if shifted < ord('A'):
                        shifted += 26
                    new_decrypted_text += chr(shifted)
            else:
                new_decrypted_text += decrypted_text[j]
        decrypted_text = new_decrypted_text

        # Apply reverse additive shift if specified
        if shift_layers and i in shift_layers:
            decrypted_text = apply_additive_shift(decrypted_text, -shift_layers[i])

    return decrypted_text


def main():
    choice = input("Do you want to (E)ncrypt or (D)ecrypt? ").strip().upper()
    text = input("Enter the text: ")
    
    # Get the keys for multiple layers
    keys = input("Enter the keys separated by commas (alphabets only): ")
    keys = [key.strip() for key in keys.split(",")]
    
    # Optional: Define additive shifts
    shift_layers = {}
    shift_input = input("Enter additive shifts for layers (e.g., 0:2,1:3) or leave empty: ")
    if shift_input:
        shift_layers = {int(k): int(v) for k, v in (pair.split(":") for pair in shift_input.split(","))}

    if choice == 'E':
        encrypted = encrypt(text, keys, shift_layers)
        print("Encrypted text:", encrypted)
    elif choice == 'D':
        decrypted = decrypt(text, keys, shift_layers)
        print("Decrypted text:", decrypted)
    else:
        print("Invalid choice. Please choose 'E' or 'D'.")


if __name__ == "__main__":
    main()
