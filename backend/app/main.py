from fastapi import FastAPI

app = FastAPI(
    title="Enterprise Knowledge Assistant",
    version="1.0.0"
)

@app.get("/")
def root():
    return {
        "message": "Enterprise Knowledge Assistant API Running"
    }

@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }