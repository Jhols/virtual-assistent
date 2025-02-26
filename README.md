# Virtual Assistant Project

This project demonstrates how to create a simple voice-controlled virtual assistant using Python. The assistant listens to the user's speech, processes commands, and responds accordingly using text-to-speech (TTS). The assistant can perform tasks like greeting the user, saving the user's name, and responding to basic commands like "help" and "goodbye."

## Requirements

- Python 3.x
- `virtualenv` (for creating a virtual environment)
- `speechrecognition` (for recognizing speech)
- `pyttsx3` (for text-to-speech functionality)
- `pyaudio` (required for microphone input)

## Setting Up the Project

To set up this project, follow the steps below. You neeed to have Python installed:

### 1. Install `virtualenv` (if not already installed)

`virtualenv` is a tool to create isolated Python environments, which helps to manage dependencies separately for different projects.

To install `virtualenv`, run the following command:

```bash
pip install virtualenv
```

### 2. Create a Virtual Environment

Create a new virtual environment for this project. This helps keep your project's dependencies isolated from other projects.

1. Navigate to your project directory in the terminal.
2. Run the following command to create the virtual environment:

```bash
virtualenv venv
```

This will create a new folder called `venv` where all dependencies for the project will be installed.

### 3. Activate the Virtual Environment

To activate the virtual environment, run the following command based on your operating system:

- On **Windows**:

```bash
.\venv\Scripts\activate
```

- On **macOS/Linux**:

```bash
source venv/bin/activate
```

You should now see `(venv)` at the beginning of your terminal prompt, indicating that the virtual environment is active.

### 4. Install Required Dependencies

Install the required dependencies for the project using `pip`. 

```bash
pip install -r requirements.txt
```

The `requirements.txt` file contains the necessary Python packages.

### 6. Running the Project

Once the virtual environment is set up and dependencies are installed, you can run the assistant script.

To start the virtual assistant, simply run the Python script:

```bash
python index.py
```

The assistant will start listening for voice commands. You can say things like:

- "Hello" or "Hi" – to get a greeting.
- "My name is [Your Name]" – to set your name.
- "What is my name?" – to ask the assistant your name.
- "Thank you" – to receive a polite response.
- "Bye" or "Goodbye" – to end the conversation.

### 7. Deactivating the Virtual Environment

When you're done working with the project, you can deactivate the virtual environment by running:

```bash
deactivate
```

This will return you to your system's global Python environment.

## Code Overview

The main functionality of the virtual assistant is handled by the `index.py` file. Here's a brief breakdown of how the code works:

- **Speech Recognition**: The assistant listens to the user's voice input through the microphone using the `speechrecognition` library. The speech is then converted to text.
- **Text-to-Speech**: Once the assistant recognizes the command, it responds by speaking the response aloud using the `pyttsx3` library.
- **Commands**: The assistant can respond to specific commands like greetings, asking for the user's name, and more. The assistant uses regular expressions (`re`) to match the recognized phrases with the appropriate response.