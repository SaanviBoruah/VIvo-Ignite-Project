import streamlit as st
import numpy as np
import librosa
import psychometric_tests
from st_audiorec import st_audiorec
from textblob import TextBlob
import nltk
import cv2
from fer import FER
from PIL import Image

# Configure page
st.set_page_config(
    page_title="Emotional State Detection Platform",
    page_icon="🧠",
    layout="wide"
)

# Download NLTK resources
@st.cache_resource
def download_nltk_resources():
    nltk.download('vader_lexicon', quiet=True)

download_nltk_resources()

# Initialize models (including FER)
@st.cache_resource
def load_models():
    return {'emotion_detector': FER()}

models = load_models()

with open("style.css") as css:
    st.markdown(f'<style>{css.read()}</style>', unsafe_allow_html=True)

# Color-Mood Mapping
COLOR_MOOD_MAP = {
    'red': 'Angry/Passionate',
    'blue': 'Calm/Peaceful',
    'green': 'Balanced/Hopeful',
    'yellow': 'Happy/Energetic',
    'orange': 'Excited/Enthusiastic',
    'purple': 'Creative/Mysterious',
    'pink': 'Loving/Playful',
    'brown': 'Stable/Grounded',
    'black': 'Depressed/Anxious',
    'white': 'Pure/Innocent',
    'gray': 'Neutral/Indifferent',
    'teal': 'Refreshed/Calm',
    'magenta': 'Bold/Innovative',
    'lavender': 'Relaxed/Serene',
    'gold': 'Joyful/Optimistic',
    'silver': 'Calm/Reflective',
    'turquoise': 'Refreshed/Calm',
    'maroon': 'Serious/Disciplined',
    'navy': 'Trusting/Reliable',
    'beige': 'Comfortable/Relaxed'
}

def hex_to_rgb(hex_color):
    hex_color = hex_color.lstrip("#")
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

def find_nearest_color(selected_hex, simple_colors):
    selected_rgb = hex_to_rgb(selected_hex)
    min_distance = float("inf")
    nearest_color = "gray"

    for hex_code, color_name in simple_colors.items():
        color_rgb = hex_to_rgb(hex_code)
        distance = np.linalg.norm(np.array(selected_rgb) - np.array(color_rgb))
        if distance < min_distance:
            min_distance = distance
            nearest_color = color_name

    return nearest_color

def analyze_voice(audio_file):
    y, sr = librosa.load(audio_file, sr=None)
    pitch = librosa.yin(y, fmin=50, fmax=2000)
    pitch = pitch[pitch > 0]

    if len(pitch) == 0:
        return "No speech detected in audio"

    mean_pitch = np.mean(pitch)
    pitch_std = np.std(pitch)
    voiced_frames_ratio = len(pitch) / len(y) * 100

    interpretation = []
    if mean_pitch < 85:
        interpretation.append("low pitch (possibly indicating sadness, fatigue, or depression)")
    elif 85 <= mean_pitch < 165:
        interpretation.append("moderate pitch (typical for calm, relaxed speech)")
    elif 165 <= mean_pitch < 255:
        interpretation.append("elevated pitch (could indicate stress or anxiety)")
    elif 255 <= mean_pitch < 350:
        interpretation.append("high pitch (may suggest excitement or anxiety)")
    else:
        interpretation.append("very high pitch (could indicate strong emotions)")

    if pitch_std < 15:
        interpretation.append("monotonous speech (possibly indicating depression or fatigue)")
    elif 15 <= pitch_std < 30:
        interpretation.append("normal pitch variation")
    else:
        interpretation.append("high pitch variability (may suggest emotional stress or excitement)")

    if voiced_frames_ratio < 60:
        interpretation.append("frequent pauses (could indicate anxiety or cognitive load)")
    elif 60 <= voiced_frames_ratio < 80:
        interpretation.append("normal speech flow")
    else:
        interpretation.append("rapid speech (may suggest excitement or stress)")

    return {
        "mean_pitch_hz": round(float(mean_pitch), 1),
        "pitch_variability": round(float(pitch_std), 1),
        "voiced_speech_percent": round(voiced_frames_ratio, 1),
        "interpretation": interpretation
    }

