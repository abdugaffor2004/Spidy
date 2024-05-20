from fastapi import FastAPI, File, Form, UploadFile
from fastapi.responses import JSONResponse
from question_generator import QuestionGenerator
import os

app = FastAPI()
UPLOAD_DIRECTORY = "./uploads"
if not os.path.exists(UPLOAD_DIRECTORY):
    os.makedirs(UPLOAD_DIRECTORY)

@app.post("/upload")
async def upload_file(
    file: UploadFile = File(...),
    start_page: str = Form(...),
    last_page: str = Form(...),
    question_amount: str = Form(...)
):
    #filename = generate_filename(contents)
    file_location = os.path.join(UPLOAD_DIRECTORY, file.filename)
    with open(file_location, "wb") as f:
            
            f.write(await file.read())


    question_generator = QuestionGenerator()
    
    text = question_generator.extract_text_from_pages(file_location, int(start_page), int(last_page))
    tokenizd_str = question_generator.split_text_into_chunks(text, 500)
    questions = question_generator.main_generator(tokenizd_str, int(question_amount), 0)
    content = {
        "startPage": questions,
        "lastPage": last_page,
        "questionAmount": question_amount,
        "fileName": file.filename
    }

    return JSONResponse(content)


@app.get('/')
def read_root():
    return JSONResponse({"Hello": "World"}) 

# Run the server using the command: uvicorn myapp:app --reload
