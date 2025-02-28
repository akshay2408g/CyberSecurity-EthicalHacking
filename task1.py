import hashlib

def calculate_file_hash(file_path):
    hash_sha256 = hashlib.sha256()
    with open(file_path, 'rb') as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_sha256.update(chunk)
    return hash_sha256.hexdigest()

def store_hash(file_path, hash_value):
    with open(file_path + '.hash', 'w') as hash_file:
        hash_file.write(hash_value)

def check_file_integrity(file_path):
    current_hash = calculate_file_hash(file_path)
    try:
        with open(file_path + '.hash', 'r') as hash_file:
            stored_hash = hash_file.read().strip()
            print(f"Current Hash: {current_hash}")
            print(f"Stored Hash: {stored_hash}")
            if current_hash == stored_hash:
                print("File integrity verified: No changes detected.")
            else:
                print("File integrity compromised: Changes detected!")
    except FileNotFoundError:
        print("No hash file found. Please store the hash first.")

if __name__ == "__main__":
    file_to_monitor = 'C:/Users/Akshay/Desktop/class.txt'
    
    # Step 1: Calculate and store the hash
    file_hash = calculate_file_hash(file_to_monitor)
    store_hash(file_to_monitor, file_hash)
    
    # Step 2: Check the file integrity
    check_file_integrity(file_to_monitor)
