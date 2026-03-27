"""
Starter Project — Tests
========================
Write tests for your project here. Copilot is great at generating tests!

Instructions:
  1. Import your functions/classes from main.py or utils.py.
  2. Write a comment describing the test, then let Copilot complete it.
  3. Run: pytest starter_project/test_main.py -v

Tip: Ask Copilot Chat: "Generate tests for the functions in starter_project/main.py"
"""

import pytest
from starter_project.main import Course, GradeTracker
from starter_project.utils import calculate_average


# ---------------------------------------------------------------------------
# Tests for utility functions
# ---------------------------------------------------------------------------

def test_calculate_average():
    """Test the calculate_average function."""
    assert calculate_average([80, 90, 100]) == 90
    assert calculate_average([]) == 0.0
    assert calculate_average([50]) == 50


# ---------------------------------------------------------------------------
# Tests for Course class
# ---------------------------------------------------------------------------

@pytest.fixture
def sample_course():
    """Returns a sample Course instance with 30/70 weighting."""
    return Course("Test Course", test_weight=0.3, homework_weight=0.7)


def test_course_creation(sample_course):
    """Test that a course is initialized correctly."""
    assert sample_course.name == "Test Course"
    assert sample_course.tests == []
    assert sample_course.homeworks == []
    assert sample_course.test_weight == 0.3
    assert sample_course.homework_weight == 0.7


def test_add_grades(sample_course):
    """Test adding grades to a course."""
    sample_course.add_test(80)
    sample_course.add_homework(100)
    assert sample_course.tests == [80]
    assert sample_course.homeworks == [100]


def test_calculate_final_grade(sample_course):
    """Test the final grade calculation with both tests and homework."""
    sample_course.add_test(80)
    sample_course.add_test(90)  # avg = 85
    sample_course.add_homework(100)
    sample_course.add_homework(90)  # avg = 95
    # Expected: (85 * 0.3) + (95 * 0.7) = 25.5 + 66.5 = 92.0
    assert sample_course.calculate_final_grade() == pytest.approx(92.0)


def test_calculate_grade_with_only_tests(sample_course):
    """Test final grade calculation with only test scores."""
    sample_course.add_test(80)
    sample_course.add_test(90)  # avg = 85
    assert sample_course.calculate_final_grade() == pytest.approx(85.0)


def test_calculate_grade_with_only_homework(sample_course):
    """Test final grade calculation with only homework scores."""
    sample_course.add_homework(100)
    sample_course.add_homework(90)  # avg = 95
    assert sample_course.calculate_final_grade() == pytest.approx(95.0)


def test_calculate_grade_no_grades(sample_course):
    """Test final grade calculation with no grades added."""
    assert sample_course.calculate_final_grade() == 0.0


# ---------------------------------------------------------------------------
# Tests for GradeTracker class
# ---------------------------------------------------------------------------

@pytest.fixture
def tracker():
    """Returns a GradeTracker instance for testing."""
    return GradeTracker()


def test_gradetracker_add_course(tracker):
    """Test adding a new course to the tracker."""
    tracker.add_course("Math 101")
    assert "Math 101" in tracker.courses
    assert isinstance(tracker.courses["Math 101"], Course)


def test_gradetracker_add_duplicate_course_raises_error(tracker):
    """Test that adding a duplicate course raises a ValueError."""
    tracker.add_course("Math 101")
    with pytest.raises(ValueError, match="Course 'Math 101' already exists."):
        tracker.add_course("Math 101")


def test_gradetracker_add_grade(tracker):
    """Test adding a grade to a course in the tracker."""
    tracker.add_course("Science 101")
    tracker.add_grade("Science 101", "test", 90)
    tracker.add_grade("Science 101", "homework", 95)
    course = tracker.courses["Science 101"]
    assert course.tests == [90]
    assert course.homeworks == [95]


def test_gradetracker_add_grade_to_nonexistent_course(tracker):
    """Test that adding a grade to a non-existent course raises an error."""
    with pytest.raises(ValueError, match="Course 'Ghost Course' not found."):
        tracker.add_grade("Ghost Course", "test", 100)


def test_gradetracker_get_course_grade(tracker):
    """Test getting a calculated course grade from the tracker."""
    tracker.add_course("History 101", test_weight=0.3, homework_weight=0.7)
    tracker.add_grade("History 101", "test", 85)
    tracker.add_grade("History 101", "homework", 95)
    # (85 * 0.3) + (95 * 0.7) = 25.5 + 66.5 = 92.0
    assert tracker.get_course_grade("History 101") == pytest.approx(92.0)
