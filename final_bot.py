import time
import random
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# =========================================================
# CONFIGURATION
# =========================================================
DRIVER_PATH = r"C:\Users\ZamuxoloNkombisa-Int\Desktop\type_bot\msedgedriver.exe"
TARGET_URL = "https://somewheretypingtest.com/test"

# Typing Speed
MIN_DELAY = 0.02 
MAX_DELAY = 0.05 

# 1. Initialize Driver
service = Service(executable_path=DRIVER_PATH)
driver = webdriver.Edge(service=service)

def start_typing():
    try:
        driver.get(TARGET_URL)
        print("Waiting for you to reach the test stage...")

        # --- STAGE 1: SEARCH FOR THE TEXTAREA ---
        # We use a CSS selector that matches the start of your class list
        textarea_selector = "textarea.notranslate"
        
        while True:
            try:
                # Wait until the textarea actually exists on the page
                typing_box = driver.find_element(By.CSS_SELECTOR, textarea_selector)
                
                # Check if the 'current word' is visible yet
                current_word_element = driver.find_element(By.CSS_SELECTOR, '[data-current="true"]')
                word_to_type = current_word_element.text.strip()
                
                if word_to_type:
                    print(f"Test Started! Targeting word: {word_to_type}")
                    
                    # CLICK the box once to ensure focus
                    typing_box.click()
                    break
            except:
                time.sleep(1)

        # --- STAGE 2: THE TYPING LOOP ---
        while True:
            try:
                # 1. Grab word
                word_element = driver.find_element(By.CSS_SELECTOR, '[data-current="true"]')
                word = word_element.text.strip()
                
                # 2. Type into the specific textarea we found
                for letter in word:
                    typing_box.send_keys(letter)
                    time.sleep(random.uniform(MIN_DELAY, MAX_DELAY))
                
                # 3. Finish word
                typing_box.send_keys(Keys.SPACE)
                
                # 4. Small buffer for site to update
                time.sleep(0.05)
                
            except Exception as e:
                print("Test complete or error occurred.")
                break

    except Exception as outer_e:
        print(f"Outer Error: {outer_e}")

if __name__ == "__main__":
    try:
        start_typing()
    finally:
        print("\nBot finished.")
        input("Press Enter to close browser...")
        driver.quit()