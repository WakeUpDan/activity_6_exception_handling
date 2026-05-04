# The "Engine" Layer (Inheritance)

class MathOperation:
    """Base class for all math logic."""
    def execute(self, a: float, b: float) -> float:
        raise NotImplementedError("Each operation must define its own execute method.")