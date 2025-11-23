from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def Read_Root():
    return{"Message":"hello world"}

