from app.core.security import (
    hash_password,
    verify_password,
    create_access_token
)

password = "password123"

hashed = hash_password(password)

print("Hashed:")
print(hashed)

print()

print(
    "Verification:",
    verify_password(password, hashed)
)

print()

token = create_access_token("dev@gmail.com")

print("JWT:")
print(token)