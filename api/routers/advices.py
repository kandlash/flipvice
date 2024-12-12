from fastapi import APIRouter
from models.advice import Advice

router = APIRouter()

@router.post('/add')
async def post_advice(advice: Advice):
    return {'message': f'advice: {advice}'}

@router.get('/get')
async def get_advice(id: int):
    return {'message': f'advice: test'}