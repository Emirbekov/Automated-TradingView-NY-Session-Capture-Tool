from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def create_driver():
    """
    Creates NON-headless browser
    Loads user profile
    """
    #Options like maximized
    options = webdriver.ChromeOptions()

    options.add_argument("--start-maximized")

    options.add_argument("--disable-blink-features=AutomationControlled")

    service = Service(ChromeDriverManager().install())

    driver = webdriver.Chrome(
        service = service,
        options = options
    )
    
    return driver
    
