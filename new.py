import random

class Game:
    def __init__(self):
        self.player = Player("Player")
        self.dealer = Dealer("Computer")
        self.die = Die()
    
    def game_start(self):
        print("Enter any number to choose first player ")
        userOneInput = int(input(">>>"))
        if userOneInput % 2 == 0:
            # print("Player 1 starts the game")
            self.player.round()
        else: 
            self.dealer.round()

    

class Die:
    def __init__(self):
        self.die = random.randint(1,6)
    def __str__(self):
        return f"{self.die}"

class Player:
    def __init__(self, name):
        self.name = name
        self.round_score = 0
        self.game_score = 0
        self.dealer = Dealer("Player")
    
    def __str__(self):
        return f"{self.name}"

    def round(self):
        print(f'Your turn {self.name}')
        anotherGo = 'R'
        round_score = 0
        while anotherGo == 'R':
            die = random.randint(1,6)
            print('You rolled ',die)
            if die == 1:
                self.round_score= 0
                self.game_score = 0
                print('The other player takes their turn.')
                print('Press Enter to continue')
                # self.dealer.round()
            else:
                self.round_score +=  die
                self.game_score += self.round_score
                print('Your score this turn is ',self.round_score)
                print('Your totoal score is ',self.game_score)
            if self.game_score>= 100:
                return self.game_score

    

class Dealer:
    def __init__(self, name):
        self.name = name
        self.round_score = 0
        self.game_score = 0
        # self.player = Player("Player")
    
    def __str__(self):
        return f"{self.name}"

    def round(self):
        print(f'Your turn {self.name}')
        anotherGo = 'R'
        round_score = 0
        while anotherGo == 'R':
            die = random.randint(1,6)
            print('You rolled ',die)
            if die == 1:
                self.round_score= 0
                self.game_score = 0
                print('The other player takes their turn.')
                print('Press Enter to continue')
                # self.player.round()
            else:
                self.round_score +=  die
                self.game_score += self.round_score
                print('Your score this turn is ',self.round_score)
                print('Your totoal score is ',self.game_score)
            if self.game_score>= 100:
                return self.game_score

        


game = Game()
game.game_start()
