# CyberSecurity-EthicalHacking

# Company Name : CODETECH IT SOLUTIONS
# Name : AKSHAY PARMAR
# Intern ID : CT08NQI
# Domain : CYBER SECURITY & ETHICAL HACKING
# Batch Duration : 5 JAN 2025 to 5 MAR 2025 
# Mentor Name : Neela Santhosh


# Description of Task 1

The script consists of several key functions that work together to calculate, store, and verify the hash of a specified file. The hash serves as a unique fingerprint of the file's contents, allowing for easy detection of any modifications. The script is structured in a way that makes it easy to understand and extend for more complex use cases.

Key Functions

1.calculate_file_hash(file_path): This function takes the path of a file as input and computes its SHA-256 hash. It opens the file in binary mode and reads it in chunks of 4096 bytes to efficiently handle large files without consuming excessive memory. The hashlib.sha256() function is used to create a hash object, which is updated with each chunk of data read from the file. Finally, the function returns the hexadecimal representation of the computed hash.

2.store_hash(file_path, hash_value): This function is responsible for saving the computed hash to a file. It creates a new file with the same name as the original file but appends a .hash extension. The hash value is written as a string in this file, allowing for easy retrieval during integrity checks.

3. check_file_integrity(file_path): This function checks the integrity of the specified file by comparing its current hash with the stored hash. It first calculates the current hash using the calculate_file_hash function. Then, it attempts to read the stored hash from the corresponding .hash file. If the stored hash is found, the function prints both the current and stored hashes for comparison. It then checks if the two hashes match. If they do, it confirms that the file's integrity is intact; otherwise, it indicates that the file has been modified.

# Main Execution Block
The script's main execution block is where the user specifies the file to monitor. Initially, it calculates the hash of the specified file and stores it in a .hash file. After storing the hash, it calls the check_file_integrity function to verify the file's integrity. This structure allows the user to run the script multiple times to monitor the file over time.

![Screenshot 2025-02-28 161907](https://github.com/user-attachments/assets/6c4c0167-5395-4a9a-ba88-89e3377fe8de)
![Screenshot 2025-02-28 161923](https://github.com/user-attachments/assets/be35a790-63c6-455f-b15c-a9157edc4126)

