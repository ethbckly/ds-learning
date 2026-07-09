class RecentUsers:
    
    def __init__(self, capacity):
        self.capacity = capacity
        self.user_list = []

    def login(self, user):
        if user in self.user_list:
            self.user_list.remove(user)
        
        if len(self.user_list) == self.capacity:
            self.user_list.pop(0)
        
        self.user_list.append(user)

        

recent = RecentUsers(3)

recent.login("alice")
recent.login("bob")
recent.login("charlie")
recent.login("bob")

print(recent.user_list)

