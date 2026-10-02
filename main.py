from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

# CSS files
app.mount(
    "/static",
    StaticFiles(directory="static"),
    name="static"
)

# HTML files
templates = Jinja2Templates(
    directory="templates"
)


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {"request": request}
    )


@app.get("/calculate")
async def calculate(
    a: float,
    b: float,
    operation: str
):

    if operation == "add":
        result = a + b

    elif operation == "subtract":
        result = a - b

    elif operation == "multiply":
        result = a * b

    elif operation == "divide":

        if b == 0:
            return {
                "success": False,
                "error": "Cannot divide by zero"
            }

        result = a / b

    else:
        return {
            "success": False,
            "error": "Invalid operation"
        }

    return {
        "success": True,
        "result": result
    }