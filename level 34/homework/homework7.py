def function(message):
    def inner_function():
        print(f"Inner message: {message}")
    inner_function()

function("Hello")