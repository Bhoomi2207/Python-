for c in range(1, 5):
    if c == 1:
        n = input("Are you tired? ")
        if n == 'yes':
            print("You did not finish the race")
            break
        elif n == 'no':
            print("Are you tired?")
            continue
    elif c == 5:
        print("Congratulation")
