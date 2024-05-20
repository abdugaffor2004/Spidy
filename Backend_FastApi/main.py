from fastapi import FastAPI, File, Form, UploadFile
from fastapi.responses import JSONResponse

app = FastAPI()

@app.post("/upload")
async def upload_file(
    file: UploadFile = File(...),
    start_page: str = Form(...),
    last_page: str = Form(...),
    question_amount: str = Form(...)
):
    content = {
        "startPage": start_page,
        "lastPage": last_page,
        "questionAmount": question_amount,
        "fileName": file.filename
    }

    return JSONResponse(content)


@app.get('/')
def read_root():
    return JSONResponse({"Hello": "World"}) 

# Run the server using the command: uvicorn myapp:app --reload
