import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


if __name__ == '__main__':
    # make a folder for screenshots called "screenshots"
    os.mkdir('screenshots')
    
    # launch the browser and go go "https://google.com" for no reason
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get('https://google.com')

    # screenshot for proof
    driver.save_screenshot('screenshots/the-screenshot.png')
    print('peepee poopoo')
