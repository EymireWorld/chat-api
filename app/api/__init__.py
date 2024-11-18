from fastapi import APIRouter

from app.api.auth.router import router as api_router


router = APIRouter(prefix='/api')
router.include_router(
    api_router,
    prefix='/auth',
    tags=['Auth'],
)
