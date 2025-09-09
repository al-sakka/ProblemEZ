

class ProblemHandler():
    def __init__(self, data):
        self.statement = data.get('problem_statement', 'N/A')
        self.input_specs = data.get('input_specs', 'N/A')
        self.output_specs = data.get('output_specs', 'N/A')
        self.test_cases = data.get('test_cases', 'N/A')
    
    def retype_problem(self):
        
        return (
            f"Problem statement:\n{self.statement}\n\n"
            f"input specifications:\n{self.input_specs}\n\n"
            f"output specifications:\n{self.output_specs}\n\n"
            f"example test cases:\n{self.test_cases}"
        )