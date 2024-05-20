#from docx import Document
import PyPDF2
from YaGPT import GPT
import random
import re
import json

class QuestionGenerator:

    # функция генератор одиночного вопроса
    def generation(self, chunks, type_generation, question_number):
        return result.append(GPT(chunks[question_number], type_generation))

    #фуекция генератор списка вопросов
    def main_generator(self, chunks, number, type_generation):
        result = []

        if number <= len(chunks):
            # генерируем числа
            unique_numbers = random.sample(range(len(chunks)), number)
            for i in unique_numbers:
                result.append(GPT(chunks[i], type_generation))
        else:
            print("Для генерации " + str(number) + " недостаточно текста")
            for i in chunks:
                result.append(GPT(i, type_generation))

        return(result)

    '''
    def read_docx(self, file_path):# Открытие документа .dox
        doc = Document(file_path)
        full_text = []
        for para in doc.paragraphs:
            full_text.append(para.text)
        return '\n'.join(full_text)
    '''
    #функция для копирования текста из страниц .pdf
    def extract_text_from_pages(self, pdf_path, start_page, end_page):
        extracted_text = ""
        with open(pdf_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            num_pages = len(reader.pages)
            if start_page < 0 or start_page >= num_pages:
                print("Start page is out of range.")
                return ""
            if end_page < 0 or end_page >= num_pages:
                print("End page is out of range.")
                return ""

            for page_num in range(start_page, end_page + 1):
                page = reader.pages[page_num]
                extracted_text += page.extract_text()

        result = json.loads(extracted_text)
        json_str_no_newlines = json.dumps(result, separators=(',', ':'))
        return json.loads(json_str_no_newlines)

    def split_text_into_chunks(self, text, chunk_size):# Разбиение текста по n словам
        words = text.split()
        chunks = [' '.join(words[i:i + chunk_size]) for i in range(0, len(words), chunk_size)]
        return chunks

    #функция для копирования текста из страниц .pdf
    def extract_text_from_pages(self, pdf_path, start_page, end_page):
        extracted_text = ""
        with open(pdf_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            num_pages = len(reader.pages)
            if start_page < 0 or start_page >= num_pages:
                print("Start page is out of range.")
                return ""
            if end_page < 0 or end_page >= num_pages:
                print("End page is out of range.")
                return ""

            for page_num in range(start_page, end_page + 1):
                page = reader.pages[page_num]
                extracted_text += page.extract_text()

        return extracted_text
'''
question_generator = QuestionGenerator()
file_path = 'C:/Users/p_kar/OneDrive/Рабочий стол/Папки/Python/ОПД/тест2.pdf'
#text = question_generator.read_docx(file_path)
start_page = 2
end_page = 4
text = question_generator.extract_text_from_pages(file_path, start_page, end_page)
chunk_size = 500  # Задаем размер отрезка в словах
chunks = question_generator.split_text_into_chunks(text, chunk_size)

#генератор списка вопросов
number = 5
type_generation = 0
result = question_generator.main_generator(chunks, number, type_generation)

#генератор одиночного вопроса
question_number = 0
result2 = question_generator.generation(chunks, type_generation, question_number)
print(result)


text = ''
nom = 0
for i in result:
  nom += 1
  text = "№ " +str(nom)+":"
  for n in i:
    if n !="n":
      text += n
    else:
      print(text)
      text = ''
  print(text)
  '''