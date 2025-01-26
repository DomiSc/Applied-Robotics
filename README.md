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
      - Ac, Ah: 1 point.

3. Visualization:

   - The detected cards are displayed on the screen with bounding boxes, confidence scores, and their corresponding labels.


Here's the README for your card detection project:

Playing Card Detection with YOLOv8
This project implements a real-time playing card detection system using the YOLOv8 object detection model. It is designed to detect playing cards and assign their Blackjack values in a game scenario. The system uses a pre-trained model and a webcam feed to detect and classify cards in real-time.

Dataset and Model
The project utilizes the dataset and pre-trained model from the repository:
TeogopK/Playing-Cards-Object-Detection.

The specific model used is yolov8m.pt, which has been trained to recognize various playing cards.

Prerequisites
Python

Install Python 3.8 or higher.
Required Libraries

Install the following Python packages:
bash
Kopieren
Bearbeiten
pip install ultralytics opencv-python-headless
YOLOv8 Model

Download the pre-trained yolov8m.pt model from the dataset repository: final_models/yolov8m.pt.
Save the model file in your project directory.
Webcam

Ensure a functioning webcam is connected to your system.
How It Works
Card Detection:

The script captures live video frames from the webcam and uses the YOLOv8 model to detect playing cards in real-time.
Blackjack Values:

Detected cards are assigned their corresponding Blackjack values. For example:
2c, 2d, 2h, 2s: 2 points.
Jc, Qh, Ks: 10 points.
Ac, Ah: 1 point.
Visualization:

The detected cards are displayed on the screen with bounding boxes, confidence scores, and their corresponding labels.
Real-Time Updates:

The program continuously scans for new cards until terminated by pressing the q key.
Setup Instructions
1. Clone or Download the Repository
Clone the repository or copy the script files to a local directory:
bash
Kopieren
Bearbeiten
git clone https://github.com/your-username/playing-card-detection.git
cd playing-card-detection
2. Place the YOLOv8 Model
Download and place the yolov8m.pt model in the same directory as the script.
3. Run the Program
Start the detection script using Python:
bash
Kopieren
Bearbeiten
python detect_cards.py
Usage
Launch the Program:

Run the script and allow the camera to initialize.
Detect Cards:

Show playing cards in front of the camera. The program will:
Detect and classify the card.
Display the card label, confidence, and its Blackjack value.
Stop the Program:

Press the q key to terminate the script.
Troubleshooting
Webcam Not Detected:

Ensure your webcam is properly connected and accessible by Python.
Model File Not Found:

Verify that the yolov8m.pt file is placed in the correct directory.
Performance Issues:

Reduce the model size by using a smaller variant (e.g., yolov8n.pt) if your system has limited resources.
Missing Libraries:

Install any missing dependencies using:
bash
Kopieren
Bearbeiten
pip install -r requirements.txt
Potential Enhancements
Add functionality to detect multiple cards simultaneously.
Incorporate a scoring system for Blackjack games.
Optimize for faster detection on low-end devices.
Create a graphical user interface (GUI) for enhanced usability.
License
This project is licensed under the MIT License. Refer to the LICENSE file for more details.

## Author
Alexandra Sumera, Peter Pham, Samuel Schweigert, Dominick Schrenk
