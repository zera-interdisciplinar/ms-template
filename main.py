from fastapi import FastAPI
import uvicorn

app = FastAPI()

#API de teste para deploy em produção, endpoint de saúde
@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/")
def root():
    return {"message": "ms-template is running"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)