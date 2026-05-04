# The "Engine" Layer (Inheritance)

from cProfile import label
from platform import processor
from random import choice
from unittest import result


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

     def start(self):
        """Main loop following the steps in image_9cdf4f.png."""
        print("--- Welcome to the OOP Calculator ---")

        while True:
            print("\nAvailable Operations:")
            for key, (name, _) in self._registry.items():
                print(f"{key}. {name}")
        
        choice = input("Select an operation (1-4): ")

        if choice in self._registry:
            label, processor = self._registry[choice]

            # Input handling

            val1 = self._get_number("Enter first number: ")
            val2 = self._get_number("Enter second number: ")

            # Logic execution with Exception Handling
            
            try:
                result = processor.execute(val1, val2)
                print(f"\n[Result] {label}: {result}")
            except ZeroDivisionError as e:
                print(f"\nMath Error: {e}")
        else:
            print("Operation not recognized.")