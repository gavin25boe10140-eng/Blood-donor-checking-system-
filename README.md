# Blood Donor Screening System

**Python Console Application | Academic Project**

A command-line tool that automates initial eligibility screening for blood donors based on age, weight, and medical history.

## Problem Statement

Manual screening of blood donors is time-intensive. This project automates basic eligibility checks to reduce screening time and ensure consistent application of criteria.

**Concepts Applied**: Functions, Loops, Conditionals, Exception Handling, Input Validation

## Features

- **Input Validation**: Try-except blocks prevent crashes from invalid inputs
- **Age Check**: Validates 18-65 years eligibility range
- **Weight Verification**: Ensures minimum 50kg requirement
- **Medical Questionnaire**: Screens for recent donations, illness, tattoos/piercings, and medication
- **Continuous Operation**: Process multiple candidates in one session

## Technical Implementation

**Language**: Python 3.x  
**Key Concepts**: Functions, exception handling, control flow (if-else, while, for loops), string methods

### Program Flow
```
Input Age → Validate → Input Weight → Validate → Medical Questions → Result
```
**Fail-Fast Logic**: Immediate rejection at any failure point saves time.

## How to Run

```bash
python "Blood Donor Checking System.py"
```

## Sample Output

```
[ STARTING DONOR VALIDATION ]
Step 1: Enter candidate age: 25
Step 2: Enter candidate weight (kg): 68

Please reply 'y' or 'n' to the items below:
Recent blood donation (within 90 days)? n
Signs of illness (fever/flu) present? n
New tattoos or piercings (last 6 months)? n
Currently using antibiotic medication? n

-----------------------------------
RESULT: PRE-SCREENING PASSED
Candidate is cleared for hemoglobin test.
-----------------------------------
```

## Future Enhancements

- Export data to CSV/database
- Build GUI using Tkinter
- Generate unique donor IDs
- Add appointment scheduling
- Create analytics dashboard

## Learning Outcomes

- Writing reusable functions
- Implementing error handling
- Working with loops and conditionals
- Validating user input
- Real-world problem solving

