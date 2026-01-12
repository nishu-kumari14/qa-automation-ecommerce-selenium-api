# Manual Test Cases - E-Commerce Website (SauceDemo)

## Scope
This test suite covers authentication, cart operations, checkout flow, and logout behavior for https://www.saucedemo.com.

## Test Cases

| TC ID | Module | Title | Preconditions | Test Data | Steps | Expected Result | Priority | Severity |
|---|---|---|---|---|---|---|---|---|
| TC-001 | Login | Verify successful login with valid credentials | User is on login page | Username: standard_user, Password: secret_sauce | 1. Enter valid username 2. Enter valid password 3. Click Login | User is redirected to inventory page | High | Critical |
| TC-002 | Login | Verify login fails for locked user | User is on login page | Username: locked_out_user, Password: secret_sauce | 1. Enter locked user credentials 2. Click Login | Error message for locked user is displayed | High | High |
| TC-003 | Login | Verify login fails for invalid password | User is on login page | Username: standard_user, Password: wrong_pass | 1. Enter valid username 2. Enter invalid password 3. Click Login | Error message is displayed and login is blocked | High | High |
| TC-004 | Login | Verify required validation for empty credentials | User is on login page | Username: blank, Password: blank | 1. Leave username and password empty 2. Click Login | Validation error appears for missing credentials | Medium | Medium |
| TC-005 | Add to Cart | Verify single product can be added to cart | User is logged in | Product: Sauce Labs Backpack | 1. Click Add to cart for selected product 2. Open cart | Selected product appears in cart and cart badge shows 1 | High | High |
| TC-006 | Add to Cart | Verify multiple products can be added to cart | User is logged in | Products: Backpack, Bike Light | 1. Add two products 2. Open cart | Both products are listed and cart badge shows 2 | Medium | Medium |
| TC-007 | Add to Cart | Verify product can be removed from cart | User has at least one product in cart | Product: Sauce Labs Backpack | 1. Open cart 2. Click Remove for product | Product is removed from cart and badge updates | Medium | Medium |
| TC-008 | Checkout | Verify user can navigate to checkout from cart | User has at least one item in cart | N/A | 1. Open cart 2. Click Checkout | User is redirected to checkout information page | High | High |
| TC-009 | Checkout | Verify checkout information page validation | User is on checkout info page | First Name: blank, Last Name: QA, Zip: 500001 | 1. Keep first name empty 2. Fill other fields 3. Click Continue | Validation error appears for missing first name | High | Medium |
| TC-010 | Checkout | Verify successful order placement | User has at least one item in cart | First Name: Hemanth, Last Name: QA, Zip: 500001 | 1. Fill checkout info 2. Click Continue 3. Click Finish | Order success message "Thank you for your order!" is displayed | High | Critical |
| TC-011 | Checkout | Verify checkout cannot proceed with empty cart | User is logged in with empty cart | N/A | 1. Open cart 2. Try to proceed logically to checkout without item | Checkout should not complete without any item | Medium | Medium |
| TC-012 | Logout | Verify user can log out successfully | User is logged in | N/A | 1. Open menu 2. Click Logout | User is redirected to login page | High | High |
| TC-013 | Logout | Verify session is restricted after logout | User has logged out | Inventory URL | 1. Logout 2. Use back button or inventory URL | User is not allowed to use authenticated inventory session | Medium | Medium |
| TC-014 | Navigation | Verify cart icon opens cart page | User is logged in | N/A | 1. Click cart icon in header | Cart page is displayed | Low | Low |
| TC-015 | UI/Content | Verify inventory page loads product list | User is logged in | N/A | 1. Login 2. Observe product listing | Product grid is visible with item names, prices, and action buttons | Low | Low |

## Traceability Tags
- AUTH: TC-001, TC-002, TC-003, TC-004
- CART: TC-005, TC-006, TC-007, TC-014
- CHECKOUT: TC-008, TC-009, TC-010, TC-011
- SESSION: TC-012, TC-013
- UI: TC-015
