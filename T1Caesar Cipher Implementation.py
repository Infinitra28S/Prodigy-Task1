def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char  # keep punctuation/numbers
    return result

def decrypt(text, shift):
    return encrypt(text, -shift)

# === Main Program ===
choice = input("Encrypt or Decrypt? (e/d): ").lower()
message = input("Enter your message: ")
shift = int(input("Enter shift value (e.g. 3): "))

if choice == 'e':
    encrypted = encrypt(message, shift)
    print("🔐 Encrypted message:", encrypted)

elif choice == 'd':
    decrypted = decrypt(message, shift)
    print("🔓 Decrypted message:", decrypted)

else:
    print("❌ Invalid choice.")


# This code implements a simple Caesar cipher for text encryption and decryption.
