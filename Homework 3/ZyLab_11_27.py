# Amaan Muhammad
# PSID: 1607608

# Create Class
class Soccer:
    soccer_details = {}
    # Prompt user to input 5 jersey numbers
    def addplayers(self):
        for i in range(1,6):
            jersey = int(input("Enter player {}'s jersey number:\n".format(i)))
            rating = int(input("Enter player {}'s rating:\n".format(i) ))
            print()
            self.soccer_details[jersey] = rating
    # Menu options
    def menu(self):
        print("\nMENU")
        print("a - Add player")
        print("d - Remove player")
        print("u - Update player rating")
        print("r - Output players above a rating")
        print("o - Output roster")
        print("q - Quit")
        option = input("\nChoose an option:\n")
        return option
    # Define 'Output roster' menu option
    def Output_Roster(self):
        sorted_jersey = sorted(self.soccer_details.keys())
        print("ROSTER")
        for jersey in sorted_jersey:
            print("Jersey number: {}, Rating: {}".format(jersey,self.soccer_details[jersey]))
    # Define 'Add player' menu option
    def Add_Player(self):
        jersey = int(input("Enter a new player's jersey number: "))
        rating = int(input("Enter the player's rating: "))
        self.soccer_details[jersey] = rating
    # Define 'Remove player' menu option
    def Delete_Player(self):
        jersey = int(input("Enter a jersey number: "))
        del self.soccer_details[jersey]
    # Define 'Update player rating' menu option
    def Update_Player_Rating(self):
        jersey = int(input("Enter a jersey number: "))
        new_rating = int(input("Enter a new rating for player: "))
        self.soccer_details[jersey] = new_rating
    # Define 'Ouput players above a rating' menu option
    def Above_Rating(self):
        rating = int(input("Enter a rating"))
        sorted_jersey = sorted(self.soccer_details.keys())
        print("ABOVE {}".format(rating))
        for jersey in sorted_jersey:
            if(self.soccer_details[jersey]>rating):
                print("Jersey number: {}, Rating: {}".format(jersey,self.soccer_details[jersey]))


if __name__ == "__main__":
    # Object for class
    obj = Soccer()
    # Initiating addplayers function
    obj.addplayers()
    obj.Output_Roster()
    # Input of user from menu will go through if elif statements
    while(True):
        option = obj.menu()
        if(option == 'a'):
            obj.Add_Player()
        elif(option == 'd'):
            obj.Delete_Player()
        elif(option == 'u'):
            obj.Update_Player_Rating()
        elif(option == 'r'):
            obj.Above_Rating()
        elif(option == 'o'):
            obj.Output_Roster()
        elif(option == 'q'):
            exit()
        else:
            print("Invalid option")
