# Voice Translator Program
![image](https://github.com/user-attachments/assets/f1f17809-f01a-491a-8156-95d748e4d52d)

## Description
This code is a program that allows a person to speak into a microphone, transcribe their voice to text, translate the text to Turkish, generate a witty response, and then read that response aloud. Additionally, it displays both the original text and the generated response in an interactive window. Here’s a step-by-step explanation without technical jargon:

### What does this program do?
1. **Voice Recognition**: The program listens to what you say through the microphone and converts your voice into text using a voice recognition service.
2. **Translation**: The text you spoke is automatically translated into Turkish. A witty response is also generated, containing a paragraph in Turkish and another in English. The response is clever and includes a question.
3. **Response Playback**: The first part of the response (the Turkish paragraph) is converted to speech and played through the computer speakers.
4. **Visual Interface**: The program features a window that displays the text you said, the translation into Turkish, and the generated response.
5. **Microphone Interaction**: To use it, you click a button, speak, and the program takes care of processing everything else.

### How does it work?
- When you speak, the program captures the audio and converts it to text.
- Then, it translates what you said into Turkish.
- Additionally, it generates a response that includes a paragraph in Turkish and another in English.
- The first part of the response is converted to audio and played back.
- The entire process is displayed in a window, where you can see the recognized text and the generated response.

This program is designed to interact with voice and create a conversation, utilizing translation and automated responses.

## Installation
To run this file in Python, follow these steps:

1. **Install Python**  
   Make sure you have Python installed on your system. If not, you can download it from [python.org](https://www.python.org).

2. **Install Required Dependencies**  
   This file uses several libraries that need to be installed. Open a terminal and run the following commands to install them:
   - Install `tkinter` for the graphical interface:
     - On Windows: It comes pre-installed with Python.
     - On Linux:
       ```bash
       sudo apt-get install python3-tk
       ```
     - On Mac:
       ```bash
       brew install python-tk
       ```
   - Install additional libraries required by the program using pip:
     ```bash
     pip install python-dotenv SpeechRecognition gtts google-generativeai
     ```

3. **Set Up the Google Generative AI API**  
   - The code requires an API token to use Google Bard services.
   - Create a `.env` file in the same directory as the code with the following content:
     ```makefile
     BARD_API_KEY=YOUR_API_KEY
     ```
   Replace `YOUR_API_KEY` with your actual API key. You can obtain this key through the Google Cloud portal.

4. **Run the Program**  
   - Once all dependencies are installed and the `.env` file is set up, open a terminal or command line.
   - Navigate to the directory where the `translator.py` file is located:
     ```bash
     cd path/to/your/file
     ```
   - Run the file with the following command:
     ```bash
     python translator.py
     ```

5. **Using the Program**  
   - A window will appear with two text boxes and a button.
   - Click the button to access the microphone and say something. The program will recognize your voice, translate what you say into Turkish, generate a response, and display it in the window. It will also play the first part of the response in Turkish through the speakers.

## Additional Requirements
- Internet access is needed to use the Google API.
- A functional microphone is required for the program to recognize audio.


If you wish to contribute to this project, feel free to fork the repository and submit a pull request with your improvements.

This project is licensed under the MIT License. See the LICENSE file for more details.
