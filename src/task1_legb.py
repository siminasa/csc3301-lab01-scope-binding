"""
Lab 1 Task 1: LEGB Scope Investigation
CSC3301 Programming Language Paradigms

Complete the function to demonstrate all four LEGB scope levels.
Your output must match the expected format exactly.
"""

# Global scope variable
x = "GLOBAL_X"

def investigate_legb():
    enclosing_x = "ENCLOSING_X"

    def inner_function():
        local_x = "LOCAL_X"
        print("Built-in scope:", int)
        print("Global scope:", x)
        print("Enclosing scope:", enclosing_x)
        print("Local scope:", local_x)

    inner_function()

investigate_legb()
