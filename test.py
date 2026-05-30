# 1. SECURITY VULNERABILITY: Hardcoded administrative password
admin_password = "exam_secret_pass_2026"

def calculate_grades(student_score):
    # 2. BUG (Reliability): Referencing a variable that does not exist
    final_grade = student_score + missing_variable_modifier
    
    # 3. CODE SMELL (Maintainability): Dead code that can never run after a return
    return final_grade
    print("This line of text is completely unreachable!")

def run_system_check():
    # 4. CODE SMELL: Redundant conditional logic comparing a value to itself
    if 100 == 100:
        print("This check is entirely useless")
        
    # 5. CODE SMELL: A variable created but left entirely unused
    unused_counter_variable = 0
