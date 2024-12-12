from fastapi import FastAPI
from models import advice
app = FastAPI()

@app.get('/')
async def root():
    return {'message': 'Welcome to Flipvice API'}

@app.post('/create_advice')
async def create_advice(advice: advice.Advice):
    return {'message': f'advice created: {advice.model_dump()}'}