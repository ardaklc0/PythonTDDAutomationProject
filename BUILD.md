# Build and Run Instructions

## Prerequisites
- Python 3.x installed
- Chrome or Firefox browser installed

## Setup

1. **Create a Virtual Environment** (Recommended)
   ```bash
   python -m venv venv
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

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
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
pytest --alluredir=reports
```

To view the Allure report:
```bash
allure serve reports
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
