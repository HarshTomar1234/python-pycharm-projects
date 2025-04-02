# Closure is a function having access to the  scope of its parent function after the parent function has returned.

def parent_function(person, coins):
    # coins = 3

    def play_game():
        nonlocal coins
        coins -= 1

        if coins > 1:
            print("\n" + person + "has " + str(coins) + " coins left.")
        elif coins == 1:
            print("\n" + person + "has " + str(coins) + " coin left.")
        else:
            print("\n" + person + " is out of coins.")

    # If we are defining nested function than on returning inside function we don't use parenthesis after function.
    return play_game


tommy = parent_function(" Tommy ", 3)
jenny = parent_function(" Jenny ", 5)

tommy()
tommy()
tommy()

jenny()
