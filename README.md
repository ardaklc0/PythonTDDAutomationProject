# Python TDD Automation Project

This project is a Test-Driven Development (TDD) test automation framework using Python, Pytest, and Selenium.

## Project Structure

The repository is organized as follows:

- **`tests/`**: Contains the test files (e.g., `login_test.py`) that define test cases using pytest.
- **`pages/`**: Implements the Page Object Model (POM) design pattern. Each file corresponds to a web page (e.g., `loginPage.py`, `homePage.py`) and contains locators and methods to interact with that page.
- **`utils/`**: Contains utility scripts and constants (e.g., `utils.py` for URL, credentials, and helper functions).
- **`reports/`**: Directory where test reports (like Allure results) are generated.
- **`screenshots/`**: Stores screenshots captured during test failures.
- **`drivers/`**: Directory for browser drivers (though `webdriver-manager` is used to manage them automatically).
- **`conftest.py`**: Pytest configuration file that defines fixtures (e.g., browser setup/teardown) and command-line options.
- **`BUILD.md`**: Detailed instructions on how to set up the environment and run the tests.
- **`requirements.txt`**: List of Python dependencies required for the project.

## Getting Started

Please refer to [BUILD.md](BUILD.md) for detailed instructions on how to install dependencies and run the tests.
