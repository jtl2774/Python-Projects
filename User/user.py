class User: 
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        # default attributes 
        self.is_rewards_member = False
        self.gold_card_points = 0

    def display_info(self):
        print(f"First Name: {self.first_name}")
        print(f"Last Name: {self.last_name}")
        print(f"Email: {self.email}")
        print(f"Age: {self.age}")
        print(f"Member: {self.is_rewards_member}")
        print(f"Points: {self.gold_card_points}")
    
    def enroll(self):
        self.is_rewards_member = True
        self.gold_card_points = 200
        return self

    def spend_points(self,amount):
        self.gold_card_points = self.gold_card_points - amount

user_1 = User("Sadie", "Flick", "sflick@codingdojo.com", 99)
user_2 = User("Leslie", "Crowe", "lcrowe@codingdojo.com", 39)
user_1.display_info()
user_2.enroll().spend_points(80)
user_2.display_info()

    