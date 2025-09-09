from google.genai import types
from google import genai
from utils.prompts import user_prompt, system_prompt
from src.problem_handler import ProblemHandler
import os

class AI_Agent():
    def __init__(self, data):
        self.api_key = os.getenv("GEMINI_API_KEY")
        self.client = genai.Client(api_key=self.api_key)
        self.problem_handler = ProblemHandler(data)
    
    def _format_data(self):
        formatted_problem = self.problem_handler.retype_problem()
        # print(formatted_problem)
        
        return formatted_problem

    def get_agent_response(self):
        
        response = self.client.models.generate_content(
            model = "gemini-2.5-pro",
            
            config = types.GenerateContentConfig(
                system_instruction = system_prompt
            ),
            
            contents = user_prompt + self._format_data()
        )

        return (response.text)
    
    
    def agent_conversation (self, input):
        chat = self.client.chats.create(
            model = "gemini-2.5-pro"
        )
        
        response = chat.send_message(input)
        