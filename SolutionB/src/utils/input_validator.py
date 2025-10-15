def get_valid_input(start, end):
    while True:
        try:
            user_input = int(input(f'Enter a number between {start} and {end}: '))
            if start <= user_input <= end:
                return user_input
            else:
                print(f"Invalid input. Please enter a number between {start} and {end}.")
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

if __name__ == "__main__":
    print(get_valid_input(1, 100))  
    