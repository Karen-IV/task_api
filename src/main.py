from fastapi import FastAPI, Depends,Request

app = FastAPI()
@app.get('/',tags=['home'])
def home(request:Request):
    return "Home"