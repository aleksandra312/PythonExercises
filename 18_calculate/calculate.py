def calculate(operation, a, b, make_int=False, message='The result is'):
    """Perform operation on a + b, ()possibly truncating) & returning w/msg."""

    if operation == "add":
        res = a + b

    elif operation == "subtract":
        res = a - b 

    elif operation == "multiply":
        res = a * b 

    elif operation == "divide":
        res = a / b 

    else:
        return 
    
    if make_int:
        res = int(res)

    return f"{message} {res}"