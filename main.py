from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def hello(name: str = "Recruto", message: str = "Давай дружить!"):
    return {f"Hello {name}! {message}!"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
