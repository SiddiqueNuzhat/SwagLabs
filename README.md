**Selenium Automation Test for Swag Labs**

This repository contains a Selenium WebDriver test script for automating the sorting of products by name (Z-A) and price (high-low) on the Swag Labs platform. The script also performs visual testing by capturing screenshots and comparing them with a baseline image.

**Prerequisites**
Before you can run this project locally, ensure you have the following installed on your machine:

1. **Python 3.x**: Ensure Python is installed and added to your system's PATH.
2. **Google Chrome:** The latest version of Google Chrome browser.
3. **ChromeDriver:** A compatible version of ChromeDriver that matches your Chrome browser version. Download it from here.
4. **Selenium WebDriver:** Install Selenium by running the following command:
   ** pip install selenium**
5. **Pillow:** Install the Pillow library for image comparison and capture
  **  pip install Pillow**

**Setting Up and Running the Tests**
1. **Clone the Repository:** Clone this repository to your local machine using the following command:
    ** git clone <repository_url>
     cd <repository_directory>**
2. **Download ChromeDriver:** Ensure you download the ChromeDriver for your specific Chrome browser version. Set the path of the ChromeDriver in the script if it's not globally accessible.
3. **Running the Tests in GUI Mode** : The script first runs the tests in normal GUI mode. To execute the tests:
    ** python rtcamp.py**
4. **Running the Tests in Headless Mode**: After running in GUI mode, the script automatically runs the tests in headless mode, but you can modify it to run only in headless mode.
     The run_test_in_headless() function will run the tests without opening a browser window.
5. **Screenshots and Visual Testing**: The script captures screenshots and compares them with a baseline image. Screenshots are saved in the screenshots/ folder. If no baseline image exists, the current screenshot is saved as the baseline.
6. **Test Execution Logs/Reports**: All actions performed in the test, such as sorting by name and price, and screenshot comparisons, are printed to the console. To capture these logs in a file, you can redirect the output:
  **python rtcamp.py > test_execution.log**

**Audio-Video Recording of Execution**
To capture video and audio recording of the test execution (both GUI and headless modes), you can use screen recording software Nimbus or built-in tools for your operating system. I have used Nimbus.
Note: I have added waits in the script to record video for better visibility and then removed it. You can add time.sleep(2) before each method and it will halt for few seconds before proceeding for next action.
