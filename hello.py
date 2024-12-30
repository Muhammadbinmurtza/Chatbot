from langchain_google_genai import GoogleGenerativeAI
from dotenv import load_dotenv
from fastapi import FastAPI
import os
load_dotenv()
app = FastAPI()

llm= GoogleGenerativeAI(model = "gemini-1.5-flash", api_key= os.getenv("api_google"))

@app.get("/chat")

def api(query : str):
    prompt = """give answer to every query in flirting way
    imagine you are girl and flirting with your boy friend 
    and give answer in more flirting way
    user query:
    """
    response = llm.invoke(query + prompt)
    return response 
