import pyttsx3
import speech_recognition as sr
import pandas as pd

# ✅ Load Traffic Dataset
data_file = "Traffic.csv"  # Ensure this file is in the same directory
df = pd.read_csv(data_file)

# ✅ Initialize Text-to-Speech Engine
engine = pyttsx3.init()
engine.setProperty('rate', 150)  # Adjust speed
def speak(text):
    print(f"AI: {text}")
    engine.say(text)
    engine.runAndWait()

# ✅ SPEECH RECOGNITION
def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        try:
            audio = recognizer.listen(source, timeout=5)
            text = recognizer.recognize_google(audio).lower()
            print(f"You: {text}")
            return text
        except sr.UnknownValueError:
            speak("Sorry, I didn't understand. Can you repeat?")
            return None
        except sr.RequestError:
            speak("Voice recognition service is unavailable.")
            return None
        except sr.WaitTimeoutError:
            speak("I didn't hear anything. Please try again.")
            return None

# ✅ Traffic Prediction using Dataset
def get_traffic_info(day, time_of_day):
    filtered_data = df[(df['Day'].str.lower() == day.lower()) & (df['Time of Day'].str.lower() == time_of_day.lower())]
    if not filtered_data.empty:
        traffic_status = filtered_data.iloc[0]['Traffic Condition']
        speak(f"The traffic on {day} in the {time_of_day} is {traffic_status}.")
    else:
        speak("I couldn't find accurate traffic data for that time and day.")

# ✅ MAIN LOOP - LISTENS & RESPONDS
def yatri_ai():
    speak("Hello! I am YATRI AI. How can I assist you?")
    while True:
        command = listen()
        if command:
            if "traffic" in command:
                speak("Please mention the day of the week.")
                day = listen()
                if day:
                    speak("Please mention the time of the day, like morning, afternoon, or evening.")
                    time_of_day = listen()
                    if time_of_day:
                        get_traffic_info(day, time_of_day)
            elif "exit" in command or "stop" in command or "bye" in command:
                speak("Goodbye! Drive safely.")
                break
            else:
                speak("I didn't understand that. Please try again.")

# ✅ RUN THE AI
yatri_ai()