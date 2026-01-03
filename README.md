# DSTUDIO Testing

A Selenium-based automated testing framework for testing the contact form functionality on the DSTUDIO website (https://dstudio.com.bd/).

## 📋 Project Overview

This project implements both automated and manual testing for the DSTUDIO contact page. The automated tests utilize Selenium WebDriver with Python and pytest, following the Page Object Model (POM) design pattern for better maintainability and scalability. The project also includes comprehensive manual testing documentation and test cases.

## 🛠️ Tech Stack

- **Python 3.14**
- **Selenium WebDriver** - Browser automation
- **Pytest** - Testing framework
- **WebDriver Manager** - Automatic driver management
- **pytest-html** - HTML test report generation

## 📁 Project Structure

```
DSTUDIO/
├── conftest.py              # Pytest fixtures and hooks
├── contact_page.py          # Page Object Model for contact page
├── test_contact.py          # Test cases for contact form
├── test_suite.py            # Test suite runner
├── pytest.ini               # Pytest configuration
├── reports/                 # Generated HTML test reports
│   └── report.html
├── screenshots/             # Screenshots of failed tests
└── assets/
    └── style.css           # Custom styling for reports
```

## ✨ Features

### Test Automation Features
- **Page Object Model (POM)** design pattern
- **Automatic screenshot capture** on test failures
- **HTML test reports** with detailed results
- **Test markers** for different test categories (smoke, sanity, regression)
- **Session-scoped browser fixture** for efficient test execution
- **Incognito mode** testing

### Test Coverage
The project includes comprehensive test cases for the contact form:

1. **Navigation Test** - Verify contact page navigation
2. **Empty Data Test** - Submit form with empty fields
3. **Invalid Email Test** - Submit form with invalid email format
4. **Missing Name Test** - Submit form without name field
5. **Valid Data Test** - Submit form with valid data

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- Chrome browser installed
- pip (Python package manager)

### Installation

1. Clone the repository:
```bash
git clone <https://github.com/antumarma/DSTUDIO_Testing>
cd DSTUDIO
```

2. Install required dependencies:
```bash
pip install selenium pytest pytest-html webdriver-manager
```

### Required Python Packages

```
selenium>=4.0.0
pytest>=7.0.0
pytest-html>=3.1.0
webdriver-manager>=3.8.0
```

## 📝 Usage

### Running All Tests

```bash
pytest test_contact.py
```

### Running Tests by Marker

Run only sanity tests:
```bash
pytest -m sanity
```

Run only smoke tests:
```bash
pytest -m smoke
```

Run only regression tests:
```bash
pytest -m regression
```

### Running Test Suite with HTML Report

```bash
python test_suite.py
```

This will:
- Execute all tests marked with `@pytest.mark.sanity`
- Generate an HTML report in `reports/report.html`
- Create a self-contained HTML file with all assets embedded

### Viewing Test Results

After running tests, open the generated HTML report:
```
reports/report.html
```

The report includes:
- Test execution summary
- Pass/fail status for each test
- Execution duration
- Environment information
- Screenshots for failed tests (if any)

## 🎯 Test Markers

The project uses pytest markers to categorize tests:

- `@pytest.mark.smoke` - Quick health check tests
- `@pytest.mark.sanity` - Basic functionality tests
- `@pytest.mark.regression` - Complete end-to-end test suite

## 🏗️ Configuration

### Browser Configuration (conftest.py)

The WebDriver is configured with the following options:
- **Incognito mode** for clean test sessions
- **Maximized window** for consistent element visibility
- **Automatic ChromeDriver management** via webdriver-manager
- **Session scope** to reuse browser instance across tests

### Pytest Configuration (pytest.ini)

Defines test markers for organizing test execution:
```ini
[pytest]
markers =
    smoke: smoke tests for quick health check
    sanity: basic functionality tests
    regression: complete end-to-end suite
```

## 📊 Test Reporting

### HTML Reports

The project uses pytest-html plugin to generate detailed HTML reports with:
- Test results summary (passed, failed, skipped)
- Execution time for each test
- Environment information
- Custom descriptions
- Screenshots for failed tests
- Filtering and sorting capabilities

### Screenshot Capture

Failed tests automatically capture screenshots, saved to:
```
screenshots/<test_name>.png
```

## 🔧 Page Object Model

### ContactPage Class

Located in `contact_page.py`, this class encapsulates all interactions with the contact page:

```python
class ContactPage:
    - navigate_to_contact_page()  # Navigate to contact section
    - fill_contact_form()         # Fill form fields
    # Additional methods for form interaction
```

## 📌 Best Practices Implemented

1. **Page Object Model** - Separation of test logic and page interactions
2. **Fixture Reuse** - Session-scoped driver for efficiency
3. **Automatic Cleanup** - Driver quits after all tests complete
4. **Screenshot on Failure** - Automatic debugging assistance
5. **Descriptive Test Names** - Clear test purpose identification
6. **Test Markers** - Organized test execution
7. **HTML Reporting** - Comprehensive test results documentation




