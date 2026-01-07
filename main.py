from fastapi import FastAPI

app = FastAPI()

#domdbadj
@app.get('/kkr2')
def Read_Root(name:str):
    return{"Name":name}

