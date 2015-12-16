from collections import namedtuple
from data import *
import math
import random
# Room = namedtuple('Room',"name, nSeats, projector, computer, equipment, level")
# Course = namedtuple('Course', 'name, program, nStudents, type')
# Assignments: ['Room':'Course']
from collections import namedtuple
import random

Room = namedtuple("Room", "name, nSeats, projector, computer, equipment, level")
Course = namedtuple("Course", "name, program, nStudents, type")


def check_room_size(course, room):
    return course.nStudents <= room.nSeats


def check_projector(course, room):
    if course.type == "Lecture" or course.type == "Seminar":
        return room.projector
    return True


def check_computers(course, room):
    if course.program == "Data" and course.type == "Lab":
        return room.computer
    return True


def check_equipment(course, room):
    if course.program == "Machine Engineering" and course.type == "Labs":
        return room.equipment
    return True


def check_level(assignment, course, room):
    for key in assignment:
        if assignment[
            key].program == course.program and not key.level == room.level:
            return False
    return True


def allocate(courses, rooms):
    return recursive_backtracking({}, courses, rooms)


def recursive_backtracking(assignments, courses, rooms):
    if len(assignments) == len(rooms):
        return assignments
    room = select_unassigned_variable(rooms, assignments)
    for course in courses:
        if check_room_size(course, room) and course not in assignments.values():
            assignments[room] = course
            result = recursive_backtracking(assignments, courses, rooms)
            if result:
                return result
            del assignments[room]
    return None


def select_unassigned_variable(rooms, assignments):
    for room in rooms:
        if room not in assignments:
            return room


def print_assignments(result):
    for key in result:
        print("Name: ", key.name, " Seats: ", key.nSeats, " Students: ",
              result[key].nStudents, " Course: ", result[key].name,
              " Program: ", result[key].program, " Type: ", result[key].type,
              " Equipment: ", key.equipment)


def check_constraints(assignments):
    violated_constraints = 0
    for key in assignments:
        if not check_room_size(assignments[key], key):
            # This is the most important constraint.
            # The rooms should always be big enough.
            violated_constraints += 1 * 100
        if not check_projector(assignments[key], key):
            violated_constraints += 1
        if not check_computers(assignments[key], key):
            violated_constraints += 1
        if not check_equipment(assignments[key], key):
            violated_constraints += 1
        if not check_level(assignments, assignments[key], key):
            violated_constraints += 1
    return violated_constraints


def three_swap(assignements, key_1, key_2, key_3):
    new_assignements = dict(assignements)
    new_assignements[key_1] = assignements[key_2]
    new_assignements[key_2] = assignements[key_3]
    new_assignements[key_3] = assignements[key_1]
    return new_assignements


def two_swap(assignements, key_1, key_2):
    new_assignements = dict(assignements)
    new_assignements[key_1] = assignements[key_2]
    new_assignements[key_2] = assignements[key_1]
    return new_assignements


def swap(assignments):
    # new_assignements = dict(assignments)
    key_1 = random.choice(list(assignments.keys()))
    key_2 = key_1
    while key_1 == key_2:
        key_2 = random.choice(list(assignments.keys()))
    # 1 chance out of 100 of doing 3-swap
    swap_number = random.randrange(1, 3)
    if swap_number == 2:
        key_3 = key_1
        while key_3 == key_1 or key_3 == key_2:
            key_3 = random.choice(list(assignments.keys()))
        return three_swap(assignments, key_1, key_2, key_3)
    else:
        return two_swap(assignments, key_1, key_2)


def generate_schedule():
    schedule = [1000]
    alpha = 0.9
    for i in range(1, 1000):
        schedule.append(schedule[i - 1] * alpha)
        # schedule.append((schedule[i-1]-1))
    schedule.append(0)
    return schedule


def simulated_annealing(assignements):
    schedule = generate_schedule()
    while True:
        t = schedule.pop(0)
        if t == 0:
            return assignements
        next = swap(assignements)
        next_fitness = check_constraints(next)
        if next_fitness == 0:
            return next
        old_fitness = check_constraints(assignements)
        increment = old_fitness - next_fitness
        if increment > 0:
            assignements = next
        else:
            probability = int(math.e ** (increment / t) * 100)
            rand = random.randrange(1, 100)
            if rand <= probability:
                assignements = next


if __name__ == '__main__':
    rooms = roomArray()
    courses = courseArray()

    sol = allocate(courses, rooms)
    print "backtraking:"
    print_assignments(sol)
    print check_constraints(sol)

    final_sol = simulated_annealing(sol)
    print "simulated annealing:"
    print_assignments(final_sol)
    print check_constraints(final_sol)
