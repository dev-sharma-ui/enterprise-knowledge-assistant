from app.db.session import engine

try:
    with engine.connect():
        print("Database connected successfully!")
except Exception as e:
    print(f"Connection failed: {e}")