def main():
    # Page header and privacy notice
    st.markdown("""
    <div style="background:#EAEAED; padding:10px; text-align: center; border-radius:10px; border:2px solid #55E4C4; margin-bottom:20px">
    Built by <strong style="color:#ff4c4b">Saanvi Boruah</strong>. Project submission: <strong style="color:#ff4c4b">Multi-modal emotional wellbeing analysis suite</strong> for Vivo Ignite.
    </div>
    """, unsafe_allow_html=True)

    st.title("Emotional State Detection Platform 🧠")

    st.markdown("""
    <div style="background:#EAEAED; padding:10px; border-radius:10px; margin-bottom:20px">
    <strong style="color: #ff4c4b">Privacy Notice:</strong> No data is stored. All analysis happens in real-time.
    </div>
    """, unsafe_allow_html=True)

    # Create tabs
    tab1, tab2 = st.tabs(["🧪 General Tests", "🔍 Advanced Tests"])

    with tab1:
        st.subheader("Basic Emotional Assessment Modules")
        
        # Initialize session state for general tests
        if 'general_valid' not in st.session_state:
            st.session_state.general_valid = False

        # Color Mood Test
        color = st.color_picker("🎨 Choose a color representing your mood", "#0000ff")

        # Text Analysis
        journal_text = st.text_area("📝 Write about how you are feeling (min 50 characters)", height=100)

        # Psychometric Test
        selected_test = st.selectbox("📊 Select a psychometric test:", 
                                   list(psychometric_tests.TESTS.keys()), 
                                   index=7)
        responses = []
        with st.container(border=True, height=300):
            test_data = psychometric_tests.TESTS[selected_test]
            for i, question in enumerate(test_data["questions"]):
                response = st.radio(
                    f"{i + 1}. {question}",
                    options=test_data["options"],
                    key=f"gen_q{i}"
                )
                responses.append(test_data["scoring"][test_data["options"].index(response)])

        # Voice Analysis
        wav_audio_data = st_audiorec()
        if wav_audio_data is not None:
            st.audio(wav_audio_data, format='audio/wav')

        # General Tests Validation
        st.markdown("---")
        gen_col1, gen_col2 = st.columns(2)
        with gen_col1:
            if st.button("✅ Validate General Tests"):
                valid = True
                if len(journal_text) < 50:
                    st.error("Text analysis requires at least 50 characters")
                    valid = False
                if not wav_audio_data:
                    st.error("Voice recording required")
                    valid = False
                if valid:
                    st.session_state.general_valid = True
                    st.success("All general tests validated!")

        with gen_col2:
            if st.button("📄 Generate General Report", 
                        disabled=not st.session_state.general_valid,
                        type="primary"):
                with st.container(border=True):
                    st.subheader("General Tests Analysis Report")
                    
                    # Color Analysis
                    color_hex = color.lstrip("#").lower()
                    simple_colors = {
                        "ff0000": "red",  # Red
                        "0000ff": "blue",  # Blue
                        "00ff00": "green",  # Green
                        "ffff00": "yellow",  # Yellow
                        "ffa500": "orange",  # Orange
                        "800080": "purple",  # Purple
                        "ffc0cb": "pink",  # Pink
                        "a52a2a": "brown",  # Brown
                        "000000": "black",  # Black
                        "ffffff": "white",  # White
                        "808080": "gray",  # Gray
                        "008080": "teal",  # Teal
                        "ff00ff": "magenta",  # Magenta
                        "e6e6fa": "lavender",  # Lavender
                        "ffd700": "gold",  # Gold
                        "c0c0c0": "silver",  # Silver
                        "40e0d0": "turquoise",  # Turquoise
                        "800000": "maroon",  # Maroon
                        "000080": "navy",  # Navy
                        "f5f5dc": "beige"  # Beige
                    }

                    nearest_color = find_nearest_color(color_hex, simple_colors)
                    st.write(f"**Color Mood**: {COLOR_MOOD_MAP.get(nearest_color, 'Unknown')}")

                    # Text Analysis
                    analysis = TextBlob(journal_text)
                    polarity = analysis.sentiment.polarity
                    st.write(f"**Text Sentiment**: {'Positive' if polarity > 0 else 'Negative' if polarity < 0 else 'Neutral'}")

                    # Psychometric Results
                    test_results = psychometric_tests.calculate_score(selected_test, responses)
                    st.write("**Psychometric Assessment**:")
                    st.write(test_results)

                    # Voice Analysis
                    with open("temp_audio.wav", "wb") as f:
                        f.write(wav_audio_data)
                    voice_results = analyze_voice("temp_audio.wav")
                    st.write("**Voice Analysis**:")
                    st.write(f"Average pitch: {voice_results['mean_pitch_hz']} Hz")

    with tab2:
        st.subheader("Advanced Facial Emotion Recognition")
        
        # Initialize session state for advanced test
        if 'advanced_valid' not in st.session_state:
            st.session_state.advanced_valid = False

        picture = st.camera_input("😃 Take a picture for facial analysis")
        if picture:
            img = Image.open(picture)
            img_array = np.array(img)
            img_array = cv2.cvtColor(img_array, cv2.COLOR_RGB2BGR)
            results = models['emotion_detector'].detect_emotions(img_array)
            st.session_state.facial_emotions = results

        # Advanced Test Validation
        st.markdown("---")
        adv_col1, adv_col2 = st.columns(2)
        with adv_col1:
            if st.button("✅ Validate Advanced Test"):
                if 'facial_emotions' in st.session_state:
                    st.session_state.advanced_valid = True
                    st.success("Facial analysis validated!")
                else:
                    st.error("Please capture a facial image first")

        with adv_col2:
            if st.button("📄 Generate Advanced Report", 
                        disabled=not st.session_state.advanced_valid,
                        type="primary"):
                with st.container(border=True):
                    st.subheader("Advanced Test Analysis Report")
                    facial_results = st.session_state.facial_emotions
                    if facial_results:
                        for i, face in enumerate(facial_results):
                            emotions = face['emotions']
                            dominant = max(emotions, key=emotions.get)
                            st.write(f"""
                            - **Face {i+1}**: {dominant.capitalize()} 
                            (Confidence: {emotions[dominant]:.0%})
                            """)
                    else:
                        st.write("No faces detected in the image")

if __name__ == "__main__":
    main()
