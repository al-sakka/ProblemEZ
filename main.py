from src.data_retrival import Data_Retrival
from src.agent import AI_Agent
from yaspin import yaspin
import time

def main():
    url = input("Enter Problem URL: ")
    
    data = Data_Retrival(url=url)
    problem_data = data.get_problem_data()
    
    agent = AI_Agent(problem_data)
    
    print("--------------------------------------------------------------------------")
    with yaspin(text="Simplifying problem...", color="cyan") as sp:
        simplified_problem = agent.get_agent_response()
        
        sp.text = "Done."
        sp.ok("✅")
        
        print('\n' + simplified_problem)

# Entry Point
if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print("Error: {e}")