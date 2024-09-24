from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

from PIL import Image, ImageChops #for image capture
import os

def perform_login(driver):

    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.CSS_SELECTOR,".submit-button.btn_action").click() 
    #assert if product page displayed or not after login
    title = driver.find_element(By.XPATH, "//*[contains(text(),'Products')]").text
    assert title in "Products"

def sort_name(driver, dropdown_list):
    #sort products by Name(Z-A)
    select = Select(dropdown_list)
    select.select_by_index(1)

    #get titles of all listed products
    title_elements = driver.find_elements(By.XPATH, "//div[@data-test='inventory-item-name']")
    titles = [title.text for title in title_elements]
    print(f"Extracted title: {titles}")

    sorted_title = sorted(titles, reverse=True)   #sort the fetched title text
    print(f"Sorted title: {sorted_title}")

    # Verify if the titles are already in Z-A order
    if titles == sorted_title:
        print("Titles are in Z-A order.")
    else:
        print("Titles are NOT in Z-A order.")

def sort_price(driver):
     # Re-fetching the dropdown list separately here because it was throwing stale element exception
    dropdown_list = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, "//*[@data-test='product-sort-container']"))
    )
    #sort products by index
    select = Select(dropdown_list)
    select.select_by_index(3)

    #get price of all listed products
    price_elements = driver.find_elements(By.XPATH, "//div[@data-test='inventory-item-price']")

    # Extract and convert the text of each price to a float (handling currency symbols and commas)
    prices = []
    for price in price_elements:
        price_text = price.text.strip() #get text and remove extra spaces
        price_text = price_text.replace('$','').replace(',','') #remove $ and comma
        prices.append(float(price_text)) #convert to float and append to list.
    print(f"Extracted prices: {prices}")

    sorted_price = sorted(prices, reverse=True)  #sort the fetched prices from high to low
    print(f"Sorted price: {sorted_price}")

    # Verify if the price are already in high to low order
    if prices == sorted_price:
        print("Prices are in high-low order.")
    else:
        print("Prices are NOT in high-low order.")

def add_cart(driver): #clicking on Add to cart only as further checkout process are not there
    driver.find_element(By.ID, "add-to-cart-sauce-labs-bike-light").click()
    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
    driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()

#Logic to capture screenshot of current page and compare with base image
def capture_image(driver, screenshot_path):
    driver.save_screenshot(screenshot_path)

def compare_images(image1_path, image2_path):
    image1 = Image.open(image1_path)
    image2 = Image.open(image2_path)
    if image1.size != image2.size: #checking if image sizes are same
        print("Images have different sizes!")
        return False
    diff = ImageChops.difference(image1, image2) # Comparing the images here
    
def run_test_in_gui():
    print("Running in GUI mode...")
    # Initialize the Chrome WebDriver and open webpage.
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()
    
    perform_login(driver) #Perform login
    dropdown_list = driver.find_element(By.XPATH, "//*[@data-test='product-sort-container']") #define locator of sort dropdown
    sort_name(driver, dropdown_list) #perfrom sorting by name Z-A
    sort_price(driver) #perfrom sort by price high-low
    
    #capture screenshot after performing above operations and compare it with base imge
    current_screenshot_path = "screenshots/current_screenshot.png"
    baseline_image_path = "screenshots/baseline_image.png"
    capture_image(driver, current_screenshot_path)

    if os.path.exists(baseline_image_path): # Compare with the baseline image
        compare_images(current_screenshot_path, baseline_image_path)
    else:
        print("Baseline image does not exist. Saving current screenshot as baseline.")
        os.rename(current_screenshot_path, baseline_image_path)
    add_cart(driver)  #Add multiple products to cart
    driver.quit()

def run_test_in_headless():
    print("Running in headless mode...")
    # Set up Chrome options to run in headless mode
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Enable headless mode
    chrome_options.add_argument("--window-size=1920x1080")  # Set window size for consistent layout
    chrome_options.add_argument("--disable-gpu")  # Disable GPU acceleration (recommended for Linux)
    chrome_options.add_argument("--no-sandbox")  # Bypass OS security model (useful for CI)

    # Initialize the Chrome WebDriver with headless options
    driver = webdriver.Chrome(options=chrome_options)

    # Open the webpage
    driver.get("https://www.saucedemo.com/")
    perform_login(driver) #Perform login
    dropdown_list = driver.find_element(By.XPATH, "//*[@data-test='product-sort-container']") #define locator of sort dropdown
    sort_name(driver, dropdown_list) #perfrom sort by name Z-A
    sort_price(driver) #perfrom sort by price high-low
    add_cart(driver) #Add multiple products to cart
    driver.quit()

if __name__ == "__main__":
    run_test_in_gui() # First run the script in GUI mode
    run_test_in_headless() # Then run the script in headless mode

