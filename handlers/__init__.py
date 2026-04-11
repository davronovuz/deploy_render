from aiogram import Router
from .users import user_router
from .echo import echo_router
from .groups import group_router


def setup_handlers()->Router:
    main_router=Router()
    main_router.include_router(group_router)
    main_router.include_router(user_router)
    main_router.include_router(echo_router)

    return main_router