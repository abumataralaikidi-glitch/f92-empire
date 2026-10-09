from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import os

app = FastAPI(title="F-92 Sovereign Empire - Core")

templates_dir = "templates" if os.path.exists("templates") else "."
templates = Jinja2Templates(directory=templates_dir)

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    if os.path.exists(os.path.join(templates_dir, "dashboard.html")):
        return templates.TemplateResponse("dashboard.html", {"request": request})
    return "<h3>إمبراطورية F-92 السيادية تعمل بكفاءة مطلقة بنسبة 100%</h3>"

@app.get("/status")
def system_status():
    return {
        "empire": "F-92 Sovereign Empire",
        "commander": "العراب",
        "status": "Online & Secured",
        "treasury": "$92,000,000"
    }
