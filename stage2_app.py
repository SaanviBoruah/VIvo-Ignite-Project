import streamlit as st
import numpy as np
import librosa
import psychometric_tests
from st_audiorec import st_audiorec
from textblob import TextBlob
import nltk
from PIL import Image, ImageDraw
from transformers import pipeline

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

# Load models
@st.cache_resource
def load_models():
    detector = pipeline("object-detection", model="facebook/detr-resnet-50")
    classifier = pipeline("image-classification", model="Rajaram1996/FacialEmoRecog")
    return detector, classifier

face_detector, emotion_classifier = load_models()

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

def detect_and_analyze_faces(image):
    results = face_detector(image)
    draw = ImageDraw.Draw(image)
    emotions = []
    
    for result in results:
        if result['label'] == 'person' and result['score'] > 0.9:
            box = result['box']
            xmin, ymin, xmax, ymax = box.values()
            
            # Crop face region
            face = image.crop((xmin, ymin, xmax, ymax))
            
            # Analyze emotion
            emotion_result = emotion_classifier(face)
            top_emotion = emotion_result[0]['label']
            
            # Draw bounding box and label
            draw.rectangle([xmin, ymin, xmax, ymax], outline="red", width=2)
            draw.text((xmin, ymin-20), top_emotion, fill="red")
            
            emotions.append({
                "position": (xmin, ymin, xmax-xmin, ymax-ymin),
                "emotion": top_emotion,
                "confidence": emotion_result[0]['score']
            })
    
    return image, emotions

def main():
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

    tab1, tab2 = st.tabs(["🧪 General Tests", "🔍 Advanced Tests"])

    with tab1:
        st.subheader("Basic Emotional Assessment")
        
        color = st.color_picker("🎨 Select a color representing your mood", "#0000ff")
        journal_text = st.text_area("📝 Write about how you are feeling (min 50 characters)", height=100)
        selected_test = st.selectbox("📊 Choose a psychometric test:", 
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

        wav_audio_data = st_audiorec()
        if wav_audio_data is not None:
            st.audio(wav_audio_data, format='audio/wav')

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
                        disabled=not st.session_state.get('general_valid', False),
                        type="primary"):
                with st.container(border=True):
                    st.subheader("General Analysis Report")
                    color_hex = color.lstrip("#").lower()
                    simple_colors = {
                        "ff0000": "red", "0000ff": "blue", "00ff00": "green",
                        "ffff00": "yellow", "ffa500": "orange", "800080": "purple",
                        "ffc0cb": "pink", "a52a2a": "brown", "000000": "black",
                        "ffffff": "white", "808080": "gray", "008080": "teal",
                        "ff00ff": "magenta", "e6e6fa": "lavender", "ffd700": "gold",
                        "c0c0c0": "silver", "40e0d0": "turquoise", "800000": "maroon",
                        "000080": "navy", "f5f5dc": "beige"
                    }
                    nearest_color = find_nearest_color(color_hex, simple_colors)
                    st.write(f"**Color Mood**: {COLOR_MOOD_MAP.get(nearest_color, 'Unknown')}")

                    analysis = TextBlob(journal_text)
                    polarity = analysis.sentiment.polarity
                    st.write(f"**Text Sentiment**: {'Positive' if polarity > 0 else 'Negative' if polarity < 0 else 'Neutral'}")

                    test_results = psychometric_tests.calculate_score(selected_test, responses)
                    st.write("**Psychometric Assessment**:")
                    st.write(test_results)

                    with open("temp_audio.wav", "wb") as f:
                        f.write(wav_audio_data)
                    voice_results = analyze_voice("temp_audio.wav")
                    st.write("**Voice Analysis**:")
                    st.write(f"Average pitch: {voice_results['mean_pitch_hz']} Hz")
                    st.write("Interpretations:")
                    for item in voice_results['interpretation']:
                        st.write(f"- {item.capitalize()}")

    with tab2:
        st.subheader("Advanced Facial Emotion Analysis")
        uploaded_file = st.file_uploader("📸 Upload a photo for analysis", 
                                       type=["jpg", "jpeg", "png"])
        
        if uploaded_file is not None:
            image = Image.open(uploaded_file).convert("RGB")
            processed_image, face_results = detect_and_analyze_faces(image)
            
            st.image(processed_image, caption="Processed Image with Emotion Detection")
            
            if face_results:
                st.write("**Detected Emotions**:")
                for i, face in enumerate(face_results):
                    st.write(f"""
                    - Face {i+1}:
                        - Position: {face['position']}
                        - Emotion: {face['emotion']}
                        - Confidence: {face['confidence']:.2%}
                    """)
            else:
                st.warning("No faces detected in the image")

if __name__ == "__main__":
    main()
