from DataForProjects.DataFile import social_media_profiles
import random
score = 0

should_continue = True
account_b = random.choice(social_media_profiles)

while should_continue:
    account_a = account_b
    account_b = random.choice(social_media_profiles)
    if account_a == account_b:
        account_b = random.choice(social_media_profiles)

    def check_answer(guess,a,b):
        if a>b:
            return guess == 'a'
        else:
            return guess == 'b'

    def format_account(account):
        account_name = account['name']
        account_description = account['description']
        account_country = account['country']
        return f"{account_name} a {account_description}, from {account_country}"

    print(f"Compare A : {format_account(account_a)}")
    print("VS")
    print(f"Compare B : {format_account(account_b)}")

    guess = input("Who has more follower's A or B ? : \n").lower()
    is_correct = check_answer(guess,account_a['follower_count'],account_b['follower_count'])
    if is_correct:
        score+=1
        print(f"You are right ! current score {score}")
    else:
        should_continue = False
        print(f"Wrong pall ! current score {score}")

