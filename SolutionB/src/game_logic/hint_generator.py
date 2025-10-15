def provide_hint(guess,actual_number):
    if guess > actual_number:
        return "Your guess is Too high"
    elif guess < actual_number:
        return "Your guess is Too low"
    else:
        return "Correct"
