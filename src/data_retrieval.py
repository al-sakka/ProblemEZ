from src.driver import Driver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class DataRetrieval():
    def __init__(self, url):
        driver = Driver()
        web_driver = driver.setup_driver()
        web_driver.get(url)
        wait = WebDriverWait(web_driver, 15)
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, "problemindexholder")))
        self.soup = BeautifulSoup(web_driver.page_source, 'html.parser')
        web_driver.quit()  # Close the browser after getting the page source
    
    def get_problem_data(self):
        
        problem_statement = self.soup.find('div', class_="problem-statement").get_text(strip=True)
        input_specs = self.soup.find('div', class_="input-specification").get_text(strip=True)
        output_specs = self.soup.find('div', class_="output-specification").get_text(strip=True)
        test_cases = self.soup.find('div', class_="sample-tests").get_text(strip=True)
    
        data = {
            'problem_statement': problem_statement,
            'input_specs' : input_specs,
            'output_specs' : output_specs,
            'test_cases' : test_cases
        }
        
        return data