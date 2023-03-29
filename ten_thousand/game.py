import sys

from game_logic import GameLogic

class Game:

    def __init__(self):
        self.total_score = 0
        self.round_num = 1
        self.unbanked_score = []
        self.saved_dice = []
        self.current_dice = []

    def welcome(self):
        print('Welcome to Ten Thousand')
        print('(y)es to play or (n)o to decline')
        response = input('> ')
        if response.lower() == 'n':
            print('OK. Maybe another time')
            # game_exit()

        elif response.lower() == 'y':
            # To create an instance use GameLogic."name of static function"
            self.round_start()

    @staticmethod
    def game_exit():
        sys.exit()

    def round_start(self):
        self.play_round()

        # TODO: Save for possible use in zilch function
        # if len(self.current_dice) = 0:
        #     print('HOT DICE! Roll again!')
        #     return

    def play_round(self):
        while True:
            print(f'Starting round {self.round_num}')
            # Number of dice to be rolled equals 6 - saved dice
            dice_roll = GameLogic.roll_dice(6 - len(self.saved_dice))
            print(f'*** {" ".join(str(each_di_value) for each_di_value in dice_roll)} ***')
            print('Enter dice to keep, or (q)uit:')
            response = input().lower()
            if response == 'q':
                print(f'Thanks for playing. You earned {self.total_score} points')
                sys.exit()
            else:
                self.dice_to_keep(self, response)

    @staticmethod
    def dice_to_keep(self, response):
        for chosen_character in response:
            if chosen_character.isnumeric():
                self.saved_dice.append(int(chosen_character))
        # print(f'Your unbanked score is {self.unbanked_score} points')
        print('(r)oll again, (b)ank your points or (q)uit:')
        choice = input('> ').lower()
        if choice == 'r':
            return
        #     break
        elif choice == 'b':
            self.bank()
            return
            # break
        elif choice == 'q':
            print(f'Thanks for playing. You earned {self.total_score} points')
            exit()
        else:
            print('Invalid choice. Please try again')


    def bank(self):
        dice_tuple = tuple(self.saved_dice)
        unbanked_score = GameLogic.calculate_score(dice_tuple)
        print(f'You banked {unbanked_score} in round {self.round_num}')
        self.total_score += unbanked_score
        print(f'Total score is {self.total_score} points')
        self.round_num += 1
        self.saved_dice = []
        if self.total_score >= 10000:
            print(f'Congratulations! you won with a score of {self.total_score} points!')
            exit()

# TODO Need to finish unbanked score
    # def unbanked_round_score(self):
    #     self.unbanked_score = self.round_score - self.total_score
    #     print(f'You have {self.unbanked_score} unbanked points and {len(self.current_dice)} dice remaining')


if __name__ == '__main__':
    my_game = Game()
    my_game.welcome()
    # test_roller = (3, 2, 5, 4, 3, 3)
    # my_game.play(test_roller)
    # my_game.play()
    # pass