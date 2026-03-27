"""
Starter Project — Utility Functions
=====================================
Put shared helper functions here. This keeps main.py clean.

Instructions:
  1. As you build your project, move reusable logic here.
  2. Import functions in main.py: from utils import my_function
"""


def greet(name: str) -> str:
    """Return a greeting message."""
    return f"Welcome to SolHacks 2026, {name}! 🚀"


def calculate_average(grades: list[float]) -> float:
    """Calculates the average of a list of numbers."""
    if not grades:
        return 0.0
    return sum(grades) / len(grades)
