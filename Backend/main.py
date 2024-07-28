from fastapi import FastAPI, File, UploadFile
from PyPDF2 import PdfReader
from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
import uvicorn
import aiofiles
import os


model = OllamaLLM(model="llama3")
template = """
Summarize the text below.
Test: {Input_Text}
Summary:
"""


app = FastAPI()


@app.post("/upload-file")
async def index(file: UploadFile = File(...)):
    print(file.file)
    local_file_path = 'Data/' + file.filename
    async with aiofiles.open(local_file_path, 'wb') as f_obj:
        content = await file.read()
        await f_obj.write(content)
    summarized_text = ""
    reader = PdfReader(local_file_path)
    number_of_pages = len(reader.pages)
    for page_num in range(0, number_of_pages):
        page = reader.pages[0]
        text = page.extract_text()
        prompt = ChatPromptTemplate.from_template(template=template)
        chain = prompt | model
       ## summarized_text += chain.invoke({"Input_Text": text})
    os.remove(local_file_path)
    return {"Summary": summarized_text}


if __name__ == "__main__":
    directories = os.listdir()
    if 'Data' not in directories:
        os.mkdir("Data")
    uvicorn.run(app, host='127.0.0.1', port=8000)
