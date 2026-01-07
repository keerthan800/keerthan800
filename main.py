from fastapi import FastAPI

app = FastAPI()

#domdbadj
@app.get('/kkrnew')
def Read_Root(name:str):
    return{"Name":name}

