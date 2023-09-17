# define the base class player
class Player:
    def play(self):
        print("The player is playing cricket.")
# define the Derived class Batsman 
class Batsman(Player):
    def play(self):
        print("The batsman is batting.")
# define the Derived class Bowler
class Bowler(Player):
    def play(self):
        print("The bowler is bowling.")
# Create objects of both the Batsman and Bowler classes
batsman = Batsman()
bowler = Bowler()
# Call the play() method for each object
batsman.play()
bowler.play()