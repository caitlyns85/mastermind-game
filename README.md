# Mastermind

A Python program to play the classic Mastermind game. It can:

- Generate a random secret code.
- Allow the player to guess the code.
- Provide feedback on correct colors and positions.
- Progress through multiple stages with increasing difficulty.

This repository also includes step-by-step example scripts showing each stage of the game.

---

## Features

- Interactive command-line game.
- Automatic feedback for guesses.
- Progressive stages in `stages/` for increasing difficulty.
- Step-by-step examples for each stage.

---

## File Structure
```
mastermind/
│
├── src/
│   ├── mastermind.py      # main program
│   └── stages/
│       ├── stage1.py
│       ├── stage2.py
│       ├── ...
│       └── stage9.py
│
└── README.md
```
---

## Setup and Installation

1. Clone the repository:

```bash
git clone https://github.com/caitlyns85/mastermind-game.git
cd mastermind
```

2. (Optional) Create a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

All dependencies are standard Python libraries (no external packages required).

---

## Running the Game

```bash
python3 src/mastermind.py
```

Follow the on-screen instructions to play the game. Each stage will automatically progress once the current stage is completed.

---

## Example Scripts

All `stage1.py` – `stage9.py` scripts are in `src/stages/`. They demonstrate:

- Game setup for each stage
- Guess validation
- Feedback on guesses
- Stage progression

Run a script individually to see how each stage works:

```bash
python3 src/stages/stage1.py
```

---

## Notes

- All scripts are compatible with Python 3.
- Ensure files are in the correct folder structure for the program to run.
- No external dependencies are required.

