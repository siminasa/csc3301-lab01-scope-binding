"""
Lab 1 Task 1: LEGB Scope Investigation
CSC3301 Programming Language Paradigms

Complete the function to demonstrate all four LEGB scope levels.
Your output must match the expected format exactly.
"""

# Global scope variable
x = "GLOBAL_X"


def investigate_legb():
    """
    Create a demonstration of all four LEGB scopes.
    
    Expected output (exact):
    Built-in scope: <class 'int'>
    Global scope: GLOBAL_X
    Enclosing scope: ENCLOSING_X
    Local scope: LOCAL_X
    
    Hints:
    - Built-in: 'int', 'str', 'print' are built-in names
    - Global: Variables defined at module level
    - Enclosing: Variables in outer function (for nested functions)
    - Local: Variables defined inside the current function
    """
    # Global scope variable
x = "GLOBAL_X"

def investigate_legb():
    # We define a variable in the enclosing scope (outside inner function)
    enclosing_x = "ENCLOSING_X"
    
    def inner_function():
        # We define a variable in the local scope (inside inner function)
        local_x = "LOCAL_X"
        
        # Demonstrating all four scopes
        print(f"Built-in scope: {int}")  # 'int' is a built-in type
        print(f"Global scope: {x}")  # 'x' is global
        print(f"Enclosing scope: {enclosing_x}")  # 'enclosing_x' is in the outer function
        print(f"Local scope: {local_x}")  # 'local_x' is inside inner function
    
    inner_function()  # Call the inner function to run the demonstration

# This is the entry
    pass


if __name__ == "__main__":
    investigate_legb()
