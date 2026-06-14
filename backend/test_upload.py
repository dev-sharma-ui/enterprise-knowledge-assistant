import requests


TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJkZXZAZXhhbXBsZS5jb20iLCJleHAiOjE3ODE0ODM5ODB9.yZheccRjg6d4YHkSXGPg7PRDATrzalUvDj1tETm83GY"

url = "http://127.0.0.1:8000/documents/upload"

headers = {
    "Authorization": f"Bearer {TOKEN}"
}

data = {
    "title": "Operating System Notes",
    "visibility": "private"
}

with open(r"C:\Users\Asus\Downloads\OS_Full_Notes.pdf", "rb") as f:

    files = {
        "file": (
            "OS_Full_Notes.pdf",
            f,
            "application/pdf"
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