from src.data_retrival import Data_Retrival

if __name__ == "__main__":
    data = Data_Retrival()
    url = input("Enter problem url: ")
    print(data.get_problem_statement(url))