import uvicorn
from fastapi import FastAPI

# from mangum import Mangum

app = FastAPI()


@app.get("/")
async def root():
    return {"message`": "Hello World!"}


# app.include_router(api_router, prefix="/api/v1")
# handler = Mangum(app)

# Will test on http://0.0.0.0:8000
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)
