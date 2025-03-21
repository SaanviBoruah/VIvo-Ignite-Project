import streamlit as st
import numpy as np
import librosa
import psychometric_tests
from st_audiorec import st_audiorec
from textblob import TextBlob  # Import TextBlob
import nltk

# Configure page
st.set_page_config(
    page_title="Emotional State Detection Platform",
    page_icon="🧠",
    layout="wide"
)

# Download NLTK resources (only runs once per session)
@st.cache_resource
def download_nltk_resources():
    try:
        nltk.data.find('vader_lexicon/vader_lexicon.zip')
    except LookupError:
        nltk.download('vader_lexicon') # Download the resource

download_nltk_resources()

# Initialize models (cached for performance)
# No more Hugging Face model
@st.cache_resource
def load_models():
    return {}  # No Hugging Face model

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


# Function to convert hex to RGB
def hex_to_rgb(hex_color):
    hex_color = hex_color.lstrip("#")
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))


# Function to find the nearest color
def find_nearest_color(selected_hex, simple_colors):
    selected_rgb = hex_to_rgb(selected_hex)
    min_distance = float("inf")
    nearest_color = "gray"  # Default color if no match is found

    for hex_code, color_name in simple_colors.items():
        color_rgb = hex_to_rgb(hex_code)
        distance = np.linalg.norm(np.array(selected_rgb) - np.array(color_rgb))
        if distance < min_distance:
            min_distance = distance
            nearest_color = color_name

    return nearest_color


def analyze_voice(audio_file):
    y, sr = librosa.load(audio_file, sr=None)

    # Extract pitch using YIN algorithm
    pitch = librosa.yin(y, fmin=50, fmax=2000)
    pitch = pitch[pitch > 0]  # Remove unvoiced frames

    if len(pitch) == 0:
        return "No speech detected in audio"

    # Calculate pitch characteristics
    mean_pitch = np.mean(pitch)
    pitch_std = np.std(pitch)
    voiced_frames_ratio = len(pitch) / len(y) * 100  # Percentage of voiced speech

    # Emotional state interpretation based on pitch characteristics
    interpretation = []

    # Pitch height analysis
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

    # Pitch variability analysis
    if pitch_std < 15:
        interpretation.append("monotonous speech (possibly indicating depression or fatigue)")
    elif 15 <= pitch_std < 30:
        interpretation.append("normal pitch variation")
    else:
        interpretation.append("high pitch variability (may suggest emotional stress or excitement)")

    # Voiced speech analysis
    if voiced_frames_ratio < 60:
        interpretation.append("frequent pauses (could indicate anxiety or cognitive load)")
    elif 60 <= voiced_frames_ratio < 80:
        interpretation.append("normal speech flow")
    else:
        interpretation.append("rapid speech (may suggest excitement or stress)")

    # Create final report
    analysis = {
        "mean_pitch_hz": round(float(mean_pitch), 1),
        "pitch_variability": round(float(pitch_std), 1),
        "voiced_speech_percent": round(voiced_frames_ratio, 1),
        "interpretation": interpretation
    }

    return analysis


