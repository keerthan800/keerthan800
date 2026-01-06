from fastapi import FastAPI

app = FastAPI()

@app.get('/kkr')
def Read_Root(name:str):
    return{"Name":name}

