import random

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def hello():
    code = f"{random.randint(1, 9999):04d}"
    return {"code": code}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
