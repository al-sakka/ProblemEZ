from src.data_retrieval import DataRetrieval
from src.agent import AI_Agent
from yaspin import yaspin
import time

class App():
    def __init__(self, url):
        self.url = url
        
    def start_app(self):
        data = DataRetrieval(url=self.url)
        problem_data = data.get_problem_data()
        
        agent = AI_Agent(problem_data)
        
        print("--------------------------------------------------------------------------")
        with yaspin(text="Simplifying problem...", color="cyan") as sp:
            simplified_problem = agent.get_agent_response()
            
            sp.text = "Done."
            sp.ok("✅")
            
            print('\n' + simplified_problem)