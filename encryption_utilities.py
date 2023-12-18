import json

def loadPasswordFile(filename):
    try:
        with open(filename, 'r') as file:
            passwords = json.load(file)
        return passwords
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print(f"Error decoding JSON from {filename}")
        return []

def savePasswordFile(passwords, filename):
    with open(filename, 'w') as file:
        json.dump(passwords, file)