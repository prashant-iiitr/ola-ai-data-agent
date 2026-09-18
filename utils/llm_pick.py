import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()


def pick_llm(level: str):
    model_name = "gemini-3.6-flash"

    if level.lower() == "low":
        model_name = "gemini-3.6-flash"
    elif level.lower() == "medium":
        model_name = "gemini-3.6-flash"
    elif level.lower() == "high":
        model_name = "gemini-3.6-flash"
    else:
        raise ValueError(f"Unsupported level: {level}")

    llm = ChatGoogleGenerativeAI(
        model=model_name,
        google_api_key=os.getenv("GEMINI_API_KEY"),
        temperature=0,
        max_retries=3,
        timeout=60,
    )

    return llm


