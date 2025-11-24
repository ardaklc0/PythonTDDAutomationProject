import pytest
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Type in browser name e.g. chrome OR firefox")

def get_driver_path(path, driver_name):
    if path.lower().endswith(".exe"):
        return path
    # If path is a file but not exe (e.g. LICENSE), get dir
    if os.path.isfile(path):
        path = os.path.dirname(path)
    
    # Look for exe in the directory
    exe_path = os.path.join(path, driver_name)
    if os.path.exists(exe_path):
        return exe_path
    
    # Fallback: search in directory
    for file in os.listdir(path):
        if file.lower() == driver_name.lower():
            return os.path.join(path, file)
            
    raise FileNotFoundError(f"Could not find {driver_name} in {path}")

@pytest.fixture(scope="class")
def test_setup(request):
    browser = request.config.getoption("--browser")

    if browser == 'chrome':
        path = ChromeDriverManager().install()
        real_path = get_driver_path(path, "chromedriver.exe")
        service = ChromeService(real_path)
        driver = webdriver.Chrome(service=service)
    elif browser == 'firefox':
        path = GeckoDriverManager().install()
        real_path = get_driver_path(path, "geckodriver.exe")
        service = FirefoxService(real_path)
        driver = webdriver.Firefox(service=service)

    driver.implicitly_wait(5)
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()
    driver.quit()
    print("Test Completed")