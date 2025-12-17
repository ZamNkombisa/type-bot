from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# 1. Setup Edge Options
edge_options = Options()
# This keeps the browser open after the script finishes
edge_options.add_experimental_option("detach", True)

# 2. Initialize the Edge Driver
service = Service(EdgeChromiumDriverManager().install())
driver = webdriver.Edge(service=service, options=edge_options)

try:
    # 3. Test on Google
    driver.get("https://www.google.com")
    print("Edge is running!")

    # Find search box and type
    # (Note: Google sometimes shows a cookie popup first)
    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys("Edge automation is working!")
    search_box.send_keys(Keys.RETURN)

except Exception as e:
    print(f"An error occurred: {e}")

# We removed driver.quit() so you can see the result