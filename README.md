# Black Jack Project

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
