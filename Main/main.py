import art
import game_data
import random


def main():
    length = len(game_data.data)
    score = 0

    while True:

        random_1 = random.randint(0, length - 1)
        random_2 = random.randint(0, length - 1)

        if random_1 != random_2:

            first_name = game_data.data[random_1]['name']
            first_desc = game_data.data[random_1]['description']
            first_contry = game_data.data[random_1]['country']
            first_final_details = f"Compare A: {first_name}, a {first_desc}, from {first_contry}"
            print(first_final_details)

            print(art.vs)

            second_name = game_data.data[random_2]['name']
            second_desc = game_data.data[random_2]['description']
            second_contry = game_data.data[random_2]['country']
            second_final_details = f"Against B: {second_name}, a {second_desc}, from {second_contry}"
            print(second_final_details)

            user_guess = input("Who has more followers? Type 'A' or 'B': ")

            if user_guess == "A":
                if game_data.data[random_1]['follower_count'] > game_data.data[random_2]['follower_count']:
                    score += 1
                    print(f"You're right! Current score: {score}")
                else:
                    return f"Sorry, that's wrong. Final score: {score}"
            if user_guess == "B":
                if game_data.data[random_2]['follower_count'] > game_data.data[random_1]['follower_count']:
                    score += 1
                    print(f"You're right! Current score: {score}")
                else:
                    return f"Sorry, that's wrong. Final score: {score}"
        else:
            continue


if __name__ == "__main__":
    print(art.logo)
    print(main())
