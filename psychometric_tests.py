TESTS = {
    "K10 (Kessler Psychological Distress Scale)": {
        "questions": [
            "In the past 4 weeks, about how often did you feel tired out for no good reason?",
            "In the past 4 weeks, about how often did you feel nervous?",
            "In the past 4 weeks, about how often did you feel so nervous that nothing could calm you down?",
            "In the past 4 weeks, about how often did you feel hopeless?",
            "In the past 4 weeks, about how often did you feel restless or fidgety?",
            "In the past 4 weeks, about how often did you feel so restless you could not sit still?",
            "In the past 4 weeks, about how often did you feel depressed?",
            "In the past 4 weeks, about how often did you feel that everything was an effort?",
            "In the past 4 weeks, about how often did you feel so sad that nothing could cheer you up?",
            "In the past 4 weeks, about how often did you feel worthless?"
        ],
        "options": ["None of the time", "A little of the time", "Some of the time", "Most of the time", "All of the time"],
        "scoring": [1, 2, 3, 4, 5],
        "interpretation": {
            "10–19": "Likely well",
            "20–24": "Mild distress",
            "25–29": "Moderate distress",
            "30–50": "Severe distress"
        }
    },
    "GHQ-12 (General Health Questionnaire-12)": {
        "questions": [
            "Have you been able to concentrate on whatever you're doing?",
            "Have you lost much sleep over worry?",
            "Have you felt that you are playing a useful part in things?",
            "Have you felt capable of making decisions about things?",
            "Have you felt constantly under strain?",
            "Have you felt you couldn't overcome your difficulties?",
            "Have you been able to enjoy your normal day-to-day activities?",
            "Have you been able to face up to your problems?",
            "Have you been feeling unhappy or depressed?",
            "Have you been losing confidence in yourself?",
            "Have you been thinking of yourself as a worthless person?",
            "Have you been feeling reasonably happy, all things considered?"
        ],
        "options": ["Not at all", "No more than usual", "Rather more than usual", "Much more than usual"],
        "scoring": [0, 1, 2, 3],
        "interpretation": {
            "0–12": "Low distress",
            "13–24": "Moderate distress",
            "25–36": "High distress"
        }
    },
    "PHQ-9 (Patient Health Questionnaire-9)": {
        "questions": [
            "Little interest or pleasure in doing things",
            "Feeling down, depressed, or hopeless",
            "Trouble falling or staying asleep, or sleeping too much",
            "Feeling tired or having little energy",
            "Poor appetite or overeating",
            "Feeling bad about yourself — or that you are a failure or have let yourself or your family down",
            "Trouble concentrating on things, such as reading the newspaper or watching television",
            "Moving or speaking so slowly that other people could have noticed? Or the opposite — being so fidgety or restless that you have been moving around a lot more than usual",
            "Thoughts that you would be better off dead or of hurting yourself in some way"
        ],
        "options": ["Not at all", "Several days", "More than half the days", "Nearly every day"],
        "scoring": [0, 1, 2, 3],
        "interpretation": {
            "0–4": "Minimal depression",
            "5–9": "Mild depression",
            "10–14": "Moderate depression",
            "15–19": "Moderately severe depression",
            "20–27": "Severe depression"
        }
    },
    "GAD-7 (Generalized Anxiety Disorder-7)": {
        "questions": [
            "Feeling nervous, anxious, or on edge",
            "Not being able to stop or control worrying",
            "Worrying too much about different things",
            "Trouble relaxing",
            "Being so restless that it is hard to sit still",
            "Becoming easily annoyed or irritable",
            "Feeling afraid as if something awful might happen"
        ],
        "options": ["Not at all", "Several days", "More than half the days", "Nearly every day"],
        "scoring": [0, 1, 2, 3],
        "interpretation": {
            "0–4": "Minimal anxiety",
            "5–9": "Mild anxiety",
            "10–14": "Moderate anxiety",
            "15–21": "Severe anxiety"
        }
    },
    "PSS (Perceived Stress Scale)": {
        "questions": [
            "In the last month, how often have you been upset because of something that happened unexpectedly?",
            "In the last month, how often have you felt that you were unable to control the important things in your life?",
            "In the last month, how often have you felt nervous and stressed?",
            "In the last month, how often have you felt confident about your ability to handle your personal problems?",
            "In the last month, how often have you felt that things were going your way?",
            "In the last month, how often have you found that you could not cope with all the things that you had to do?",
            "In the last month, how often have you been able to control irritations in your life?",
            "In the last month, how often have you felt that you were on top of things?",
            "In the last month, how often have you been angered because of things that happened that were outside of your control?",
            "In the last month, how often have you felt difficulties were piling up so high that you could not overcome them?"
        ],
        "options": ["Never", "Almost never", "Sometimes", "Fairly often", "Very often"],
        "scoring": [0, 1, 2, 3, 4],
        "interpretation": {
            "0–13": "Low stress",
            "14–26": "Moderate stress",
            "27–40": "High stress"
        }
    },
    "DASS-21 (Depression, Anxiety, and Stress Scale)": {
        "questions": [
            "I found it hard to wind down",
            "I was aware of dryness of my mouth",
            "I couldn't seem to experience any positive feeling at all",
            "I experienced breathing difficulty (e.g., excessively rapid breathing, breathlessness in the absence of physical exertion)",
            "I found it difficult to work up the initiative to do things",
            "I tended to over-react to situations",
            "I experienced trembling (e.g., in the hands)",
            "I felt that I was using a lot of nervous energy",
            "I was worried about situations in which I might panic and make a fool of myself",
            "I felt that I had nothing to look forward to",
            "I found myself getting agitated",
            "I found it difficult to relax",
            "I felt down-hearted and blue",
            "I was intolerant of anything that kept me from getting on with what I was doing",
            "I felt I was close to panic",
            "I was unable to become enthusiastic about anything",
            "I felt I wasn't worth much as a person",
            "I felt that I was rather touchy",
            "I was aware of the action of my heart in the absence of physical exertion (e.g., sense of heart rate increase, heart missing a beat)",
            "I felt scared without any good reason",
            "I felt that life was meaningless"
        ],
        "options": ["Did not apply to me at all", "Applied to me to some degree, or some of the time", "Applied to me to a considerable degree, or a good part of time", "Applied to me very much, or most of the time"],
        "scoring": [0, 1, 2, 3],
        "interpretation": {
            "Depression": {
                "0–9": "Normal",
                "10–13": "Mild",
                "14–20": "Moderate",
                "21–27": "Severe",
                "28+": "Extremely severe"
            },
            "Anxiety": {
                "0–7": "Normal",
                "8–9": "Mild",
                "10–14": "Moderate",
                "15–19": "Severe",
                "20+": "Extremely severe"
            },
            "Stress": {
                "0–14": "Normal",
                "15–18": "Mild",
                "19–25": "Moderate",
                "26–33": "Severe",
                "34+": "Extremely severe"
            }
        }
    },
    "PANAS (Positive and Negative Affect Schedule)": {
        "questions": [
            "Interested", "Distressed", "Excited", "Upset", "Strong", "Guilty", "Scared", "Hostile", "Enthusiastic", "Proud",
            "Irritable", "Alert", "Ashamed", "Inspired", "Nervous", "Determined", "Attentive", "Jittery", "Active", "Afraid"
        ],
        "options": ["Very slightly or not at all", "A little", "Moderately", "Quite a bit", "Extremely"],
        "scoring": [1, 2, 3, 4, 5],
        "interpretation": {
            "Positive Affect": "Higher scores indicate more positive emotions",
            "Negative Affect": "Higher scores indicate more negative emotions"
        }
    },
    "POMS (Profile of Mood States)": {
        "questions": [
            "Tense", "Angry", "Worn out", "Unhappy", "Lively", "Confused", "Sad", "Active", "On edge", "Energetic",
            "Fatigued", "Friendly", "Bitter", "Weary", "Alert", "Resentful", "Exhausted", "Cheerful", "Annoyed", "Lonely"
        ],
        "options": ["Not at all", "A little", "Moderately", "Quite a bit", "Extremely"],
        "scoring": [0, 1, 2, 3, 4],
        "interpretation": {
            "Tension": "Higher scores indicate more tension",
            "Depression": "Higher scores indicate more depression",
            "Anger": "Higher scores indicate more anger",
            "Vigor": "Higher scores indicate more vigor",
            "Fatigue": "Higher scores indicate more fatigue",
            "Confusion": "Higher scores indicate more confusion"
        }
    },
    "CDS (Cognitive Distortions Scale)": {
        "questions": [
            "I often think that if something bad happens, it will ruin everything",
            "I tend to blame myself for things that go wrong, even if they are not my fault",
            "I often think that if I don't do something perfectly, I have failed",
            "I frequently assume that others are thinking negatively about me",
            "I often think that if something bad happens, it will last forever",
            "I tend to focus on the negative aspects of situations and ignore the positive ones",
            "I often think that if I make a mistake, it means I am a failure",
            "I frequently assume that the worst will happen",
            "I often think that if someone disagrees with me, it means they don't like me",
            "I tend to think in extremes, such as all-or-nothing or black-and-white"
        ],
        "options": ["Never", "Rarely", "Sometimes", "Often", "Always"],
        "scoring": [1, 2, 3, 4, 5],
        "interpretation": {
            "0–20": "Minimal cognitive distortions",
            "21–30": "Mild cognitive distortions",
            "31–40": "Moderate cognitive distortions",
            "41–50": "Severe cognitive distortions"
        }
    },
    "SHI (Self-Harm Inventory)": {
        "questions": [
            "Have you ever deliberately cut yourself?",
            "Have you ever deliberately burned yourself?",
            "Have you ever deliberately hit yourself?",
            "Have you ever deliberately scratched yourself?",
            "Have you ever deliberately pulled your hair?",
            "Have you ever deliberately prevented wounds from healing?",
            "Have you ever deliberately taken an overdose of medication?",
            "Have you ever deliberately taken a substance to harm yourself?",
            "Have you ever deliberately put yourself in a dangerous situation?",
            "Have you ever deliberately driven recklessly to harm yourself?"
        ],
        "options": ["No", "Yes"],
        "scoring": [0, 1],
        "interpretation": {
            "0": "No self-harm",
            "1–3": "Mild self-harm",
            "4–6": "Moderate self-harm",
            "7–10": "Severe self-harm"
        }
    }
}

