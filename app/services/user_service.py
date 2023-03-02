

class UserService():

    def __init__(self, user_repository):
        self.user_repository = user_repository

    def find_user_by_id(self, id):
        return self.user_repository.find_by_id(id)

    def find(self, page, size):
        return self.user_repository.find(page, size)

    def save(self, data):
        return self.user_repository.save(data)

    def update(self, data):
        return self.user_repository.update(data)

    def delete(self, id):
        return self.user_repository.delete(id)