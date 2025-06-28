import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import os
import sys
import platform

# Initialize speech engine
try:
    engine = pyttsx3.init()
    engine.setProperty('rate', 170)
    voices = engine.getProperty('voices')
    # Use female voice if available, else default to first voice
    engine.setProperty('voice', voices[1].id if len(voices) > 1 else voices[0].id)
except Exception as e:
    print(f"Error initializing speech engine: {e}")
    sys.exit(1)

def talk(text):
    print("🎙️ VENNALA:", text)
    try:
        engine.say(text)
        engine.runAndWait()
    except Exception as e:
        print(f"Error in text-to-speech: {e}")

def take_command():
    listener = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            print("🎧 Listening...")
            listener.adjust_for_ambient_noise(source)
            voice = listener.listen(source, timeout=5, phrase_time_limit=5)
        command = listener.recognize_google(voice)
        command = command.lower()
        print("🗣️ You said:", command)
        return command
    except sr.UnknownValueError:
        talk("Sorry bro, I didn’t catch that.")
        return ""
    except sr.RequestError:
        talk("Network issue with Google service.")
        return ""
    except Exception as e:
        talk(f"Sorry, something went wrong: {e}")
        return ""

def run_vennala():
    command = take_command()

    if not command:
        return

    try:
        if "play" in command:
            song = command.replace("play", "").strip()
            talk("Playing on YouTube 🎶")
            pywhatkit.playonyt(song)

        elif "what's the time" in command:
            time = datetime.datetime.now().strftime('%I:%M %p')
            talk(f"It’s {time} ⏰")

        elif "who is uttam codes" in command or "who is uttam_codes" in command:
            info = (
                "Uttam, known as uttam_codes on Instagram, is a coding content creator. "
                "He teaches Python projects in Telugu and runs uttamcodes.in 💻"
            )
            talk(info)

        elif "who is" in command:
            person = command.replace("who is", "").strip()
            try:
                info = wikipedia.summary(person, sentences=1)
                talk(info)
            except wikipedia.exceptions.DisambiguationError:
                talk("Multiple results found. Please be more specific.")
            except wikipedia.exceptions.PageError:
                talk("Sorry, I couldn’t find information about that person.")
            except Exception as e:
                talk(f"Error fetching info: {e}")

        elif "joke" in command:
            talk(pyjokes.get_joke())

        elif "open chrome" in command:
            if platform.system() == "Windows":
                chrome_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
                if os.path.exists(chrome_path):
                    talk("Opening Chrome 🚀")
                    os.startfile(chrome_path)
                else:
                    talk("Chrome path not found 😬")
            else:
                talk("Opening Chrome on non-Windows systems not supported yet 😬")

        elif "open code" in command or "open vs code" in command:
            try:
                talk("Opening VS Code 💻")
                os.system("code")
            except:
                talk("VS Code not found or not in system PATH 😬")

        elif "exit" in command or "stop" in command:
            talk("Okay bro, see you later 👋")
            sys.exit()

        else:
            talk("I heard you, but I don’t understand that yet 😅")
    except Exception as e:
        talk(f"Something went wrong: {e}")

def main():
    talk("Yo! I'm VENNALA – your personal voice assistant 💡")
    while True:
        run_vennala()

if __name__ == "__main__":
    main()