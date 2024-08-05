The application provides a user-friendly interface for uploading documents in various formats (PDF, DOCX, TXT) and receiving concise summaries generated by a locally deployed language model.

## Features

- **File Upload:** Upload documents in various formats.
- **Document Display:** View the uploaded document's content.
- **Summarization:** Receive a summarized version of the document.
- **Concurrency:** Handle multiple concurrent requests efficiently.

## Technologies Used

- **Backend:** FastAPI
- **Frontend:** React.js
- **LLM Deployment:** Ollama with [llama3 model](https://ollama.com/library/llama3)

## Setup and Installation

### Prerequisites

 1. Python 3.8+
 2. Node.js and npm
 3. [Ollama with llama3 model](https://ollama.com/library/llama3)

**Frontend Setup**
Navigate to the frontend directory (DocumentSummarizer/Frontend/) and open command line to follow below instructions

 1. To install requirements - `npm install`
 2. To run the frontend server - `npm start`

Open your browser and navigate to http://localhost:3000 to use the application.

**LLM Deployment**

 1. Installing Ollama - Download Ollama from [here](https://ollama.com/download/mac)
 2. Run following in command line to make sure ollama is installed - `ollama -h`. You should see help menu of Ollama
 3. Run following command to install *llama3* model- `ollama pull llama3 `
 4. Run following to make sure llama3 model is installed and working 
`ollama run llama3  `. You should see a chat window where you can communicate with the llama model.

**Backend Setup**

Navigate to Backend folder (DocumentSummarizer/Backend/) and open the terminal to run following commands -

 1. To install packages - `pip install -r requirements.txt`
 2. To run the backend server - `python main.py`

To verify that server is up and running make sure to load documentations at http://127.0.0.1:8000

You should see swagger documentation once above loads. Test the POST api to make sure 

Project Structure
DocumentSummarizer/
│
├── Backend/
│   ├── main.py
│   ├── requirements.txt
│
├── frontend/
│   ├── src/
│   ├── public/
│   ├── package.json
│   └── package-lock.json
│
└── README.md

Backend/: Contains the backend code (FastAPI).
Frontend/: Contains the frontend code (React.js).

**Submission Requirements**
The repository contains:

 - Backend code (FastAPI)
 - Frontend code (React.js)