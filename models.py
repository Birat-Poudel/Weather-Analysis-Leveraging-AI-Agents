from langchain_google_genai import ChatGoogleGenerativeAI, HarmBlockThreshold, HarmCategory
from dotenv import load_dotenv
import os

load_dotenv()

class Model:

    def google_gemini_pro(self):
        return ChatGoogleGenerativeAI(
            model = "gemini-pro",
            google_api_key = os.getenv("GEMINI_API_KEY"),
            safety_settings = {
                HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: HarmBlockThreshold.BLOCK_NONE,
            },
        )