import uvicorn
from fastapi import FastAPI
import argparse

parser = argparse.ArgumentParser(description="Run the FastAPI server.")
parser.add_argument("-p", "--port", type=int, default=8000, help="Port to run the server on. Default is 8000")
parser.add_argument("--ext", action="store_true", help="Run the server on 0.0.0.0 instead of 127.0.0.1")

args = parser.parse_args()

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Hello World"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0" if args.ext else "127.0.0.1", port=args.port)
