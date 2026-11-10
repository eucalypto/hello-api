from fastapi import FastAPI

app = FastAPI()

@app.get("/hello")
def hello():
	return {"message": "Hello from Docker!"}

@app.get("/health")
def health():
	return {"status": "ok"}
