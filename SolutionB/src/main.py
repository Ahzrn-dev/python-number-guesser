from src.utils.input_validator import get_valid_input
from src.game_logic.number_generator import generate_number 
from src.game_logic.hint_generator import provide_hint
from src.game_logic.scorer import scorer


def main():
    actual_number = generate_number(1, 100)  
    score = scorer()
    while True:
        user_input = get_valid_input(1, 100)
        if user_input > actual_number:
            print(provide_hint(user_input, actual_number))
            score.decrease_score()
        elif user_input < actual_number:
            print(provide_hint(user_input, actual_number))
            score.decrease_score()
        else:
            print(provide_hint(user_input, actual_number))
            print(f"Your score is {score.got_score()}")
            break
    

if __name__ == "__main__":
    main()  
    