# Main app
def main():
    # Purpose and Submission
    st.markdown("""
    <div style="background:#EAEAED; padding:10px; text-align: center; border-radius:10px; border:2px solid #55E4C4; margin-bottom:20px">
    Built by <strong style="color:#ff4c4b">Saanvi Boruah</strong>. Project submission: <strong style="color:#ff4c4b">Multi-modal emotional wellbeing analysis suite</strong> for Vivo Ignite.
    </div>
    """, unsafe_allow_html=True)

    st.title("Emotional State Detection Platform 🧠")

    # Privacy notice
    st.markdown("""
    <div style="background:#EAEAED; padding:10px; border-radius:10px; margin-bottom:20px">
    <strong style="color: #ff4c4b">Privacy Notice:</strong> No data is stored. All analysis happens in real-time.
    </div>
    """, unsafe_allow_html=True)

    st.markdown(
                """
                <div style="text-align: center; margin-top: 20px;">
                    <a href="https://stage2-vivo-ignite-project-by-saanvi-boruah.streamlit.app/" target="_blank">
                        <button style="background-color:#ff4c4b; color:white; padding: 10px 20px; border: 4px solid #55E4C4; border-radius: 16px; cursor: pointer; font-size: large">
                            Talk to the Chatbot for Emotional Support
                        </button>
                    </a>
                </div><br>
                """,
                unsafe_allow_html=True,
            )

    # Section 1: Color Picker
    st.subheader("Color Mood Test")
    st.markdown("""
    <div style="background:#55e4c530; color:#2f7163; text-align: center; padding:10px; border-radius:0px 0px 10px 10px; margin-bottom:20px">
    Emotion and sentiment representation based on color-mood associations. Color-emotion associations vary by culture and individual.
    </div>
    """, unsafe_allow_html=True)
    color = st.color_picker("Select a color representing your mood", "#0000ff")

    # Section 2: Text Analysis
    st.subheader("Text Analysis")
    st.markdown("""
    <div style="background:#55e4c530; color:#2f7163; text-align: center; padding:10px; border-radius:0px 0px 10px 10px; margin-bottom:20px">
    Ideal for analyzing the sentiment of the user's journal or free-form text input. Emotion analysis from text are based on 6 Ekman emotions.
    </div>
    """, unsafe_allow_html=True)
    journal_text = st.text_area("Write about how you are feeling", height=100)

    # Section 3: Emotion Assessment
    st.subheader("Emotion Assessment")
    st.markdown("""
    <div style="background:#55e4c530; color:#2f7163; text-align: center; padding:10px; border-radius:0px 0px 10px 10px; margin-bottom:20px">
    Validated psychometric tests and assessment tools used to detect emotions, mental states, and mental health conditions. Useful to assess conditions like anxiety, depression, stress, and more.
    </div>
    """, unsafe_allow_html=True)
    selected_test = st.selectbox("Select a test to take:", list(psychometric_tests.TESTS.keys()), index=7)

    with st.container(border=True, height=400):
        # Display the selected test
        test_data = psychometric_tests.TESTS[selected_test]
        # st.write(f"{selected_test}")

        # Collect user responses
        responses = []
        for i, question in enumerate(test_data["questions"]):
            response = st.radio(
                f"{i + 1}. {question}",
                options=test_data["options"],
                key=f"q{i}"
            )
            responses.append(test_data["scoring"][test_data["options"].index(response)])

    # Section 4: Voice Analysis
    st.subheader("Voice Analysis")
    st.markdown("""
    <div style="background:#55e4c530; color:#2f7163; text-align: center; padding:10px; border-radius:0px 0px 10px 10px; margin-bottom:20px">
    Voice analysis interpretations are based on acoustic patterns and should be considered alongside other assessments. Individual speech patterns may vary.
    </div>
    """, unsafe_allow_html=True)
    st.write("Click the microphone to start recording:")
    wav_audio_data = st_audiorec()

    if wav_audio_data is not None:
        st.audio(wav_audio_data, format='audio/wav')

    button1, button2 = st.columns(2)

    valid = False
    actions = 0

    # Validate
    if button1.button("**Validate**"):
        if color is not None:
            actions += 1
            button1.write("✅ Color input valid")
        else:
            button1.write("⚠️ Please select a color")

        if len(journal_text) >= 50:
            actions += 1
            button1.write("✅ Text input valid")
        elif journal_text is not None and len(journal_text) < 50 and len(journal_text) > 0:
            button1.write("⚠️ Text too short for analysis. Please write more.")
        else:
            button1.write("⚠️ Please write about how you are feeling")

        if responses is not None:
            actions += 1
            button1.write("✅ Emotion assessment valid")
        else:
            button1.write("⚠️ Please answer all questions")

        if wav_audio_data is not None:
            actions += 1
            button1.write("✅ Voice recording valid")
        else:
            button1.write("⚠️ Please record your voice")

        if actions == 4:
            valid = True
            button1.write("**All tests validated**")
        else:
            valid = False
            button1.write("**Please validate all tests before submitting.**")

        button1.write(f"**{actions} tests validated**")

    # Submit button
    if button2.button("**Analyze Mental State**", type="primary", disabled = not valid):  # disabled = not valid,
        with st.container(border=True):
            st.subheader("Emotion Analysis Results")
            # Disclaimer
            st.markdown("""
            <div style="background:#EAEAED; padding:10px; border-radius:0px 0px 10px 10px; margin-bottom:20px">
            <strong style="color:#ff4c4b">Note:</strong> This is not a medical diagnosis. Consult a professional for medical advice.
            </div>
            """, unsafe_allow_html=True)
            results = []
    
            # 1. Color Analysis
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
            color_mood = COLOR_MOOD_MAP.get(nearest_color, "Unknown")
            st.markdown(f"""
                <div>
                🎨 <strong style="font-size:large">Color Mood Results: </strong>{color_mood}<br><br>
                </div>
                """, unsafe_allow_html=True)
    
            # 2. Text Analysis (TextBlob Only)
            if journal_text:
                text_blob = TextBlob(journal_text)
                sentiment_polarity = text_blob.sentiment.polarity
                sentiment_subjectivity = text_blob.sentiment.subjectivity
    
                sentiment_label = "Neutral"
                if sentiment_polarity > 0.1:
                    sentiment_label = "Positive"
                elif sentiment_polarity < -0.1:
                    sentiment_label = "Negative"
    
                st.markdown(f"""
                <div>
                📝 <strong style="font-size:large">Text Sentiment Results: </strong>{sentiment_label} (Polarity: {sentiment_polarity:.2f}, Subjectivity: {sentiment_subjectivity:.2f})<br>
                </div>
                """, unsafe_allow_html=True)
    
            # 3. Voice Analysis
            if wav_audio_data is not None:
                with open("temp_audio.wav", "wb") as f:
                    f.write(wav_audio_data)
                voice_analysis = analyze_voice("temp_audio.wav")
    
                if isinstance(voice_analysis, dict):
                    results.append(f"🎤 **Voice Analysis**:")
                    results.append(f"- Average pitch: {voice_analysis['mean_pitch_hz']} Hz")
                    results.append(f"- Pitch variability: {voice_analysis['pitch_variability']} Hz")
                    results.append(f"- Speech continuity: {voice_analysis['voiced_speech_percent']}% voiced")
                    results.append("--- Emotional indicators:")
                    for item in voice_analysis['interpretation']:
                        results.append(f"  • {item.capitalize()}")
                else:
                    results.append(f"🎤 **Voice Analysis Results:** {voice_analysis}")
    
            # 4. Psychometric Test Analysis
            # Calculate score and interpretation
            if selected_test == "DASS-21 (Depression, Anxiety, and Stress Scale)":
                results = psychometric_tests.calculate_score(selected_test, responses)
                st.write(f"😔 **Depression**: {results['Depression'][0]} ({results['Depression'][1]})")
                st.write(f"😟 **Anxiety:** {results['Anxiety'][0]} ({results['Anxiety'][1]})")
                st.write(f"😫 **Stress**: {results['Stress'][0]} ({results['Stress'][1]})")
            elif selected_test == "PANAS (Positive and Negative Affect Schedule)":
                results = psychometric_tests.calculate_score(selected_test, responses)
                st.write(f"😄 **Positive Affect**: {results['Positive Affect'][0]} ({results['Positive Affect'][1]})")
                st.write(f"☹️ **Negative Affect**: {results['Negative Affect'][0]} ({results['Negative Affect'][1]})")
            else:
                interpretation = psychometric_tests.calculate_score(selected_test, responses)
                st.markdown(f"""
                <div>
                😶 <strong style="font-size:large">Emotion Assessment Results:</strong><br>
                </div>
                """, unsafe_allow_html=True)
    
                st.markdown(f"""
                <div>
                {interpretation}<br>
                </div>
                """, unsafe_allow_html=True)
    
                # Show all results
                st.markdown("\n\n".join(results))


if __name__ == "__main__":
    main()
