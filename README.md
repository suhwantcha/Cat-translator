# Cat Meow Translator & Meme Generator

This application analyzes the audio of a cat's meow to understand its meaning and creates a humorous meme to match.

## Overview

Here's how it works:
1.  **Audio Upload:** You start by uploading an audio file of a cat's meow (formats like WAV, MP3, etc., are supported).
2.  **AI Translation:** The application sends the audio file to the Gemini API, which analyzes the meow's characteristics. Based on this analysis, it translates the meow into a short, funny, human-like phrase.
3.  **Meme Generation:** The translated phrase is then used as a prompt for a separate AI model (Stable Diffusion via Hugging Face). This model generates a unique meme image that visually represents the translated text.
4.  **Final Output:** The final result is a meme image with the translated cat "speech" as a caption.

This project translates cat meows into human-readable text and generates a meme based on the translation.

There are two versions of this application:

1.  **Streamlit App (Python)**: A more advanced version that uses AI to analyze cat meow audio files.
    -   Upload a cat's meow audio file.
    -   The app uses the Gemini API to translate the meow into a funny phrase.
    -   It then uses a Hugging Face model (Stable Diffusion) to generate a meme image based on the translation.

2.  **React App (Frontend)**: A simple frontend application that displays random cat-related phrases.
    -   Click the "Translate Meow!" button to get a random "translation".

## How to Run

### Streamlit App

1.  Install the required Python packages:
    ```
    pip install -r requirements.txt
    ```
2.  Add your API keys to `.streamlit/secrets.toml`:
    ```toml
    GEMINI_API_KEY = "YOUR_GEMINI_API_KEY"
    HUGGING_FACE_API_KEY = "YOUR_HUGGING_FACE_API_KEY"
    ```
3.  Run the Streamlit app:
    ```
    streamlit run app.py
    ```

### React App

1.  Install the required Node.js packages:
    ```
    npm install
    ```
2.  Run the React app:
    ```
    npm start
    ```

## Project Structure

-   `app.py`: The main file for the Streamlit application. It handles file uploads, API calls, and displays the results.
-   `src/App.tsx`: The main component for the React application. It contains the UI and the logic for the simple meow translator.
-   `public/`: Contains the static assets for the React application, such as `index.html` and images.
-   `requirements.txt`: Lists the Python dependencies for the Streamlit application.
-   `package.json`: Lists the Node.js dependencies for the React application.
-   `.streamlit/secrets.toml`: A configuration file for storing API keys for the Streamlit application (this file is ignored by git).
-   `.gitignore`: Specifies the files and directories that should be ignored by git.