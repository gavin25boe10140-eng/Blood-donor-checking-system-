# Blood Donor Checking System

# Problem Statement

Many blood drives are significantly delayed by the need to manually screen each potential donor. Medical professionals waste much valuable time asking the same preliminary questions to candidates who may be disqualified for something as simple as age, weight, or recent medical history. This manual filtering at the front end causes bottlenecks, adds to the workload of the staff, and elongates waiting times for those who would otherwise be eligible to donate. There is a pressing need for some automated, rapid prescreening tool that weeds out ineligible candidates before they ever reach the clinical testing stage.

# Overview of the Project

The Blood Donor Checking System is a command-line interface desktop application developed to automate preliminary checks required for a person who intends to donate blood.

# In Scope: * Validating numerical age and weight inputs.

assessing medical risk factors through a questionnaire.

Providing immediate "Pass/Fail" feedback with specific rejection reasons.

Looping functionality for the efficient processing of multiple candidates.

# Out of Scope: * Storing donor personal data - this is subject to General Data Protection Regulation/Privacy laws that require special compliance.

Connect to external medical databases.

Performing actual biological tests, such as hemoglobin levels.

# Target Users

Blood Bank Receptionists: To swiftly process walk-in candidates at the front desk.

Volunteer's Donation Camps: A donor in queues to pre-screen through a simple terminal interface.

Potential Donors (Self-Service): Can use the system at a kiosk to check their own eligibility before waiting in line.

# High-level Features

Sequential Logic Validation implements multistep screening of candidates, where candidates need to pass the Age check, falling in the range from 18 to 65 years, and a Weight check of 50 kg and above, saving screening time in the case of users who would be found ineligible.

Medical History Risk Assessment: A Yes/No questionnaire engine which assesses critical exclusion criteria including, but not limited to, recent donations, illnesses, body modifications, and antibiotic use.

Error Handling for Input: Robust input validation to prevent system crashes when non-numeric values are entered for age or weight.

Session Management: Continuous loop architecture that permits immediate validation of a new user by the operator without restarts after a session is concluded.
