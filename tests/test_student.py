from school_schedule.student import Student

def test_student_class_instantiation():
    # Arrange
    name = "Quinn"
    grade = "junior"
    classes = [
                    "Pre-Calc", 
                    "English III", 
                    "World History", 
                    "Gym", 
                    "Chemistry", 
                    "Music Composition"
                ]
    
    # Act 
    quinn = Student(name, grade, classes)

    # Assert
    assert quinn.name == "Quinn"
    assert quinn.grade == "junior"
    assert quinn.classes == [
                    "Pre-Calc", 
                    "English III", 
                    "World History", 
                    "Gym", 
                    "Chemistry", 
                    "Music Composition"
                ]
    assert quinn.get_num_classes() == 6
    assert quinn.summary() == (f"{name} is a {grade} "
            f"enrolled in {quinn.get_num_classes()} classes: "
            f"{quinn.display_classes()}")
    
def test_student_object_add_classes():
    # Arrange
    name = "Quinn"
    grade = "junior"
    classes = ["Calculus"]

    # Act 
    quinn = Student(name, grade, classes)
    quinn.add_class("History")

    # Assert
    assert quinn.classes == ["Calculus", "History"]
    assert quinn.get_num_classes() == 2
    assert quinn.summary() == (f"{name} is a {grade} "
            f"enrolled in 2 classes: "
            f"{quinn.display_classes()}")

    
def test_student_object_no_classes():
    # Arrange
    name = "Quinn"
    grade = "junior"
    classes = []

    # Act 
    quinn = Student(name, grade, classes)

    # Assert 
    assert quinn.get_num_classes() == 0
    assert quinn.summary() == (f"{quinn.name} is a {quinn.grade} "
            f"enrolled in {quinn.get_num_classes()} classes: "
            f"{quinn.display_classes()}")