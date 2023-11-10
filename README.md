## Project Statement

This project is completed 10/11/2023

## Table of Contents
1. Introduction
1. Description of the project
1. Explanation of code
1. File structure of the project

## Introduction

Project Title: Hangman

**Description of the project:**
- Classic game of Hangman
- The user inputs one single later at a time to try unlock every letter in the secret letter
- They have a set amount of lives, which are lost with each incorrect letter guessed

**Explanation of Code:**
- Asks user to input a single letter ('guess')
- Checks if letter is alphabetical and one charcter
- guess_check function to check if guess is in the secret_word provided, if so it prints a success message, if not, it reduces one life and prints a failure message
- ask_for_input function checks the validity of the input and whether the letter has been guessed before. If it input is valid, it calls the guess_check method to append the guess to list_of_guesses. Also uses a 'while' loop to keep asking for inputs so the game can continue.

## File Structure of the project

```

HangmanProject
├── milestone_2.py
├── milestone_3.py
├── milestone_4.py
├── milestone_5.py
│   
└── README.md

```
