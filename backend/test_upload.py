import requests


TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJkZXZAZXhhbXBsZS5jb20iLCJleHAiOjE3ODE3MTcwODN9.yuXYbZzCl0WDrgKR13P7oUAcF1qMJsiBOtdKWDfHM4g"

url = "http://127.0.0.1:8000/documents/upload"

headers = {
    "Authorization": f"Bearer {TOKEN}"
}

data = {
    "title": "Sprint 4 TXT Test",
    "visibility": "private"
}

with open(
    r"C:\Users\Asus\Desktop\sprint4_test.txt",
    "rb"
) as f:

    files = {
        "file": (
            "sprint4_test.txt",
            f,
            "text/plain"
        )
    }

    response = requests.post(
        url,
        headers=headers,
        data=data,
        files=files
    )

print("Status Code:")
print(response.status_code)

print()

print("Response:")
print(response.text)