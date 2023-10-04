class Player:
    def play(self):
       print("The Player is playing Cricket:")
class batsman(Player):
    def play(self):
       print("The Batsman is batting:")
class bowler(Player):
    def play(self):
       print("The Bowler is bowling:")
Batsman=batsman()
Bowler=bowler()
Batsman.play()
Bowler.play()


