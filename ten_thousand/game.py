from game_logic import GameLogic

class Game:
    def __init__(self):
        self.dice_quantity = 6
        self.total_score = 0
        self.round_num = 1
    def welcome(self):
        print('Welcome to Ten Thousand')

    def default_roller(self):
        GameLogic.roll_dice(self.dice_quantity)

    def play(self, roller=GameLogic.roll_dice):
        if type(roller) == tuple:
            roller = roller
        else:
            roller = GameLogic.roll_dice(self.dice_quantity)
        print('(y)es to play or (n)o to decline')
        response = input('> ')
        if response.lower() == 'n':
            print('OK. Maybe another time')
        elif response.lower() == 'y':
            # To create an instance use GameLogic."name of static function"
            self.round_start(roller)

    def round_start(self, roller):
        self.current_dice = list(roller)
        self.saved_dice = []
        self.play_round()

    def play_round(self):
        if len(self.current_dice) <= 0:
            print('You need to roll at least one dice. Starting a new round.')
            return

        round_num = 1
        while True:
            print(f'Starting round {round_num}')
            print(f'Rolling {self.dice_quantity} dice...')
            dice = GameLogic.roll_dice(len(self.current_dice))
            print(f'*** {" ".join(str(d) for d in dice)} ***')
            if not dice:
                print('No dice left to roll. Ending round.')
                break

            print('Enter dice to keep, or (q)uit:')
            response = input().lower()
            if response == 'q':
                print(f'Thanks for playing. You earned {self.total_score} points')
                break

            dice_to_keep = []
            for kept_dice in response:
                if kept_dice.isnumeric():
                    dice_to_keep.append(int(kept_dice))

            set_aside = [self.current_dice[i-1] for i in dice_to_keep]
            self.current_dice = [d for i, d in enumerate(self.current_dice) if i+1 not in dice_to_keep]
            self.saved_dice.extend(set_aside)

            round_score = GameLogic.calculate_score(self.saved_dice)
            unbanked_score = round_score - self.total_score
            print(f'You have {unbanked_score} unbanked points and {len(self.current_dice)} dice remaining')
            while True:
                print('(r)oll again, (b)ank your points or (q)uit:')
                choice = input('> ').lower()
                if choice == 'r':
                    break
                elif choice == 'b':
                    self.bank()
                    break
                elif choice == 'q':
                    print(f'Thanks for playing. You earned {self.total_score} points')
                else:
                    print('Invalid choice. Please try again')

            round_num += 1

    def bank(self):
        round_score = GameLogic.calculate_score(self.saved_dice)
        print(f'You banked {round_score} in round {self.round_num}')
        self.total_score += round_score
        print(f'Total score is {self.total_score} points')
        self.current_dice = []
        self.saved_dice = []
        self.round_num += 1
        if self.total_score >= 10000:
            print(f'Congratulations! you won with a score of {self.total_score} points!')
            exit()
        self.play_round()


if __name__ == '__main__':
    my_game = Game()
    my_game.welcome()
    # test_roller = (3, 2, 5, 4, 3, 3)
    # my_game.play(test_roller)
    my_game.play()