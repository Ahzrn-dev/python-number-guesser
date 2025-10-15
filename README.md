# Number Guesser 🎯

**Number Guesser** is a Python game where the player tries to guess a randomly chosen number between 1 and 100. The project offers two implementations: a simple script and a modular version for easier maintenance and scalability.

---

## Features ✨

- Guess a number between 1 and 100
- Score starts at 100 and decreases by 10 for each incorrect guess
- Provides hints if the guess is too high or too low
- Quit anytime by typing `q`
- Two implementations:
  - **Solution A:** Single-file, straightforward version
  - **Solution B:** Modular version with separate modules for:
    - Input validation
    - Random number generation
    - Hint generation
    - Score management

---

## How to Run ▶️

### Solution A (Simple)
```bash
python solutionA.py
```

### Solution B (Modular)
```bash
python main.py
```

> ⚠️ Ensure that the folder structure and modules are correctly set up before running Solution B.

---

## Gameplay 🕹️

1. Run the script
2. Try to guess the randomly chosen number
3. Receive hints if your guess is too high or too low
4. Score starts at 100 and decreases by 10 for each wrong guess
5. Type `q` to quit at any time

---

## Project Structure (for Solution B)

```
src/
├─ game_logic/
│  ├─ number_generator.py
│  ├─ hint_generator.py
│  └─ scorer.py
└─ utils/
   └─ input_validator.py
main.py
```

---

## Technologies 🛠️

- Python 3.x
- Modular programming
- Object-oriented design principles (for Solution B)

---

## Author

**Ahrzn-dev**

