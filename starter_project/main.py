"""
Starter Project — Main Application
====================================
This is your starting point. Build something awesome with Copilot!

Instructions:
  1. Decide what you want to build (see README.md for ideas).
  2. Describe your project in a comment below.
  3. Let Copilot help you build it function by function.
  4. Run often: python starter_project/main.py

Tip: Start with a clear comment describing what you want, then let Copilot
generate the code. For example:

    # Create a class called TodoApp that manages a list of tasks.
    # Each task has a title, description, priority (1-5), and done status.
    # The app should support: add, remove, complete, and list tasks.
"""

from utils import greet, calculate_average


# ---------------------------------------------------------------------------
# YOUR PROJECT STARTS HERE
# ---------------------------------------------------------------------------

class Course:
    """Represents a single course with its grades."""

    def __init__(self, name: str, test_weight: float = 0.3, homework_weight: float = 0.7):
        self.name = name
        self.test_weight = test_weight
        self.homework_weight = homework_weight
        self.tests: list[float] = []
        self.homeworks: list[float] = []

    def add_test(self, score: float):
        """Adds a test score."""
        self.tests.append(score)

    def add_homework(self, score: float):
        """Adds a homework score."""
        self.homeworks.append(score)

    def calculate_final_grade(self) -> float:
        """Calculates the final grade based on weighted averages."""
        test_avg = calculate_average(self.tests)
        homework_avg = calculate_average(self.homeworks)

        # If one category is empty, the other has full weight
        if not self.tests and not self.homeworks:
            return 0.0
        if not self.tests:
            return homework_avg
        if not self.homeworks:
            return test_avg

        return (test_avg * self.test_weight) + (homework_avg * self.homework_weight)


class GradeTracker:
    """Manages a collection of courses."""

    def __init__(self):
        self.courses: dict[str, Course] = {}

    def add_course(self, name: str, test_weight: float = 0.3, homework_weight: float = 0.7):
        """Adds a new course to the tracker."""
        if name in self.courses:
            raise ValueError(f"Course '{name}' already exists.")
        self.courses[name] = Course(name, test_weight, homework_weight)
        print(f"Course '{name}' added.")

    def add_grade(self, course_name: str, assignment_type: str, score: float):
        """Adds a grade to a specific course."""
        if course_name not in self.courses:
            raise ValueError(f"Course '{course_name}' not found.")

        course = self.courses[course_name]
        if assignment_type.lower() == 'test':
            course.add_test(score)
        elif assignment_type.lower() == 'homework':
            course.add_homework(score)
        else:
            raise ValueError("Assignment type must be 'test' or 'homework'.")
        print(f"Added {assignment_type} score {score} to '{course_name}'.")

    def get_course_grade(self, course_name: str) -> float:
        """Gets the calculated final grade for a course."""
        if course_name not in self.courses:
            raise ValueError(f"Course '{course_name}' not found.")
        return self.courses[course_name].calculate_final_grade()

    def list_courses(self):
        """Prints a summary of all courses and their current grades."""
        if not self.courses:
            print("No courses added yet.")
            return
        print("\n--- Grade Summary ---")
        for name, course in self.courses.items():
            grade = course.calculate_final_grade()
            print(f"  - {name}: {grade:.2f}")
        print("---------------------\n")


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------
def main():
    """Demonstrates the Grade Tracker functionality."""
    print(greet("Student"))
    print("Welcome to the Student Grade Tracker!")

    tracker = GradeTracker()

    # Example usage based on the request: 70% homework, 30% tests
    tracker.add_course("Computer Science 101", test_weight=0.3, homework_weight=0.7)
    tracker.add_grade("Computer Science 101", "homework", 95)
    tracker.add_grade("Computer Science 101", "homework", 88)
    tracker.add_grade("Computer Science 101", "test", 75)
    tracker.add_grade("Computer Science 101", "test", 82)

    tracker.list_courses()

    # Show detailed calculation for one course
    course_name = "Computer Science 101"
    final_grade = tracker.get_course_grade(course_name)
    course = tracker.courses[course_name]
    hw_avg = calculate_average(course.homeworks)
    test_avg = calculate_average(course.tests)

    print(f"Detailed calculation for {course_name}:")
    print(f"  Homework average ({course.homework_weight*100}%): {hw_avg:.2f}")
    print(f"  Test average ({course.test_weight*100}%): {test_avg:.2f}")
    print(f"  Final Grade = ({hw_avg:.2f} * {course.homework_weight}) + ({test_avg:.2f} * {course.test_weight}) = {final_grade:.2f}")


if __name__ == "__main__":
    main()
