from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

from crewai import Crew
from dotenv import load_dotenv

from router import detect_intent
from agents import web_agent, writer_agent, coder_agent, flight_agent, image_agent
from tasks import info_task, write_task, code_task, flight_task

load_dotenv()

app = FastAPI()

templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")


# -------- LOAD DOCS --------
def load_docs(path, max_chars=1200):  # ✅ limit size
    try:
        with open(path, "r", encoding="utf-8") as f:
            return f.read()[:max_chars]   # ✂️ truncate
    except:
        return ""



web_docs = load_docs("documents/web_agent_docs.txt")
writer_docs = load_docs("documents/writer_agent_docs.txt")
coder_docs = load_docs("documents/coder_agent_docs.txt")
flight_docs = load_docs("documents/flight_agent_docs.txt")
images_docs = load_docs("documents/image_agent_docs.txt")


# -------- HOME --------
@app.get("/")
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


# -------- PREDICT --------
@app.post("/predict")
def predict(request: Request, question: str = Form(...)):

    intent = detect_intent(question)

    # -------- CODE --------
    if intent == "code":
        crew = Crew(agents=[coder_agent], tasks=[code_task])
        result = crew.kickoff(inputs={"topic": question, "knowledge": coder_docs})

    # -------- FLIGHT --------
    elif intent == "flight":
        crew = Crew(agents=[flight_agent], tasks=[flight_task])
        result = crew.kickoff(inputs={"topic": question, "knowledge": flight_docs})

    # -------- IMAGE --------
    elif intent == "image":
        img_path = image_agent.generate(question)

        return templates.TemplateResponse(
            "index.html",
            {
                "request": request,
                "prediction_text": "Image Generated",
                "image_path": img_path
            }
        )

    # -------- INFO --------
    else:
        crew = Crew(agents=[web_agent, writer_agent], tasks=[info_task, write_task])
        result = crew.kickoff(
            inputs={
                "topic": question,
                "web_context": web_docs,
                "writer_context": writer_docs
            }
        )

    return templates.TemplateResponse(
        "index.html",
        {"request": request, "prediction_text": result}
    )
