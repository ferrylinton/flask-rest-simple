from app import connection_pool as db
from .user_repository import UserRepository


user_repository = UserRepository(db)
