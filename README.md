# Blackjack Game in Python
## Introduction
This project implements a simple Blackjack game in Python. The program is a normal Blackjack game where the player competes against the dealer. The goal is to reach a total card value of 21 or to get closer to it than the dealer, without exceeding 21.

## How the Game Works
   - The player is dealt two random cards at the start of the game.
   - The dealer is also dealt two cards, one of which is hidden until the player finishes their turn.
   - The player can choose to:
      - Hit: Draw another card.
      - Stand: End their turn and let the dealer play.
   - The dealer will follow a simple rule to draw cards until their total is at least 17.
   - If the player's or dealer's total exceeds 21, they "bust" (lose the round).
## Rules of Blackjack
1. Card Values:
   - Number cards (2-10) are worth their face value.
   - Face cards (Jack, Queen, King) are worth 10 points.
   - Aces can be worth either 1 or 11 points, whichever is more beneficial to the hand.
2. Winning Conditions:
   - A total of 21 points is a "Blackjack" and usually wins the round.
   - If neither the player nor the dealer gets a Blackjack, the closest to 21 wins.
   - If both the player and dealer have the same total, it's a tie (push).




## vosk

This project uses the Vosk speech recognition library to process audio input. Before running the project, you need to download a small Vosk model and update the path in the `voice1.py` file.

## Prerequisites
   
 Vosk Library
   - Install the Vosk library by running:
     pip install vosk


## Setup Instructions

### 1. Download the Vosk Model
   - Visit the Vosk models page: [Vosk Models](https://alphacephei.com/vosk/models)
   - Download the **small model** 
     English: `vosk-model-small-en-us 0.15`
   - Extract the downloaded file to a directory on your system.

### 2. Update the Model Path in `voice1.py`
   - Open the `voice1.py` file in a text editor.
     
   - In Line 6 the model path is specified, for example:
     model_path = "path/to/your/model"

   - Replace `"path/to/your/model"` with the actual path to the extracted model directory. For example:
     model_path = "C:/vosk/vosk-model-small-en-us"
