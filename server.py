
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import os

app = FastAPI(title="F-92 Sovereign Core")

# تحديد مسار القوالب بدقة
templates_dir = "templates" if os.path.exists("templates") else "."
templates = Jinja2Templates(directory=templates_dir)

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    # محاولة عرض قالب HTML إذا كان موجوداً، أو العرض الاحتياطي
    if os.path.exists(os.path.join(templates_dir, "index.html")):
        return templates.TemplateResponse("index.html", {"request": request})
    return "<h3>إمبراطورية F-92 تعمل بنجاح</h3>"
