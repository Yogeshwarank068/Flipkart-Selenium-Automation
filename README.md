# Flipkart Website Automation Testing

An end-to-end automated UI testing suite for the **Flipkart** web application built using **Python**, **Selenium WebDriver**, and **PyTest** following the **Page Object Model (POM)** design pattern.

---

##  Project Overview

This project automates key user workflows on Flipkart, including:
- Searching for products via keywords.
- Dynamic scrolling and product item selection from catalog results.
- Handling multi-tab/multi-window switching.
- Interacting with dynamic web components (e.g., SVG-based cart buttons).
- Automated visual verification via screenshot captures at key execution steps.

---

##  Project Architecture (Page Object Model)

The project follows a clean separation of concerns:
- **Pages**: Contains web elements and specific user interactions for each page.
- **Tests**: Contains test cases, assertions, and test flow execution using PyTest.

```text
Flipkart-website-automation/
├── Pages/
│   └── Search_product.py       # Locators & interaction methods for search and product pages
├── Test/
│   └── test_searchproduct.py   # Test execution scripts & assertions
├── screenshots/                # Captured screenshots during execution (search, item, cart)
├── pytest.ini                  # PyTest configuration settings
└── README.md                   # Project documentation

**## Tech Stack & Prerequisites**

Language: Python 3.9+
Test Framework: PyTest
Browser Automation: Selenium WebDriver (supports Edge / Chrome)
Design Pattern: Page Object Model (POM)

