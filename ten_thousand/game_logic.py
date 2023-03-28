


from collections import Counter
import random

class GameLogic:
    @staticmethod
    def calculate_score(dice):
        """
        Calculate the score for a dice roll according to the rules of the game
        Args: dice: a tuple of integers
        Return: An integer representing the roll's score
        """
        found_ones = found_fives = False

        # Create a dictionary with the counts of each die value
        dice_counts = Counter(dice)
        # Overall score
        score = 0

        # If the length of dice counts equals 3 and all count equals 2 for our dice counts values, we return 1500
        if len(dice_counts) == 3 and all(count == 2 for count in dice_counts.values()):
            return 1500
        # If length of dice counts equals 6, we return 1500
        if len(dice_counts) == 6:
            return 1500

        # check for 3 of a kind and three 1s and a 5
        # For the value and count in dice counts items, if the count equals 3 and value equals 5, we set found fives to true and multiply value * 100 and add to score
        for value, count in dice_counts.items():
            if count == 3:
                if value == 5:
                    found_fives = True
                score += value * 100
                # If our value equals one, we set found ones to true and multiply our score * 10
                if value == 1:
                    found_ones = True
                    score *= 10
                    # If our value equals five, we set found fives to true, and add 50 to our score
                    if value == 5:
                        found_fives = True
                        score += 50

        # Check for 4 of a kind by counting the occurrences of each number and returning the product of the number that appears four times and 4, or 0 if no number appears four times.
        for value, count in dice_counts.items():
            # Check if the count is equal to 4
            if count == 4:
                # If the value is equal to 5, we add 200 to the score
                if value == 5:
                    score += 200
                # If the value is not equal to 5, we multiply value * 100 and add it to our score and multiply our score * 2
                if value != 5:
                    score += value * 100
                    score *= 2
                # If the value is equal to 1, we set found ones to true and multiply our score * 10
                if value == 1:
                    found_ones = True
                    score *= 10

        # Check for 5 of a kind by counting the occurrences of each number and returning the product of the number that appears five times and 5, or 0 if no number appears five times.
        for value, count in dice_counts.items():
            # If the count is equal to 5...
            if count == 5:
                # If our value is equal to 5, we add 200 points to score
                if value == 5:
                    score += 200
                # If our value is not equal to 5, we multiply our value * 100 and add it to our score and multiply the score * 3
                if value != 5:
                    score += value * 100
                    score *= 3
                # If our value is equal to 1, we set found ones to true and multiply our score * 10
                if value == 1:
                    found_ones = True
                    score *= 10

        # Check for 6 of a kind by counting the occurrences of each number and returning the product of the number that appears six times and 6, or 0 if no number appears six times.
        for value, count in dice_counts.items():
            # If the count is equal to 6...
            if count == 6:
                # If our value is equal to 6, we add 200 points to score
                if value == 6:
                    score += 200
                # If our value is not equal to 6, we multiply our value * 100 and add it to our score and multiply the score * 4
                if value != 6:
                    score =+ value * 100
                    score *= 4
                # If our value is equal to 1, we set found ones to true and multiply our score * 10
                if value == 1:
                    found_ones = True
                    score *= 10

        # Check for a single die with a value of 5 and add 50 points to score:
        if dice_counts.get(5, 0) == 1:
            score += 50
        # Check for two dice with a value of 5 and add 100 points to score:
        elif dice_counts.get(5, 0) == 2:
            score += 100

        # Check for individual 1s and 5s
        # If the count of 1s is less than 3 and the count of 5s is less than 1, then the score for individual 1s, and 5s, is 0
        # Otherwise the score for the individual 1s is 100 times the count of 1s and the score for individual 5s is 50 times the count of the 5s
        if not found_ones:
            score += min(dice_counts.get(1, 0), 3) * 100
        if not found_fives:
            score += (dice_counts.get(5, 0) - min(dice_counts.get(5, 0), 3)) * 50

        # Returning the final score
        return score

    @staticmethod
    def roll_dice(num_dice):
        """
        Roll a specified number of dice
        num_dice: An integer representing the number of dice to roll
        Returns: A list of integers representing the values rolled
        """
        # If not an instance of num_dice, int, or num_dice is less than 1
        if not isinstance(num_dice, int) or num_dice < 1:
            # Raising Value Error
            raise ValueError("Number of dice must be a positive integer")

        # Roll the dice using random and randint in a range of 1 - 6 and return the values in range of number of dice rolled
        return [random.randint(1, 6) for _ in range(num_dice)]

if __name__ == '__main__':
    pass
