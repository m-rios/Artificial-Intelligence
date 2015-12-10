from collections import namedtuple

Course = namedtuple('Course', 'name, program, nStudents, type')
Room = namedtuple('Room',"name, nSeats, projector, computer, equipment, level")


def courseArray():
    return [
        Course('A', 'Data', 9, 'Lecture'),
        Course('B', 'Sociology', 9, 'Seminar'),
        Course('C', 'Psychology', 65, 'Lecture'),
        Course('D', 'Data', 20, 'Labs'),
        Course('E', 'Mathematics', 25, 'Lecture'),
        Course('F', 'Criminology', 20, 'Seminar'),
        Course('G', 'Machine Engineering', 15, 'Labs'),
        Course('H', 'Machine Engineering', 35, 'Lecture'),
        Course('I', 'Data', 44, 'Lecture'),
        Course('J', 'Machine Engineering', 27, 'Lecture'),
    ]


def roomArray():
    return [
        Room("T002", 20, False, True, False, 0),
        Room("T004", 30, False, True, False, 0),
        Room("T101", 70, True, False, False, 1),
        Room("T103", 20, False, False, False, 1),
        Room("T114B", 10, False, False, True, 1),
        Room("T127", 30, True, False, False, 1),
        Room("T133", 40, True, False, False, 1),
        Room("T203", 10, False, False, False, 2),
        Room("T221", 20, True, False, False, 2),
        Room("T227", 70, True, False, False, 2)
    ]