def calculate_score(test_name, responses):
    """
    Calculate the total score and interpretation for a given test.
    
    Args:
        test_name (str): The name of the test (e.g., "PHQ-9").
        responses (list): A list of user responses (scores for each question).
    
    Returns:
        For most tests: A tuple of (total_score, interpretation).
        For DASS-21 and PANAS: A dictionary with subscale scores and interpretations.
    """
    test_data = TESTS[test_name]
    total_score = sum(responses)
    interpretation = test_data["interpretation"]

    # Handle DASS-21 (Depression, Anxiety, and Stress Scale)
    if test_name == "DASS-21 (Depression, Anxiety, and Stress Scale)":
        depression_score = sum(responses[::3])  # Questions 1,4,7,...
        anxiety_score = sum(responses[1::3])    # Questions 2,5,8,...
        stress_score = sum(responses[2::3])     # Questions 3,6,9,...

        depression_interpretation = next(
            (v for k, v in interpretation["Depression"].items() 
             if check_score_range(k, depression_score)),
            "Unknown"
        )
        anxiety_interpretation = next(
            (v for k, v in interpretation["Anxiety"].items() 
             if check_score_range(k, anxiety_score)),
            "Unknown"
        )
        stress_interpretation = next(
            (v for k, v in interpretation["Stress"].items() 
             if check_score_range(k, stress_score)),
            "Unknown"
        )

        return {
            "Depression": (depression_score, depression_interpretation),
            "Anxiety": (anxiety_score, anxiety_interpretation),
            "Stress": (stress_score, stress_interpretation)
        }

    # Handle PANAS (Positive and Negative Affect Schedule)
    elif test_name == "PANAS (Positive and Negative Affect Schedule)":
        positive_affect = sum(responses[:10])  # First 10 items (positive affect)
        negative_affect = sum(responses[10:])  # Last 10 items (negative affect)
        return {
                "Positive Affect": (positive_affect, interpretation["Positive Affect"]),
                "Negative Affect": (negative_affect, interpretation["Negative Affect"])
            }

    # Handle POMS (Profile of Mood States)
    elif test_name == "POMS (Profile of Mood States)":
        tension = sum(responses[::6])  # Questions 1,7,13,19
        depression = sum(responses[1::6])  # Questions 2,8,14,20
        anger = sum(responses[2::6])  # Questions 3,9,15
        vigor = sum(responses[3::6])  # Questions 4,10,16
        fatigue = sum(responses[4::6])  # Questions 5,11,17
        confusion = sum(responses[5::6])  # Questions 6,12,18

        return f"""<strong>Tension</strong>: {tension, interpretation["Tension"]},<br>
            <strong>Depression</strong>: {depression, interpretation["Depression"]},<br>
            <strong>Anger</strong>: {anger, interpretation["Anger"]},<br>
            <strong>Vigor</strong>: {vigor, interpretation["Vigor"]},<br>
            <strong>Fatigue</strong>: {fatigue, interpretation["Fatigue"]},<br>
            <strong>Confusion</strong>: {confusion, interpretation["Confusion"]}"""
    
        f"""**Tension**: {tension, interpretation["Tension"]},
            **Depression**: {depression, interpretation["Depression"]},
            **Anger**: {anger, interpretation["Anger"]},
            **Vigor**: {vigor, interpretation["Vigor"]},
            **Fatigue**: {fatigue, interpretation["Fatigue"]},
            **Confusion**: {confusion, interpretation["Confusion"]}"""

        """return {
            "Tension": (tension, interpretation["Tension"]),
            "Depression": (depression, interpretation["Depression"]),
            "Anger": (anger, interpretation["Anger"]),
            "Vigor": (vigor, interpretation["Vigor"]),
            "Fatigue": (fatigue, interpretation["Fatigue"]),
            "Confusion": (confusion, interpretation["Confusion"])
        }"""

    # Handle other tests (K10, GHQ-12, PHQ-9, GAD-7, PSS, CDS, SHI)
    else:
        for range_str, description in interpretation.items():
            if check_score_range(range_str, total_score):
                return description
                #return total_score, description

    return "**No interpretation available.**"
    #return total_score, "No interpretation available."

def check_score_range(range_str, score):
    """
    Helper function to check if a score falls within a given range.
    
    Args:
        range_str (str): The range string (e.g., "0–4", "28+").
        score (int): The score to check.
    
    Returns:
        bool: True if the score falls within the range, False otherwise.
    """
    if "–" in range_str:
        min_score, max_score = map(int, range_str.split("–"))
        return min_score <= score <= max_score
    elif "+" in range_str:
        min_score = int(range_str.replace("+", ""))
        return score >= min_score
    else:  # Single value interpretation (e.g., SHI)
        return score == int(range_str)

