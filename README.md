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

# OUTPUT of TASK 1

- As you can see my hash are changing when I change my txt files

![Screenshot 2025-02-28 161907](https://github.com/user-attachments/assets/6c4c0167-5395-4a9a-ba88-89e3377fe8de)
![Screenshot 2025-02-28 161923](https://github.com/user-attachments/assets/be35a790-63c6-455f-b15c-a9157edc4126)


# Description of Task 2

Python script is a basic web application vulnerability scanner designed to test for two common types of vulnerabilities: SQL Injection (SQLi) and Cross-Site Scripting (XSS). This script serves as a foundational tool for security testing, allowing users to identify potential weaknesses in web applications. Below is a detailed explanation of the code and its components.

# Class Definition
The script defines a class called WebVulnScanner, which encapsulates the functionality of the scanner. The class is initialized with a target URL, which is the web application that will be tested for vulnerabilities.

# Initialization
In the __init__ method, the class takes a target_url parameter and initializes two lists of payloads:

# SQL Injection Payloads: 
These are crafted strings that are commonly used to exploit SQL injection vulnerabilities. They include variations that attempt to manipulate SQL queries by injecting conditions that always evaluate to true (e.g., "' OR '1'='1"). The goal is to see if the application improperly handles these inputs, potentially allowing an attacker to access or manipulate the database.
# Cross-Site Scripting Payloads:
These payloads are designed to test for XSS vulnerabilities. They include JavaScript code snippets that, if executed in the browser, would trigger alerts or other actions. For example, "<script>alert('XSS')</script>" is a classic XSS payload that attempts to inject a script tag into the application.

# Testing Methods
The class contains two primary methods for testing vulnerabilities:

test_sqli Method: This method iterates over the list of SQLi payloads. For each payload, it constructs a URL by appending the payload to the target URL and sends a GET request using the requests library. The response is then checked for the presence of the word "error" (in lowercase). If the response does not contain "error," it indicates a potential SQL injection vulnerability, and the script prints a message with the corresponding payload.
test_xss Method: Similar to the SQLi method, this method iterates over the XSS payloads. It sends a GET request for each payload and checks if the payload is present in the response text. If it is found, this suggests that the application reflects the input back to the user without proper sanitization, indicating a potential XSS vulnerability.
Running the Scanner
The run method orchestrates the scanning process. It prints a message indicating the start of the scan and calls both the test_sqli and test_xss methods to perform the vulnerability checks. As you can see I got Potential Vulnerability for XSS in my target URL.

# Main Execution Block
The script includes a standard Python entry point (if __name__ == "__main__":). This block prompts the user to input a target URL, creates an instance of the WebVulnScanner class with the provided URL, and calls the run method to initiate the scanning process.

![Screenshot 2025-03-01 144909](https://github.com/user-attachments/assets/c3cee275-d28b-48ba-a1e3-c1cf85e6810a)

