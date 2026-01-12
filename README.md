# QA Automation Project - E-Commerce Website Testing

## Project Overview
This repository demonstrates end-to-end QA coverage for an e-commerce platform using SauceDemo. The project combines manual testing, Selenium automation with Page Object Model, API testing in Postman, and SQL validation queries.

## Target Application
- Web UI: https://www.saucedemo.com
- API: https://reqres.in

## Tech Stack
- Python 3.x
- Selenium WebDriver
- PyTest
- WebDriver Manager
- Postman
- SQL (query documentation)

## Project Structure
```
QA-Automation/
├── testcases/
│   └── manual-test-cases.md
├── automation/
│   ├── pages/
│   │   ├── base_page.py
│   │   ├── login_page.py
│   │   ├── inventory_page.py
│   │   ├── cart_page.py
│   │   └── checkout_page.py
│   └── tests/
│       ├── conftest.py
│       ├── test_login.py
│       ├── test_cart_checkout.py
│       └── test_logout.py
├── api-testing/
│   ├── reqres-collection.json
│   └── reqres-environment.json
├── sql/
│   └── sample-queries.sql
├── requirements.txt
├── pytest.ini
└── README.md
```

## Coverage Summary
- Manual testing: 15 test cases
- UI automation (Selenium + PyTest):
  - Login functionality
  - Add product to cart
  - Checkout flow
  - Logout behavior
  - Negative login validation
- API testing (Postman):
  - GET users
  - POST create user
  - Response validation (status code, payload fields, response time)
- SQL:
  - User and order validation queries

## Setup Instructions
1. Clone the repository.
2. Create and activate a virtual environment.
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Environment Variables (Optional)
The suite includes defaults for SauceDemo credentials, but environment overrides are supported:
- SAUCE_STANDARD_USER
- SAUCE_LOCKED_USER
- SAUCE_PASSWORD
- BROWSER_MODE (headed or headless)

## Run Automation Tests
Headed mode:
```bash
pytest --browser-mode headed
```

Headless mode:
```bash
pytest --browser-mode headless
```

## Test Reports and Failure Screenshots
- HTML report is generated automatically at `reports/pytest-report.html` for every PyTest run.
- Failed UI tests automatically capture screenshots in `screenshots/`.
- Both report and screenshots are uploaded as CI artifacts in GitHub Actions.

## GitHub Actions CI
- Workflow file: `.github/workflows/pytest-ci.yml`
- Trigger: every push (all branches) and manual run.
- Execution: installs dependencies and runs `pytest --browser-mode headless`.
- Artifacts: uploads `reports/` and `screenshots/` after each run.

## Execute API Tests
1. Import `api-testing/reqres-collection.json` into Postman.
2. Import `api-testing/reqres-environment.json` and select it.
3. Run the collection using Postman Collection Runner.

Optional Newman execution:
```bash
newman run api-testing/reqres-collection.json -e api-testing/reqres-environment.json
```

## Manual Testing Artifact
Detailed manual test cases are available in:
- testcases/manual-test-cases.md

## SQL Artifact
Sample validation queries are available in:
- sql/sample-queries.sql

## Future Enhancements
- Add CI pipeline with GitHub Actions
- Integrate HTML test reports
- Add cross-browser coverage (Firefox/Edge)
- Add screenshot capture on test failure
