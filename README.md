# SauceDemo UI Automation

## 📌 Overview
This project contains an automated test suite for the [SauceDemo](https://www.saucedemo.com/) application.  
It demonstrates UI automation using **Selenium WebDriver + Pytest** with the Page Object Model (POM) design pattern.

The suite covers:
- Login scenarios (valid/invalid)
- Inventory actions (add to cart, sorting)
- Checkout flows (success, missing info)
- Cart navigation and logout

---
## 🚀 Continuous Integration (CI)

This project can be integrated into a CI pipeline so tests run automatically on every push or pull request.

### 🔹 GitHub Actions
`.github/workflows/ui-tests.yml`:

```yaml
name: UI Tests

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  test:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout repository
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.11'

      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt

      - name: Install Chrome
        run: |
          sudo apt-get update
          sudo apt-get install -y google-chrome-stable

      - name: Run tests (headless)
        run: |
          pytest tests/ --html=report.html --self-contained-html

      - name: Upload HTML report
        uses: actions/upload-artifact@v4
        with:
          name: pytest-report
          path: report.html

## Project Structure
saucedemo-ui-automation/
│
├── pages/                # Page Object classes
│   ├── base_page.py
│   ├── login_page.py
│   ├── inventory_page.py
│   ├── cart_page.py
│   └── checkout_page.py
│
├── tests/                # Test cases
│   ├── test_login.py
│   ├── test_inventory.py
│   ├── test_checkout.py
│   └── test_sorting.py
│
├── utils/                # Helpers (driver setup, waits, etc.)
│   └── driver_setup.py
│
├── conftest.py           # Shared pytest fixtures (driver)
└── requirements.txt      # Python dependencies

Code
---

## ⚙️ Setup Instructions
1. Clone the repository:
   ```bash
   git clone https://github.com/<your-username>/saucedemo-ui-automation.git
   cd saucedemo-ui-automation

Install dependencies:
pip install -r requirements.txt
Ensure you have Google Chrome installed and a matching ChromeDriver available in your PATH.
(You can download ChromeDriver from chromedriver.chromium.org)


Run all tests:
Bash-
pytest tests/
pytest tests/test_checkout.py
Generate an HTML report:
pytest --html=report.html

Test Coverage
Login: valid login, invalid login, empty credentials

Inventory: add product to cart, sorting products

Checkout: successful checkout, missing info error

Cart: navigation to checkout, remove item

Logout: return to login page

Notes-
Tests use the Page Object Model for maintainability.

The conftest.py file provides a shared driver fixture for all tests.

Assertions are case‑insensitive to match SauceDemo’s UI messages.

Timeout handling to ensure elements are visible before interaction.



