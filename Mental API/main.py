import uvicorn

from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def index():
    return{'message': 'Hello, World'}

@app.get('/Welcome')
def get_name(name: str):
    return{'Welcome to Mental Health Website': f'{name}'}

if __name__ == '__main__':
    uvicorn.run('main:app', host='127.0.0.1', port=8000)
    