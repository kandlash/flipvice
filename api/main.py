from fastapi import FastAPI
from routers import advices

app = FastAPI()
app.include_router(advices.router, prefix='/advices', tags=['advices'])

@app.get('/', tags=['root'])
async def root():
    return {'message': 'Welcome to Flipvice API'}