from fastapi import FastAPI  

app = FastAPI(
    title="Dolphin Portfolio API",
    version="0.1.0",
)


@app.get("/")
def read_root() -> dict[str, str]:
    return {
        "message": "Dolphin Portfolio API is running"
    }


@app.get("/api/health")
def health_check() -> dict[str, str]:
    return {
        "status": "ok"
    }