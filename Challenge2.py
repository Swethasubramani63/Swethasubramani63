class player:
   def play(self):
      print("The player is playing cricket")
   class Batsman(player):
          def play (self):
            print("The Batsman is batting.")
class Bowler (player):
     def play (self):
         print("The Bowler is bowling.")
  #creating objects of the

  Batsman and Bowler classes
  batsman = Batsman()
  bowler = Bowler()
  #calling the play() method 
  for each object  
  batsman.play()
  bowler.play()
