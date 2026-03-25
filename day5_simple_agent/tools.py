def calculator(expression: str):
    try:
        return eval(expression)
    except Exception as e:
        return f"Error: {str(e)}"