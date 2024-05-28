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
    tokenizd_str = question_generator.split_text_into_chunks(text, 500,int(questionAmount))
    questions = question_generator.main_generator(tokenizd_str, int(questionAmount), int(isQuestionsWithVariants))
    print( questions )
    mas = []


    for i in questions:
        result1 = question_generator.extract_between_colon_and_question(i)

        result1 = str(result1).replace("Вопрос:", "")
        result1 = result1.replace("[", "")
        result1 = result1.replace("]", "")

        line = question_generator.remove_before_question_mark(i)
        line = line.replace("Ответ:", "")
        line = line.replace("?", "")
        mas.append({'question' : result1 , 'answer' : line})

    
  
    

    content = {
        "startPage": startPage,
        "lastPage": lastPage,
        "questionAmount": questionAmount,
        "questions": mas
    }

    return JSONResponse(content)


@app.get('/')
def read_root():
    return JSONResponse({"Hello": "World"}) 

# Run the server using the command: uvicorn myapp:app --reload