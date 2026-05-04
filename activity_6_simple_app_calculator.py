# The "Engine" Layer (Inheritance)

class MathOperation:
    """Base class for all math logic."""
    def execute(self, a: float, b: float) -> float:
        raise NotImplementedError("Each operation must define its own execute method.")
    
    class Adder(MathOperation):
     def execute(self, a, b): return a + b

    class Subtractor(MathOperation):
     def execute(self, a, b): return a - b

    class Multiplier(MathOperation):
     def execute(self, a, b): return a * b

    class Divider(MathOperation):
     def execute(self, a, b):
      if b == 0:
        raise ZeroDivisionError("Division by zero is mathematically undefined.")
        return a / b
      
      # The "Application" Layer

    class UniqueCalculator:
     def __init__(self):
       
      # Mapping choices to specific inherited classes

        self._registry = {
            "1": ("Addition", Adder()),
            "2": ("Subtraction", Subtractor()),
            "3": ("Multiplication", Multiplier()),
            "4": ("Division", Divider())
        }
        
     def _get_number(self, prompt: str) -> float:
        """Helper function to handle numeric input exceptions."""
        while True:
            try:
                return float(input(prompt))
            except ValueError:
                print("Invalid input. Please enter a numerical value.")
    
