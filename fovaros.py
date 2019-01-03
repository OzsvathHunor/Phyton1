import random

def main():
    country_capital_dict = {"Slovenia": "Ljubljana", "Croatia": "Zagreb", "Austria": "Vienna"}

    while True:
        random_num = random.randint(0, 2)
        selected_country = country_capital_dict.keys()[random_num]

        guess = raw_input("What is the capital of %s? " % selected_country)

        if is_guess_correct(guess, selected_country, country_capital_dict):
            print "Correct! The capital of %s is indeed %s." % (selected_country,guess)
        else:
            print "Sorry, you are wrong. The capital of %s is not %s." % (selected_country, guess)

        again = raw_input("Would you like to continue this game? (yes/no) ")
        if again == "no":
            break

    print "END"
    print "_________________________"


def is_guess_correct(user_guess, country, cc_dict):
    capital = cc_dict[country]
    if user_guess == capital:
        return True
    else:
        return False


if __name__ == "__main__":
    main()