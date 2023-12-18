import sys
from encryption_utilities import loadPasswordFile, savePasswordFile

# The password list - Initialize it as an empty list
passwords = []

# The password file name to store the passwords to
passwordFileName = "samplePasswordFile"

# The encryption key for the Caesar cipher
encryptionKey = 16

def passwordEncrypt(text, key):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            # Encrypt only alphabetical characters
            shifted = ord(char) + key
            if char.isupper():
                encrypted_text += chr((shifted - 65) % 26 + 65)
            elif char.islower():
                encrypted_text += chr((shifted - 97) % 26 + 97)
        else:
            # Leave non-alphabetic characters unchanged
            encrypted_text += char
    return encrypted_text

def passwordDecrypt(encrypted_text, key):
    # Decryption is the same as encryption with a negative key
    return passwordEncrypt(encrypted_text, -key)

while True:
    print("What would you like to do:")
    print(" 1. Open password file")
    print(" 2. Lookup a password")
    print(" 3. Add a password")
    print(" 4. Save password file")
    print(" 5. Print the encrypted password list (for testing)")
    print(" 6. Quit program")
    print("Please enter a number (1-6)")
    choice = input()

    if choice == '1':
        # Load the password list from a file
        passwords = loadPasswordFile(passwordFileName)

    if choice == '2':
        # Lookup a password
        print("Which website do you want to lookup the password for?")
        for keyvalue in passwords:
            print(keyvalue[0])
        passwordToLookup = input()

        # Search for the website in the password list
        found = False
        for keyvalue in passwords:
            if keyvalue[0] == passwordToLookup:
                # Decrypt and display the password
                decryptedPassword = passwordDecrypt(keyvalue[1], encryptionKey)
                print(f"Password for {passwordToLookup}: {decryptedPassword}")
                found = True
                break

        if not found:
            print(f"No password found for {passwordToLookup}")

    if choice == '3':
        # Add a new password
        print("What website is this password for?")
        website = input()
        print("What is the password?")
        unencryptedPassword = input()

        # Encrypt the password and store it in the list of passwords
        encryptedPassword = passwordEncrypt(unencryptedPassword, encryptionKey)
        newPassword = [website, encryptedPassword]
        passwords.append(newPassword)
        print(f"Password for {website} added successfully.")

    if choice == '4':
        # Save the passwords to a file
        savePasswordFile(passwords, passwordFileName)
        print("Password f13ile saved successfully.")

    if choice == '5':
        # Print out the password list
        for keyvalue in passwords:
            print(', '.join(keyvalue))

    if choice == '6':
        # Quit the program
        sys.exit()

    print()
    print()
