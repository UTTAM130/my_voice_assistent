from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import pywhatkit
import datetime
import wikipedia
import pyjokes

app = FastAPI(title="VENNALA Voice Assistant API")

class CommandRequest(BaseModel):
    command: str

@app.post("/execute")
async def execute_command(request: CommandRequest):
    command = request.command.lower()
    try:
        if "play" in command:
            song = command.replace("play", "").strip()
            pywhatkit.playonyt(song)
            return {"response": f"Playing {song} on YouTube 🎶"}

        elif "what's the time" in command:
            time = datetime.datetime.now().strftime('%I:%M %p')
            return {"response": f"It’s {time} ⏰"}

        elif "who is uttam codes" in command or "who is uttam_naidu" in command:
            info = (
                "Uttam, known as uttam_naidu on Instagram, is a MSc Data Science student. "
                "He teaches how to do projects. 💻"
            )
            return {"response": info}

        elif "who is" in command:
            person = command.replace("who is", "").strip()
            try:
                info = wikipedia.summary(person, sentences=1)
                return {"response": info}
            except wikipedia.exceptions.DisambiguationError:
                return {"response": "Multiple results found. Please be more specific."}
            except wikipedia.exceptions.PageError:
                return {"response": "Sorry, I couldn’t find information about that person."}

        elif "joke" in command:
            return {"response": pyjokes.get_joke()}

        else:
            return {"response": "I don’t understand that command yet 😅"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing command: {str(e)}")

@app.get("/")
async def root():
    return {"message": "Welcome to VENNALA Voice Assistant API"}