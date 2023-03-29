from sys import exit

from game_logic import GameLogic

class Game:

    def __init__(self):
        self.total_score = 0
        self.round_num = 1
        self.unbanked_score = 0
        self.saved_dice = []
        self.current_dice = []

    def welcome(self):
        print('Welcome to Ten Thousand')
        print('(y)es to play or (n)o to decline')
        response = input('> ')
        if response.lower() == 'n':
            self.game_exit('OK. Maybe another time')

        elif response.lower() == 'y':
            # To create an instance use GameLogic."name of static function"
            self.play_round()

    @staticmethod
    def game_exit(message):
        exit(message)


    def play_round(self):
        while True:
            print(f'Starting round {self.round_num}')
            # Number of dice to be rolled equals 6 - saved dice
            dice_roll = GameLogic.roll_dice(6 - len(self.saved_dice))
            print(f'*** {" ".join(str(each_di_value) for each_di_value in dice_roll)} ***')
            print('Enter dice to keep, or (q)uit:')
            response = input().lower()
            if response == 'q':
                self.game_exit(f'Thanks for playing. You earned {self.total_score} points')
            else:
                self.dice_to_keep(self, response)

    @staticmethod
    def dice_to_keep(self, response):
        for chosen_character in response:
            if chosen_character.isnumeric():
                self.saved_dice.append(int(chosen_character))
        dice_tuple = tuple(self.saved_dice)
        self.unbanked_score = GameLogic.calculate_score(dice_tuple)
        print(f'Your unbanked score is {self.unbanked_score} points')
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
            self.game_exit(f'Thanks for playing. You earned {self.total_score} points')
        else:
            print('Invalid choice. Please try again')


    def bank(self):
        print(f'You banked {self.unbanked_score} in round {self.round_num}')
        self.total_score += self.unbanked_score
        print(f'Total score is {self.total_score} points')
        self.round_num += 1
        self.saved_dice = []
        if self.total_score >= 10000:
            print(f'Congratulations! you won with a score of {self.total_score} points!')
            exit()

    # TODO Need to finish unbanked score
    # @staticmethod
    # def unbanked_round_score(self):
        # dice_tuple = tuple(self.saved_dice)
        # self.unbanked_score = GameLogic.calculate_score(dice_tuple)
        # print(f'You have {self.unbanked_score} unbanked points and {len(self.current_dice)} dice remaining')
        # pass

    # TODO: zilch function - No points for round, and round is over
    # Round ends = increase the round by 1
    # No points for round, and round is over
    # zero out the shelf (round score set to 0)
    # reset next dice roll to 6 dice

    # TODO: Should allow user to continue rolling with 6 new dice when all dice have scored in current turn.

        # print('HOT DICE! Roll again!')
        # return

    ## TODO: handle when cheating occurs.
    # Or just typos.
    # E.g. roll = [1,3,5,2] and user selects 1, 1, 1, 1, 1, 1
    # Should allow user to continue rolling with 6 new dice when all dice have scored in current turn.

    # validate the dice that are put aside are actually in the roll
    # run the validated roll through calculate score




if __name__ == '__main__':
    try:
        my_game = Game()
        my_game.welcome()
    except KeyboardInterrupt:
        my_game.game_exit(' Ctrl C Detected')
    # test_roller = (3, 2, 5, 4, 3, 3)
    # my_game.play(test_roller)
    # my_game.play()
    # pass