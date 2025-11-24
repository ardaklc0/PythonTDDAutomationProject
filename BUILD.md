# Build and Run Instructions

## Prerequisites
- Python 3.x installed
- Chrome or Firefox browser installed
- [Allure Commandline](https://docs.qameta.io/allure/#_installing_a_commandline) installed (required for viewing reports)

## Setup

1. **Run the Setup Script**
   - Windows (PowerShell):
     ```powershell
     .\setup.ps1
     ```
   - macOS/Linux:
     ```bash
     chmod +x setup.sh
     ./setup.sh
     ```

2. **Activate the Virtual Environment**
   - Windows:
     ```powershell
     .\venv\Scripts\Activate.ps1
     ```
   - macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

## Running Tests

### Run All Tests with Pytest
To run all tests using pytest:
```bash
pytest
```

### Run Tests with Specific Browser
To run tests with a specific browser (default is Chrome):
```bash
pytest --browser=chrome
```
or
```bash
pytest --browser=firefox
```

### Run Tests with Allure Reports
To generate Allure reports:
```bash
pytest --alluredir=reports/allure-reports
```

To view the Allure report:
```bash
allure serve reports/allure-reports
```

### Run Specific Test File
To run a specific test file:
```bash
pytest tests/login_test.py
```

### Run Tests in Verbose Mode
To see detailed test output:
```bash
pytest -v
```

### Run Tests with Multiple Options
You can combine options:
```bash
pytest --browser=firefox --alluredir=reports -v
```
