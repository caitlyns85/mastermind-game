# Mastermind Game (Python)

A console-based implementation of the classic Mastermind game in Python. 

## Game Overview

Mastermind is a code-breaking game where the player tries to guess a hidden sequence of colors. In this version:

- The code consists of 4 colors chosen from: **r (red), o (orange), y (yellow), g (green), b (blue), v (violet)**.
- The player has **10 attempts** to guess the correct sequence.
- After each guess, feedback is given using:
  - **B**: Correct color in the correct position
  - **W**: Correct color in the wrong position
  - **.**: Incorrect color
- The game ends when the player guesses the code correctly or runs out of attempts.

## Features

- Randomly generated secret code
- Input validation for guesses
- Clear visual display of previous guesses and feedback
- Simple console-based gameplay

## How to Run

1. Clone this repository:
   ```bash
   git clone <repo-url>
