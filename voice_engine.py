import pyttsx3
import speech_recognition as sr

class VoiceEngine:
    def __init__(self, speed=150):
        self.engine = pyttsx3.init()
        self.setup_voice()
        self.engine.setProperty('rate', speed)

    def setup_voice(self):
        """Attempts to find a male voice as requested."""
        voices = self.engine.getProperty('voices')
        selected_voice = None
        
        # Look for a voice with 'male' in the name or id, or 'm1', 'm2' etc. (common in espeak)
        for voice in voices:
            name_lower = voice.name.lower()
            if 'male' in name_lower or ' m' in name_lower or voice.id.endswith('/m1'):
                selected_voice = voice.id
                break
        
        if not selected_voice and voices:
            # Default to the first voice if no specific male voice is identified
            selected_voice = voices[0].id
            
        if selected_voice:
            self.engine.setProperty('voice', selected_voice)

    def speak(self, text):
        """Converts text to speech."""
        print(f"Bot: {text}")
        self.engine.say(text)
        self.engine.runAndWait()

    def listen(self):
        """Captures voice input from the microphone."""
        recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            print("\nListening... (Speak now)")
            recognizer.adjust_for_ambient_noise(source, duration=0.5)
            try:
                audio = recognizer.listen(source, timeout=5, phrase_time_limit=10)
            except sr.WaitTimeoutError:
                return ""
                
        try:
            print("Recognizing...")
            query = recognizer.recognize_google(audio)
            print(f"You said: {query}")
            return query
        except sr.UnknownValueError:
            print("Sorry, I didn't catch that.")
            return ""
        except sr.RequestError as e:
            print(f"Could not request results; check your internet connection. Error: {e}")
            return ""

if __name__ == "__main__":
    # Test
    ve = VoiceEngine()
    ve.speak("Hello, I am testing the male voice for the FUTO assistant.")
