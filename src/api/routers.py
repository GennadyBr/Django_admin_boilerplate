import requests
from fastapi import APIRouter

from src.core.logger import logger
from src.db.fake_data import _create_fake_data

router = APIRouter()


@router.get('/create_fake_data')
async def create_fake_data() -> dict:
    """Create fake data"""
    logger.info('Create fake data')
    await _create_fake_data()
    return {'message': 'Create fake data'}


@router.get('/hello')
async def hello() -> dict:
    """Hello world"""
    logger.info('Hello World')
    return {'message': 'Hello World'}


@router.get('/request')
async def request() -> str:
    """Request example"""
    response = requests.get('https://google.com')
    result = f'Google Response: {response.status_code}'
    logger.info(result)
    return result


@router.get('/raise_error')
async def raise_error() -> str:
    """Raise Error"""
    try:
        div_zero = 1 / 0
    except ZeroDivisionError as error:
        logger.exception('Divide by zero error')
        return str(error)
    return str(div_zero)
