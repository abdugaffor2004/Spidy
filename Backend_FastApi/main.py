from fastapi import FastAPI, File, Form, UploadFile
from fastapi.responses import JSONResponse
from question_generator import QuestionGenerator
from fastapi.middleware.cors import CORSMiddleware
import os

app = FastAPI()
UPLOAD_DIRECTORY = "./uploads"

origins =[
    'http://localhost:5173'
]

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins
)

if not os.path.exists(UPLOAD_DIRECTORY):
    os.makedirs(UPLOAD_DIRECTORY)

@app.post("/upload")
async def upload_file(
    file: UploadFile = File(...),
    startPage: str = Form(...),
    lastPage: str = Form(...),
    questionAmount: str = Form(...),
    isQuestionsWithVariants: bool = Form(...)
):

    file_location = os.path.join(UPLOAD_DIRECTORY, file.filename)
    with open(file_location, "wb") as f:
        f.write(await file.read())


    question_generator = QuestionGenerator()
    
    text = question_generator.extract_text_from_pages(file_location, int(startPage), int(lastPage))
    tokenizd_str = question_generator.split_text_into_chunks(text, 500)
    questions = question_generator.main_generator(tokenizd_str, int(questionAmount), int(isQuestionsWithVariants))
    
    content = {
        "startPage": startPage,
        "lastPage": lastPage,
        "questionAmount": questionAmount,
        "questions": questions
    }

    return JSONResponse(content)


@app.get('/')
def read_root():
    return JSONResponse({"Hello": "World"}) 

# Run the server using the command: uvicorn myapp:app --reload
