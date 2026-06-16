import requests


TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJkZXZAZXhhbXBsZS5jb20iLCJleHAiOjE3ODE3MTcwODN9.yuXYbZzCl0WDrgKR13P7oUAcF1qMJsiBOtdKWDfHM4g"

DOCUMENT_ID = (
    "98641e20-90aa-4904-9b6f-bfbf1b96c376"
)

url = (
    f"http://127.0.0.1:8000/"
    f"documents/{DOCUMENT_ID}/process"
)

headers = {
    "Authorization": f"Bearer {TOKEN}"
}

response = requests.post(
    url,
    headers=headers
)

print("Status Code:")
print(response.status_code)

print()

print("Response:")
print(response.text)