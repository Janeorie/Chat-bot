import sys
from chatbot_logic import FUTOChatbot
from voice_engine import VoiceEngine

def main_menu():
    print("====================================")
    print("   FUTO & Nigerian Uni Assistant   ")
    print("====================================")
    print("1. Text Mode (Console Chat)")
    print("2. Voice Mode (Speech Interactive)")
    print("3. Exit")
    choice = input("\nSelect an option: ")
    return choice

def run_text_mode(bot):
    print("\n[Text Mode Activated]")
    bot.start_console_chat()

def run_voice_mode(bot, voice):
    print("\n[Voice Mode Activated]")
    voice.speak("Hello! I am your FUTO assistant. How can I help you today?")
    
    while True:
        user_input = voice.listen()
        
        if not user_input:
            continue
            
        if any(word in user_input.lower() for word in ["quit", "exit", "bye", "goodbye"]):
            response = bot.respond("quit")
            voice.speak(response)
            break
            
        response = bot.respond(user_input)
        if response:
            voice.speak(response)
        else:
            voice.speak("I'm sorry, I don't have information on that yet.")

if __name__ == "__main__":
    bot = FUTOChatbot()
    
    while True:
        choice = main_menu()
        
        if choice == '1':
            run_text_mode(bot)
        elif choice == '2':
            try:
                voice = VoiceEngine()
                run_voice_mode(bot, voice)
            except Exception as e:
                print(f"Error initializing voice mode: {e}")
                print("Make sure your microphone is connected and dependencies are installed.")
        elif choice == '3':
            print("Goodbye! Technology for Service.")
            sys.exit()
        else:
            print("Invalid choice. Please try again.")
