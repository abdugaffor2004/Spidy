#from docx import Document
import PyPDF2
from YaGPT import GPT
import random
import json
import time 
import re
class QuestionGenerator:

    # функция генератор одиночного вопроса
    def generation(self, chunks, type_generation, question_number):
        return GPT(chunks[question_number], type_generation)

    #фуекция генератор списка вопросов
    def main_generator(self, chunks, number, type_generation):
        result = []

        if number <= len(chunks):
            # генерируем числа
            unique_numbers = random.sample(range(len(chunks)), number)
            for i in unique_numbers:
                time.sleep(1)
                result.append(GPT(chunks[i], type_generation))
        else:
            print("Для генерации " + str(number) + " недостаточно текста")
            for i in chunks:
                time.sleep(1)
                result.append(GPT(i, type_generation))

        return(result)

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

    def split_text_into_chunks(self, text, chunk_size, numb):# Разбиение текста по n словам
        while True:
            words = text.split()
            chunks = [' '.join(words[i:i + chunk_size]) for i in range(0, len(words), chunk_size)]
            if len(chunks) < numb:
                chunk_size -= 100
                chunks = [' '.join(words[i:i + chunk_size]) for i in range(0, len(words), chunk_size)]
            else:
                break
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
    
    #поиск всех подстрок между ':' и '?'
    def extract_between_colon_and_question(self, text):  
        pattern = r':(.*?)\?'
        matches = re.findall(pattern, text)
        return matches
    # Находим текст после ':'
    def extract_after_colon(self, text):
        colon_index = text.find(':')
        if colon_index != -1:
            return text[colon_index + 1:].strip()
        else:
            return "Error"
    
    def remove_before_question_mark(self, text):
    
        question_index = text.find('?')
        
        
        if question_index != -1:
            return text[question_index:]
        else:
            
            return text
    