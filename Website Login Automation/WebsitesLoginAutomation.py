###############################################################
####                                                       ####
####                                                       ####
####     Automatic College Canvas Login                    ####
####                By Rhyan                               ####
####                                                       ####
###############################################################


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import yaml
import os

directory = os.path.dirname(os.path.abspath(__file__))
file_name = "loginDetails.yml"
file_path = os.path.join(directory, file_name)
chromedriver_path = os.path.join(directory, "chromedriver.exe")


# Create a Service object with the path to chromedriver
chrome_service = Service(chromedriver_path)

# Initialize the Chrome WebDriver with the specified Service object
driver = webdriver.Chrome(service=chrome_service)

def login(url,usernameId,username,passwordId,password,submit_buttonId):
    driver.get(url)
    driver.find_element(By.ID, usernameId).send_keys(username)
    driver.find_element(By.ID, passwordId).send_keys(password)
    driver.find_element(By.ID, submit_buttonId).click()

try:
    #load yaml file
    with open(file_path, 'r') as f:
        data = yaml.safe_load(f) 
    
        elcoEm = data.get('el_user', {}).get('email')
        elcops = data.get('el_user', {}).get('password')

        if elcoEm and elcops:
            # Had to change the Identifiers for the webpage.
            login("https://Websiteurl.com", "userNameInput", elcoEm, "passwordInput", elcops, "submitButton")
        else:
            print("Email or password not found in the YAML file.")
finally:
    print("Script completed. Press Enter to close the browser.")
    input()  