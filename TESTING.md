# Pure Protein Powders - Testing Documentation

![image](https://github.com/MikesCodingCreations/pp5/blob/main/media/website/site.png)

## Compatibility & Responsive Testing
I designed my website to be responsive, ensuring it functions well and looks great across various devices and browsers (see table below for details):

| **Device**                  | **BROWSER** | **SCREEN WIDTH** |
|-----------------------------|-------------|------------------|
| iPhone XS Max               | Safari      | 1284x2778 px     |
| iPhone 7                    | Safari      | 375 x 559 px     |
| Samsung Galaxy              | Chrome      | 412 x 777 px     |
| OnePlus 6T                  | Edge        | 412 x 757 px     |
| Samsung Galaxy A10          | Samsung     | 412 x 734 px     |
| Samsung Galaxy Tab S7       | Chrome      | 753 x 1037 px    |
| iPad Mini 4                 | Safari      | 768 x 954 px     |
| Mac Ventura                 | Safari      | 1920 x 955 px    |
| windows 11                  | Yandex      | 1920 x 955 px    |

## Manual Testing

**TEST Case 1: Home Page**

*Starting url: https://pureproteinpowderpp5-6078f21bc874.herokuapp.com/*

**Steps**
1. Navigate: Head over to the website's homepage.
2. Hero Check: Look for a prominent image at the top of the page. This is often called the "hero image." Make sure it's visually appealing to the website's overall theme.
3. Welcome Message Scan: See if there's a clear and visible message displayed. Verify that the exact wording says "THE PUREST QUALITY PROTEIN IS HERE."
4. Shop Now! Click on the button labeled "SHOP NOW" (or something similar that indicates browsing products).
5. Product Page Landing: Confirm that clicking the button takes you to a page displaying the website's products.

**Expected Outcome:**
- Clean Homepage Load: The homepage should load successfully without any error messages appearing in the browser console.
- Hero & Welcome Presence: Both the hero image and welcome message section should be clearly visible on the homepage.
- Compelling Hero Image: The hero image should be visually attractive and directly related to the website's overall theme.
- Welcome Message Clarity:  The welcome message text should be easily readable and stand out on the homepage.
- hop Now Functionality: Clicking the "SHOP NOW" button should seamlessly redirect the user to the dedicated product page.

**- I verify the expected outcomes all take place.**

<hr>

**TEST Case 2: Registration**

*Starting url: https://pureproteinpowderpp5-6078f21bc874.herokuapp.com/*

**Steps**
1. Registration Page: Navigate to the PureProteinPowder's website's registration page.
2. Fill & Submit: Complete the registration form with accurate and unique information (email address, password, etc.). Ensure the information hasn't been used before. Click the "Sign Up" button to submit the form.
3. Confirmation Check: Look for a confirmation message on the screen indicating successful account creation.
4. Account Creation Success: Verify that a new user account has been created successfully. This might involve checking your email for a verification link or seeing a success message on the website itself.
5. Login with New Credentials:  Use the newly created username (or email) and password to log in to the PureProteinPowder's website.
6. Authenticated User Access: After logging in, confirm that you're redirected to a page specifically designed for authenticated users (e.g., account dashboard, profile page).

**Expected Outcome:**
- Registration Form: The registration page offers a form for new users to create accounts. This form includes fields that users must fill out (often marked as "required").
- Successful Registration: When you enter valid and unique user information and click "Sign Up," the form submits successfully. You should see a confirmation message on the screen indicating that your account creation request has been accepted.
- Verification Process: You will need to verify your account through a process like clicking a verification link sent to your email. After successful verification, your new user account is officially created.
- Error Handling: If you try to register with an email address already in use, the system will display an error message to prevent duplicate accounts.
- Similarly, if you enter invalid information (weak passwords, missing fields, etc.), the system will display relevant error messages to help you correct the information and try again.

**- I verify the expected outcomes all take place.**

<hr>

**TEST Case 3: Login**

*Starting url: https://pureproteinpowderpp5-6078f21bc874.herokuapp.com/*

**Steps:**
1. Navigate to Login: Head over to the PureProteinPowder's website's login page.
2. Enter Credentials: Fill in the login form with the username and password of an existing user account (ensure they're valid).
3. Submit and Authenticate: Click the "Login" button to submit the form. The website should then authenticate your credentials.
4. Success Verification: Look for a success message on the screen that confirms a successful login. This message should ideally include the text "Successfully signed in as (USERNAME)," replacing "(USERNAME)" with your actual username.
5. Verify: Verify that you're redirected to the homepage specifically designed for authenticated users.

**Expected Outcome:**
- The login page should provide a clear login form with username and password fields.
- Submitting the form with valid credentials should successfully authenticate the user.
- A clear success message mentioning the logged-in username should appear.
- The website should maintain your login session, allowing access to authenticated features and pages without requiring repeated logins.

**- I verify the expected outcomes all take place.**

<hr>

**TEST Case 4: Products**

*Starting url: https://pureproteinpowderpp5-6078f21bc874.herokuapp.com/*

**Steps:**
1. Products Await: Navigate to the PureProteinPowder's Products page either through the "SHOP NOW" button in the homepage or via the products navbar link.
2. Product Exploration: Browse through the available protein or activewear products listed on the page.
3. Deep Dive: Click on a specific product's image or title to view its detailed information page.

**Expected Outcome:**
- The Products page should load without any error messages popping up in your browser's console.
- The list of available protein products should be displayed clearly and accurately.
- Clicking on a product image or title should seamlessly take you to the product details page, again without any console errors.
- Throughout this process, there should be no errors reported in the browser console.

**- I verify the expected outcomes all take place.**

<hr>

**TEST Case 5: Product Details**

*Starting url: https://pureproteinpowderpp5-6078f21bc874.herokuapp.com/*

**Steps:**
1. Product Deep Dive: Click on a product image to view its dedicated details page.
2. Details Check: Verify that the product details are displayed correctly, including:
    - Name: The product's clear and accurate name.
    - Size (if applicable): The product's size information, if relevant.
    - Category: The category the product belongs to (e.g., Whey Protein, Vegan Protein, Accessories).
    - Rating: Any user ratings or review stars associated with the product.
    - Description: A comprehensive description detailing the product's features and benefits.
    - Quantity Control: Confirm that the quantity buttons function properly. Clicking the "increment" button should increase the desired amount, while "decrement" should decrease it.
3. Add to Bag: Click the "ADD TO BAG" button to add the chosen product to your shopping bag.
4. Success Confirmation:  Verify that a clear success message appears on the screen, indicating the product has been successfully added to your bag.
5. Shopping Spree Continues: Click the "KEEP SHOPPING" button and confirm that you're redirected back to the main Products page, ready to browse further.

**Expected Outcome:**


**- I verify the expected outcomes all take place.**

<hr>

**TEST Case 6: Wishlist**

*Starting url: https://pureproteinpowderpp5-6078f21bc874.herokuapp.com/*

**Steps:**
1. Peeking into the wishlist: Click on the wishlist (start) icon to access your wishlist details.
2. Wishlist Content Check: Verify that the following wishlist details are displayed accurately:
    - Product Name: The name of each item in your bag.
    - SKU: The unique product identifier (if applicable).
    - Price: The individual price of each product.
3. Making Changes: Verify that the "REMOVE" button successfully removes unwanted items from your bag (without console errors).
4. Shopping Spree Continues: Click on the "KEEP SHOPPING" button and confirm that you're redirected back to the Products page list, ready to add more items to your wishlist.

**Expected Outcome:**
- Clicking the wishlist icon should smoothly display the wishlist details page.
- All wishlist information (product name, SKU, price, wishlist total) should be displayed accurately.
- Clicking "REMOVE" should remove the chosen item from your wishlist without any console errors.
- Clicking "KEEP SHOPPING" should seamlessly return you to the Products page list.

**- I verify the expected outcomes all take place.**

<hr>

**TEST Case 7: Bag**

*Starting url: https://pureproteinpowderpp5-6078f21bc874.herokuapp.com/*

**Steps:**
1. Peeking into the Bag: Click on the shopping bag icon to access your bag details.
2. Bag Content Check: Verify that the following bag details are displayed accurately:
    - Product Name: The name of each item in your bag.
    - SKU: The unique product identifier (if applicable).
    - Price: The individual price of each product.
    - Bag Total: The total cost of all items currently in your bag.
    - Delivery: Any delivery fee associated with your order (may vary depending on options).
    - Grand Total: The combined amount reflecting the bag total and any delivery fees.
3. Quantity Tweaks: Confirm that the quantity buttons function as expected. Clicking "increment" should increase the desired quantity of a product, while "decrement" should decrease it.
4. Making Changes: Verify that the "UPDATE" button allows you to update the bag contents after modifying quantities. Additionally, confirm that the "REMOVE" button successfully removes unwanted items from your bag (without console errors).
5. Ready to Checkout?: Click the "SECURE CHECKOUT" button to proceed to the checkout process, where you can finalize your order.
6. Shopping Spree Continues: Click on the "KEEP SHOPPING" button and confirm that you're redirected back to the Products page list, ready to add more items to your bag.

**Expected Outcome:**
- Clicking the bag icon should smoothly display the bag details page.
- All bag information (product name, SKU, price, bag total, delivery, grand total) should be displayed accurately.
- The quantity buttons should function correctly, allowing you to adjust the amount of each item.
- Clicking "UPDATE" should successfully update your bag after quantity changes.
- Clicking "REMOVE" should remove the chosen item from your bag without any console errors.
- Clicking "SECURE CHECKOUT" should initiate the checkout process.
- Clicking "KEEP SHOPPING" should seamlessly return you to the Products page list.

**- I verify the expected outcomes all take place.**

<hr>

**TEST Case 8: Checkout**

*Starting url: https://pureproteinpowderpp5-6078f21bc874.herokuapp.com/*

**Steps:**
1. Checkout Initiation: Click on the "SECURE CHECKOUT" button to proceed with the checkout process.
2. Order Summary Review: Verify that the order summary details are displayed accurately, including:
    - Product Name: Names of all items you're purchasing.
    - Quantity: The number of units for each product.
    - Subtotal: The price of each item multiplied by its quantity.
    - Order Total: The combined cost of all products in your order.
    - Delivery: Any applicable delivery fees.
    - Grand Total: The final amount reflecting the order total and any delivery fees.
    - Checkout Information:  Fill out the checkout form with your valid user information, including billing and shipping details as required.
3. Refining Your Order (Optional): Click on the "ADJUST BAG" button if you need to make changes to your bag contents before finalizing the order. This button should redirect you back to the bag details page.
4. Order Placement: Once everything looks good, click the "COMPLETE ORDER" button to submit your order and initiate payment processing.
5. Processing Status: A loading spinner icon should appear on the screen, indicating that your order is being processed.
6. Success! Upon successful order completion, you should be redirected to a "checkout_success" page.
7. Confirmation Message: A clear success message should be displayed on the screen, with text like "Order successfully processed!".

**Expected Outcome:**
- Clicking "SECURE CHECKOUT" should initiate the checkout process without any console errors.
- All order summary details (product names, quantities, subtotals, totals, and grand total) should be displayed accurately.
- The checkout form should function correctly, allowing you to fill it with valid user information.
- Clicking "ADJUST BAG" should take you back to the bag details page for revisions.
- Clicking "COMPLETE ORDER" should display a loading spinner while processing the order.
- After clicking "COMPLETE ORDER," you should be redirected to the "checkout_success" page without errors.
- A clear success message confirming successful order processing should be displayed.
- No console errors should occur throughout the checkout process.

**- I verify the expected outcomes all take place.**

<hr>

**TEST Case 9: Checkout success**

*Starting url: https://pureproteinpowderpp5-6078f21bc874.herokuapp.com/*

**Steps:**
1. Checkout Initiation: Click on the "SECURE CHECKOUT" button to proceed with the checkout process.
2. Order Summary Review: Verify that the order summary details are displayed accurately, including:
    - Product Name: Names of all items you're purchasing.
    - Quantity: The number of units for each product.
    - Subtotal: The price of each item multiplied by its quantity.
    - Order Total: The combined cost of all products in your order.
    - Delivery: Any applicable delivery fees.
    - Grand Total: The final amount reflecting the order total and any delivery fees.
    - Checkout Information:  Fill out the checkout form with your valid user information, including billing and shipping details as required.
3. Refining Your Order (Optional): Click on the "ADJUST BAG" button if you need to make changes to your bag contents before finalizing the order. This button should redirect you back to the bag details page.
4. Order Placement: Once everything looks good, click the "COMPLETE ORDER" button to submit your order and initiate payment processing.
5. Processing Status: A loading spinner icon should appear on the screen, indicating that your order is being processed.
6. Success! Upon successful order completion, you should be redirected to a "checkout_success" page.
7. Confirmation Message: A clear success message should be displayed on the screen, with text like "Order successfully processed!".

**Expected Outcome:**
- After successfully completing your order, the "checkout_success" page should load correctly without any errors.
- The checkout success page should display the complete order description with all the information mentioned above (order info, details, delivery address, billing info).
- Clicking the "VIEW MORE OF OUR AMAZING PRODUCTS!" button should seamlessly redirect you to the New Arrivals page.

**- I verify the expected outcomes all take place.**

<hr>

**TEST Case 10: Logged In User**

*Starting url: https://pureproteinpowderpp5-6078f21bc874.herokuapp.com/*

**Steps:**
1. Profile Access: Click on "My Profile" within the account icon. This should redirect you to your dedicated user profile page.
2. Information Check: On your profile page, verify that the following information is displayed correctly:
    - Default Delivery Information: Confirm that your default shipping address is accurate and up-to-date.
    - Order History (if applicable): If you have completed orders, check if your order history is displayed correctly, listing past purchases.
    - Update Your Profile: If any information needs updating, locate the profile editing form. Fill out the form with the new or corrected information.
3. Save the Changes: Click on the button labeled "UPDATE INFORMATION" to submit the changes you made to your profile.
4. Success Confirmation: A success message should appear on the screen after a successful update, typically stating "Profile updated successfully!"

**Expected Outcome:**
- Clicking "My Profile" should seamlessly redirect you to your user profile account page.
- The default delivery information and order history (if you have any) should be displayed accurately on your profile page.
- Updating the profile information using the form and clicking "UPDATE INFORMATION" should successfully update your profile details.
- A clear success message confirming a successful update should be displayed on the screen, typically saying "Profile updated successfully!".

**- I verify the expected outcomes all take place.**

<hr>

**TEST Case 11: Logout**

*Starting url: https://pureproteinpowderpp5-6078f21bc874.herokuapp.com/*

**Steps:**
1. Initiate Logout: Click on "Logout" within the account icon. This should redirect you to a dedicated logout page.
2. Confirm Logout: Click the "SIGN OUT" button on the logout page.
3. Logout Verification: Verify that you are successfully logged out of the website. A message like "You have signed out" should be displayed to confirm this.

**Expected Outcome:**
- Clicking "Logout" in the account icon should redirect you to the logout page.
- Clicking "SIGN OUT" on the logout page should successfully log you out.
- A clear message confirming successful logout, such as "You have signed out," should be displayed on the screen.

**- I verify the expected outcomes all take place.**

<hr>

**TEST Case 000: XXX**

*Starting url: https://pureproteinpowderpp5-6078f21bc874.herokuapp.com/*

**Steps:**
1. 

**Expected Outcome:**
- 

**- I verify the expected outcomes all take place.**

<hr>














## Validation Testing
<details>
<summary>Validation Testing</summary>

Validation testing referenced these resources:

- **[CSS Validator](https://jigsaw.w3.org/css-validator/)**

**CSS Validation**

![image](https://github.com/MikesCodingCreations/pp5/blob/main/media/validation/cssvalidation.png)

<hr>

The following resources were consulted to support validation testing:

- **[HTML Validator](https://validator.w3.org/)**

**HTML Validation**

![image](https://github.com/MikesCodingCreations/pp5/blob/main/media/validation/htmlvalidation.png)

<hr>

</details>
<hr>