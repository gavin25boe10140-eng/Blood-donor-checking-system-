import sys

def prompt_for_value(text_message):
    while True:
        entry = input(text_message)
        try:
            return float(entry)
        except ValueError:
            print(">> Error: Numerical input required.")

def run_screening_process():
    print("\n[ STARTING DONOR VALIDATION ]")
    
    current_years = prompt_for_value("Step 1: Enter candidate age: ")
    
    if current_years >= 18 and current_years <= 65:
        pass
    else:
        print(">> Status: Rejected. Age requirement (18-65) not met.")
        return

    body_mass = prompt_for_value("Step 2: Enter candidate weight (kg): ")
    
    if body_mass >= 50:
        pass 
    else:
        print(">> Status: Rejected. Weight is below 50kg limit.")
        return

    risk_factors = [
        "Recent blood donation (within 90 days)?",
        "Signs of illness (fever/flu) present?",
        "New tattoos or piercings (last 6 months)?",
        "Currently using antibiotic medication?"
    ]

    print("\nPlease reply 'y' or 'n' to the items below:")
    
    for item in risk_factors:
        user_response = input(item + " ").lower().strip()
        
        if user_response == 'y' or user_response == 'yes':
            print(">> Status: Deferred based on medical history.")
            return

    print("\n" + "-"*35)
    print("RESULT: PRE-SCREENING PASSED")
    print("Candidate is cleared for hemoglobin test.")
    print("-" * 35)

while True:
    run_screening_process()
    
    next_action = input("\nValidate another user? (press 'q' to quit): ")
    if next_action == 'q':
        print("System Exiting.")
        sys.exit()