name = " Harsh"
count = 1


def another():
    color = "Blue"
    # Inorder to modify the value of variable count which is defined in global scope we have to use global keyword.
    global count
    count += 3
    print(count)

    def greeting():
        # In order to modify value of color which is defined in parent function inside nested function we have to use nonlocal keyword.
        nonlocal color
        color = "red"
        # Here we are not giving any parameter inside greeting function so it is considering the value of name variable defined in global scope.
        print(name)
        print(color)

    greeting()


another()
