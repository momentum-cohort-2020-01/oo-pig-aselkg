import random
import time

class Game:
    def __init__(self):
        self.player = Player("Asel")
        self.dealer = Dealer("Computer")
        self.die = Die()
    
    def game_start(self):
        print("Are you ready to play.. Enter any number to choose first player")
        userOneInput = int(input(">>>"))
        if userOneInput % 2 == 0:
            player1 = self.player.round()
    
        if userOneInput % 2 != 0:
            player2 = self.dealer.round()
           

    

class Die:
    def __init__(self):
        self.dies = 6

    def roll(self):
        roll = random.randint(1,self.dies)
        return roll

class Player:
    def __init__(self, name):
        self.name = name
        self.round_score = 0
        self.game_score = 0
        
        
    
    def __str__(self):
        return f"{self.name}"

    def round(self):
        time.sleep(0.5)
        print(f'Your turn {self.name}')
        play_again = 'r'
        self.round_score = 0
        while play_again == 'r':
            
            roll = game.die.roll()
            print(f'{self.name} rolled', roll)
            if self.game_score < 100 and roll != 1:
                self.round_score +=  roll
                print(f'{self.name} round score is ',self.round_score)
                play_again = input("Whould you like to (r)oll or (h)old")
    

            if roll == 1:
                self.round_score = 0
                self.game_score += self.round_score
                print(f'{self.name} score is {self.round_score}, game score is {self.game_score}               The Computer takes turn.')
                game.dealer.round()
            
            if self.game_score >= 100:
                print('YOU WON. Your totoal score is ',self.game_score )
                break
        else: 
            self.game_score += self.round_score
            print(f'{self.name} game score is {self.game_score}')
            game.dealer.round()
        
            

    

class Dealer:
    def __init__(self, name):
        self.name = name
        self.round_score = 0
        self.game_score = 0
        
       
    
    def __str__(self):
        return f"{self.name}"

    def round(self):
        print(f'It is {self.name} turn now')
        time.sleep(0.7)
        self.round_score = 0
        while self.round_score < 20:
            roll = game.die.roll()
            print(f'{self.name} rolled ',roll)
            self.round_score +=  roll
            print('Computer round score is ',self.round_score)
            if roll == 1:
                self.round_score = 0
                self.game_score += self.round_score
                print(f'{self.name} score is {self.round_score}, game score is {self.game_score}               The Player takes their turn.')
                game.player.round()

        
            if self.round_score >= 20:
                self.game_score += self.round_score
                if self.game_score >= 100:
                    print('Computer WON. Your totoal score is ',self.game_score )
                    break
                print('Computer game score is ',self.game_score)
                game.player.round()

            

            
        
            
        
game = Game()
game.game_start()
