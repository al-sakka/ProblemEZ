import undetected_chromedriver as uc

class Driver:
    def __init__(self):
        self.options = uc.ChromeOptions()
        
        # DO NOT use headless mode - Cloudflare blocks headless browsers!!
        # options.add_argument('--headless')
        
        self.options.add_argument('--no-sandbox')
        self.options.add_argument('--disable-dev-shm-usage')
        self.options.add_argument('--disable-gpu')
        self.options.add_argument('--window-size=600,800')
        
        self.browser_executable_path = '/usr/bin/chromium-browser'
        
        self.options.binary_location = self.browser_executable_path
        
    def setup_driver(self):
        
        driver = uc.Chrome(
            options = self.options,
            browser_executable_path = self.browser_executable_path
        )
        
        return driver