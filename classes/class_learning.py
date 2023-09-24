class User:
    def __init__(self, user_id, name):
        self.id = user_id
        self.name = name
        self.followers = 0
        self.following = 0

    def print_name(self):
        print(self.name)

    def follow(self, user):
        user.followers += 1
        self.following += 1

user_1 = User("001","rave")
user_2 = User("002", "fid")

user_1.follow(user_2)
user_2.follow(user_1)
user_1.print_name()
print(user_1.following)
print(user_1.followers)
