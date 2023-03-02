from app.repositories import user_repository
from .user_service import UserService


user_service = UserService(user_repository)
