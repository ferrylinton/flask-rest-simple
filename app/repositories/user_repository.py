from .base_repository import BaseRepository

class UserRepository(BaseRepository):

    def __init__(self, db):

        BaseRepository.__init__(self, db)