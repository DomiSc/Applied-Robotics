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




# vosk

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


# Playing Card Detection with YOLOv8
This project implements a real-time playing card detection system using the YOLOv8 object detection model. It is designed to detect playing cards and assign their Blackjack values in a game scenario. The system uses a pre-trained model and a webcam feed to detect and classify cards in real-time.

## Dataset and Model
The project utilizes the dataset and pre-trained model from the repository:
https://github.com/TeogopK/Playing-Cards-Object-Detection/tree/main/final_models

The specific model used is yolov8m.pt, which has been trained to recognize various playing cards.

## Required Libraries

1. Install the following Python packages:
   - pip install ultralytics opencv-python-headless

2. YOLOv8 Model
   - Download the pre-trained yolov8m.pt model from the dataset repository: final_models/yolov8m.pt
   - Save the model file in your project directory.

 3. Webcam
   - Ensure a functioning webcam is connected to your system.

## How It Works
1. Card Detection:
   - The script captures live video frames from the webcam and uses the YOLOv8 model to detect playing cards in real-time.

2. Blackjack Values:

   - Detected cards are assigned their corresponding Blackjack values. For example:
      - 2c, 2d, 2h, 2s: 2 points.
      - Jc, Qh, Ks: 10 points.
      - Ac, Ah: 1/11 point.

3. Visualization:

   - The detected cards are displayed on the screen with bounding boxes, confidence scores, and their corresponding labels.

## Author
Alexandra Sumera, Peter Pham, Samuel Schweigert, Dominick Schrenk
