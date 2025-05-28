def caeser_encrypt(text, shift):
    encrypted = ""
    for char in text:
        if char.isalpha():
            offset = ord('A') if char.isupper() else ord('a')
            encrypted += chr((ord(char) - offset + shift) % 26 + offset)
        else:
            encrypted += char
    return encrypted

def caeser_decrypt(text, shift):
    return caeser_encrypt(text, -shift)

def main():
    print("Caeser Cipher Tool")
    choice = input("Do you want to (E)ncrypt or (D)ecrypt? ").strip().upper()

    if choice not in ['E', 'D']:
        print("Invalid choice. Please enter 'E' to encrypt or 'D' to decrypt.")
        return
    
    message = input("Enter your message: ")
    try:
        shift = int(input("Enter the shift value (e.g., 3): "))
    except ValueError:
        print("Invalid shift value. Must be an integer.")
        return
    
    if choice == 'E':
        result = caeser_encrypt(message, shift)
        print(f"Encrypted message: {result}")
    else:
        result = caeser_decrypt(message, shift)
        print(f"Decrypted message: {result}")

if __name__ == "__main__":
    main()