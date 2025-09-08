from src.driver import Driver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Data_Retrival():
    def __init__(self):
        self.driver = Driver()
    
    def get_problem_statement(self, url):
        
        driver = self.driver.setup_driver()
        
        driver.get(url)
        wait = WebDriverWait(driver, 15)
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, "problemindexholder")))
        
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        
        problem_statement = soup.find('div', class_="problem-statement")

        return problem_statement.get_text()