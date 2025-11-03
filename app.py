
import streamlit as st
import google.generativeai as genai
from PIL import Image, ImageDraw, ImageFont
import json
import io
import requests
import textwrap

# --- Configuration ---
# Using Streamlit secrets to manage API keys
try:
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
    HUGGING_FACE_API_KEY = st.secrets["HUGGING_FACE_API_KEY"]
except Exception as e:
    st.error(f"API key not found. Make sure you have GEMINI_API_KEY and HUGGING_FACE_API_KEY in your .streamlit/secrets.toml file.")
    st.stop()

# --- Hugging Face Image Generation ---
HF_API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-xl-base-1.0"

def generate_image_with_hf(prompt: str) -> Image.Image:
    headers = {"Authorization": f"Bearer {HUGGING_FACE_API_KEY}"}
    payload = {"inputs": prompt}
    
    response = requests.post(HF_API_URL, headers=headers, json=payload)
    
    if response.status_code == 200:
        image_bytes = response.content
        image = Image.open(io.BytesIO(image_bytes))
        return image
    else:
        st.error(f"Hugging Face API Error: {response.status_code} - {response.text}")
        return None

def add_text_to_image(image: Image.Image, text: str) -> Image.Image:
    draw = ImageDraw.Draw(image)
    
    try:
        # Using a slightly smaller font to be safer with wrapping
        font = ImageFont.truetype("arial.ttf", 35)
    except IOError:
        font = ImageFont.load_default()

    # --- Text Wrapping ---
    # Wrap text to a certain number of characters per line (e.g., 40)
    wrapped_text = textwrap.wrap(text, width=40)

    # --- Calculate total text block size ---
    total_text_height = 0
    max_line_width = 0
    line_spacing = 5  # Pixels between lines

    # First pass to calculate the dimensions of the wrapped text block
    line_heights = []
    for line in wrapped_text:
        bbox = draw.textbbox((0, 0), line, font=font)
        line_width = bbox[2] - bbox[0]
        line_height = bbox[3] - bbox[1]
        if line_width > max_line_width:
            max_line_width = line_width
        total_text_height += line_height
        line_heights.append(line_height)

    total_text_height += line_spacing * (len(wrapped_text) - 1)

    # --- Position and draw each line ---
    # Start Y position for the entire text block
    current_y = image.height - total_text_height - 20  # 20px margin from bottom

    for i, line in enumerate(wrapped_text):
        bbox = draw.textbbox((0, 0), line, font=font)
        line_width = bbox[2] - bbox[0]
        
        # Center each line horizontally
        line_x = (image.width - line_width) / 2
        
        draw.text((line_x, current_y), line, fill="white", font=font, stroke_width=2, stroke_fill="black")
        current_y += line_heights[i] + line_spacing
        
    return image

# --- UI ---
st.title("🐱 Cat Meow Translator & Meme Generator")

st.write("Upload a cat's meow audio file, and we'll translate it and generate a meme!")

uploaded_file = st.file_uploader("Choose a meow audio file...", type=["wav", "mp3", "m4a", "ogg"])

if uploaded_file is not None:
    st.audio(uploaded_file, format='audio/wav')

    if st.button("Translate Meow!"):
        with st.spinner("Translating the meow and generating meme..."):
            try:
                # --- 1. Upload Audio File ---
                st.info("Uploading file to Gemini...")
                your_file = genai.upload_file(
                    path=uploaded_file,
                    display_name="Cat Meow Audio",
                    mime_type=uploaded_file.type
                )
                st.write(f"Uploaded file ''{your_file.display_name}'' as: {your_file.uri}")

                # --- 2. Analyze with Gemini ---
                st.info("Analyzing audio with Gemini Pro...")
                model = genai.GenerativeModel(model_name="gemini-2.5-flash")

                prompt = """
                You are a cat behavior expert and a meme creator.
                Analyze the provided cat meow audio and do the following:
                1.  Translate the meow into a short, funny, human-readable phrase.
                2.  Create a concept for a funny meme image based on the translation. This should be a visual description of the image.
                3.  Return the result as a JSON object with two keys: 'translation' and 'meme_description'.
                """

                response = model.generate_content([prompt, your_file])
                cleaned_json_string = response.text.strip().replace("```json", "").replace("```", "").strip()
                analysis_result = json.loads(cleaned_json_string)

                # --- 3. Generate Meme Image ---
                st.info("Generating meme image with Hugging Face...")
                meme_image = generate_image_with_hf(analysis_result['meme_description'])
                
                if meme_image:
                    final_meme = add_text_to_image(meme_image, analysis_result['translation'])
                    st.success("Translation and meme generation complete!")

                    # --- 4. Display Results ---
                    st.subheader("Translation Result (JSON)")
                    st.json(analysis_result)

                    st.subheader("Generated Meme")
                    st.image(final_meme, caption="Your generated cat meme", use_container_width=True)
                else:
                    st.error("Failed to generate meme image.")

            except Exception as e:
                st.error(f"An error occurred: {e}")

else:
    st.info("Please upload an audio file to get started.")

st.sidebar.header("About")
st.sidebar.info("This app uses Gemini to translate cat meows and Hugging Face to generate memes.")
