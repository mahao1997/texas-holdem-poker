class Engine():
    def __init__(self, ):
        self.users = []
    def add_user(self, user):
        self.users.append(user)
    def login_user(self, user):
        for it in self.users:
            if user == it:
                return True
        return False
game_engine = Engine()
