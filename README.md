# Blood Donor Checking System

# Overview of the Project

The Blood Donor Checking System is a command-line interface application that aims to automate the initial checking process for blood donors. It will ensure that the candidates comply with necessary health and safety criteria before going into clinical testing such as hemoglobin tests, among others. This tool streamlines the donation process by filtering out ineligible donors early due to standard medical guidelines on age, weight, and recency of medical treatment.

# Features

Age Validation: Automatically validates whether or not the donor is within the eligible age bracket between 18 and 65 years.

Weight Verification: Verifies that the donor's body mass is at least 50kg.

Risk Factor Assessment: Interactive questionnaire checking for:

Recent blood donations (within 90 days).

Signs of current illness: fever/flu.

Recent body modifications within the past 6 months (tattoos/piercings)

Current use of antibiotics.

Real-time Feedback: Immediately provides feedback, such as "Rejected" or "Deferred," and gives specific reasons if a user fails a check.

Continuous Operation: Enables the screening of several candidates in one session without having to restart the program.

# Tools/Technologies Used

Programming Language: Python 3.x

Standard Libraries: sys for system exit operations

Interface: Console / Command Line Interface (CLI)

Steps to Install & Run the Project

Requirements: You should have Python 3 available on your machine. You can check that by running:

python --version


Download : Download the file Blood Donor Checking System.py to your local machine.

Run the Application Run the following in your terminal or command prompt, making sure you're in the directory containing the file:

python "Blood Donor Checking System.py"


# Testing Instructions
You can run the following test cases to verify the functionality of the system:

Test Case 1: Successful Donor

Run the program.

Enter Age: 25

Enter Weight: 60

Answer n to all risk factor questions.

Expected Result: RESULT: PRE-SCREENING PASSED

Test Case 2: Age Rejection

Run the program.

Enter Age: 17

Expected Output: >> Status: Rejected. Age requirement (18-65) not met.

Test Case 3: Weight Rejection

Run the program.

Enter Age: 30

Enter Weight: 45

Expected Output: >> Status: Rejected. Weight is below 50kg limit.

Test Case 4: Medical Deferral

Run the program.

Enter valid age and weight.

Answer y to "Recent blood donation?". Expected Result: >> Status: Deferred based on medical history.
