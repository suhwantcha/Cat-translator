# Cat Meow Translator & Meme Generator

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
