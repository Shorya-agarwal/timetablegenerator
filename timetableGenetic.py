from dataclasses import dataclass
from random import randrange, random
from prettytable import PrettyTable

POPULATION_SIZE = 9
NUMB_OF_ELITE_SCHEDULES = 2
TOURNAMENT_SELECTION_SIZE = 5
MUTATION_RATE = 0.1

@dataclass(frozen=True)
class GeneticAlgorithm:
    def evolve(self, population): return self._mutate_population(self._crossover_population(population))

    def _crossover_population(self, pop):
        crossover_pop = Population(0)
        for i in range(NUMB_OF_ELITE_SCHEDULES):
            crossover_pop.get_schedules().append(pop.get_schedules()[i])
        i = NUMB_OF_ELITE_SCHEDULES
        while i < POPULATION_SIZE:
            schedule1 = self._select_tournament_population(pop).get_schedules()[0]
            schedule2 = self._select_tournament_population(pop).get_schedules()[1]
            crossover_pop.get_schedules().append(self._crossover_schedule(schedule1, schedule2))
            i += 1
        return crossover_pop

    def _mutate_population(self, population):
        for i in range(NUMB_OF_ELITE_SCHEDULES, POPULATION_SIZE):
            self._mutate_schedule(population.get_schedules()[i])
        return population

    def _crossover_schedule(self, schedule1, schedule2):
        crossoverSchedule = Schedule().initialize()
        for i in range(len(crossoverSchedule.get_classes())):
            if random() > 0.5: crossoverSchedule.get_classes()[i] = schedule1.get_classes()[i]
            else: crossoverSchedule.get_classes()[i] = schedule2.get_classes()[i]
        return crossoverSchedule

    def _mutate_schedule(self, mutateSchedule):
        schedule = Schedule().initialize()
        for i in range(len(mutateSchedule.get_classes())):
            if MUTATION_RATE > random(): mutateSchedule.get_classes()[i] = schedule.get_classes()[i]
        return mutateSchedule

    def _select_tournament_population(self, pop):
        tournament_pop = Population(0)
        i = 0
        while i < TOURNAMENT_SELECTION_SIZE:
            tournament_pop.get_schedules().append(pop.get_schedules()[randrange(0, POPULATION_SIZE)])
            i += 1
        tournament_pop.get_schedules().sort(key=lambda x: x.get_fitness(), reverse=True)
        return tournament_pop


@dataclass
class Course:
    _number: str
    _name: str
    _instructors: list
    _maxNumbOfStudents: int

    def get_number(self): return self._number
    def get_name(self): return self._name
    def get_instructors(self): return self._instructors
    def get_maxNumbOfStudents(self): return self._maxNumbOfStudents
    def __str__(self): return self._name

@dataclass
class Instructor:
    _id: int
    _name: str

    def get_id(self): return self._id
    def get_name(self): return self._name
    def __str__(self): return self._name

@dataclass
class Room:
    _number: int
    _seatingCapacity: int

    def get_number(self): return self._number
    def get_seatingCapacity(self): return self._seatingCapacity

@dataclass
class MeetingTime:
    _id: int
    _time: str

    def get_id(self): return self._id
    def get_time(self): return self._time

@dataclass
class Department:
    _name: str
    _courses: list

    def get_name(self): return self._name
    def get_courses(self): return self._courses

@dataclass
class Class:
    _id: str
    _dept: str
    _course: str
    _instructor: int = None
    _meetingTime: str = None
    _room: int = None

    def get_id(self): return self._id
    def get_dept(self): return self._dept
    def get_course(self): return self._course
    def get_instructor(self): return self._instructor
    def get_meetingTime(self): return self._meetingTime
    def get_room(self): return self._room

    def set_instructor(self, instructor): self._instructor = instructor
    def set_meetingTime(self, meetingTime): self._meetingTime = meetingTime
    def set_room(self, room): self._room = room
    def __str__(self):
        return str(self._dept.get_name()) + ',' + str(self._course.get_number()) + ',' + str(self._room.get_number()) + ',' + str(self._instructor.get_id()) + ',' + str(self._meetingTime.get_id())

class Data:
    ROOMS = [['R1', 130],
            ['R2', 130],
            ['R3', 120],
            ['R4', 120],
            ['R5', 100]]

    # MEETING_TIMES = [['Monday1', '09:00 - 10:00'],
    #                  ['Monday2', '10:00 - 11:00'],
    #                  ['Monday3', '11:00 - 12:00'],
    #                  ['Monday4', '01:30 - 02:30'],
    #                  ['Monday5', '02:30 - 03:30'],
    #                  ['Monday6', '03:30 - 04:30'],

    #                  ['Tuesday1', '09:00 - 10:00'],
    #                  ['Tuesday2', '10:00 - 11:00'],
    #                  ['Tuesday3', '11:00 - 12:00'],
    #                  ['Tuesday4', '01:30 - 02:30'],
    #                  ['Tuesday5', '02:30 - 03:30'],
    #                  ['Tuesday6', '03:30 - 04:30'],

    #                  ['Wednesday1', '09:00 - 10:00'],
    #                  ['Wednesday2', '10:00 - 11:00'],
    #                  ['Wednesday3', '11:00 - 12:00'],
    #                  ['Wednesday4', '01:30 - 02:30'],
    #                  ['Wednesday5', '02:30 - 03:30'],
    #                  ['Wednesday6', '03:30 - 04:30'],

    #                  ['Thursday1', '09:00 - 10:00'],
    #                  ['Thursday2', '10:00 - 11:00'],
    #                  ['Thursday3', '11:00 - 12:00'],
    #                  ['Thursday4', '01:30 - 02:30'],
    #                  ['Thursday5', '02:30 - 03:30'],
    #                  ['Thursday6', '03:30 - 04:30'],

    #                  ['Friday1', '09:00 - 10:00'],
    #                  ['Friday2', '10:00 - 11:00'],
    #                  ['Friday3', '11:00 - 12:00'],
    #                  ['Friday4', '01:30 - 02:30'],
    #                  ['Friday5', '02:30 - 03:30'],
    #                  ['Friday6', '03:30 - 04:30']]

    MEETING_TIMES = [['MT1', '09:30 - 10:30'],
                    ['MT2', '10:30 - 11:30'],
                    ['MT3', '11:30 - 12:30'],
                    ['MT4', '1:30 - 2:30'],
                    ['MT5', '2:30 - 3:30'],
                     ['MT6', '3:30 - 4:30']]

    INSTRUCTORS = [['I1', 'Instructor 1'],
                ['I2', 'Instructor 2'],
                ['I3', 'Instructor 3'],
                ['I4', 'Instructor 4'],
                ['I5', 'Instructor 5'],
                ['I6', 'Instructor 6'],
                ['I7', 'Instructor 7'],
                ['I8', 'Instructor 8'],
                ['I9', 'Instructor 9']]

    def __init__(self):
        self._rooms = [Room(self.ROOMS[i][0], self.ROOMS[i][1]) for i in range(len(self.ROOMS))]
        self._meetingTimes = [MeetingTime(self.MEETING_TIMES[i][0], self.MEETING_TIMES[i][1]) for i in range(len(self.MEETING_TIMES))]
        self._instructors = [Instructor(self.INSTRUCTORS[i][0], self.INSTRUCTORS[i][1]) for i in range(len(self.INSTRUCTORS))]

        course1 = Course('C1', 'Course 1', [self._instructors[8], self._instructors[1]], 25)
        course2 = Course('C2', 'Course 2', [self._instructors[0], self._instructors[1], self._instructors[2]], 80)
        course3 = Course('C3', 'Course 3', [self._instructors[8], self._instructors[1]], 50)
        course4 = Course('C4', 'Course 4', [self._instructors[2], self._instructors[3]], 90)
        course5 = Course('C5', 'Course 5', [self._instructors[5]], 45)
        course6 = Course('C6', 'Course 6', [self._instructors[6], self._instructors[7]], 80)
        course7 = Course('C7', 'Course 7', [self._instructors[7], self._instructors[8]], 60)

        self._courses = [course1, course2, course3, course4, course5, course6, course7]

        dept1 = Department('B.TECH', [course1, course3])
        dept2 = Department('BCA', [course2, course4, course5])
        dept3 = Department('Bio.Eng', [course6, course7])
        self._depts = [dept1, dept2, dept3]

        self._numberOfClasses = 0
        for i in range(len(self._depts)):
            self._numberOfClasses += len(self._depts[i].get_courses())

    def get_rooms(self): return self._rooms
    def get_instructors(self): return self._instructors
    def get_courses(self): return self._courses
    def get_depts(self): return self._depts
    def get_meetingTimes(self): return self._meetingTimes
    def get_numberOfClasses(self): return self._numberOfClasses

@dataclass
class Schedule:
    def __init__(self):
        self._data = data
        self._classes = []
        self._numbOfConflicts = 0
        self._fitness = -1
        self._classNumb = 0
        self._isFitnessChanged = True

    def get_classes(self):
        self._isFitnessChanged = True
        return self._classes

    def get_numbOfConflicts(self): return self._numbOfConflicts
    def calculate_fitness(self):
        self._numbOfConflicts = 0
        classes = self.get_classes()
        for i in range(0,len(classes)):
            if classes[i].get_room().get_seatingCapacity() < classes[i].get_course().get_maxNumbOfStudents():
                self._numbOfConflicts += 1
            for j in range(len(classes)):
                if j >= i:
                    if (classes[i].get_meetingTime() == classes[j].get_meetingTime()) and (classes[i].get_id() != classes[j].get_id()):
                        if classes[i].get_room() == classes[j].get_room(): self._numbOfConflicts += 1
                        if classes[i].get_instructor() == classes[j].get_instructor(): self._numbOfConflicts += 1
        # print(1 / (1.0 * self._numbOfConflicts + 1))
        # return 1
        return 1 / (1.0 * self._numbOfConflicts + 1) or 1
    def get_fitness(self):
        if self._isFitnessChanged == True:
            self._fitness = self.calculate_fitness()
            self._isFitnessChanged = False
        return self._fitness

    def initialize(self):
        depts = self._data.get_depts()
        for i in range(len(depts)):
            courses = depts[i].get_courses()
            for j in range(len(courses)):
                newClass = Class(self._classNumb, depts[i], courses[j])
                self._classNumb += 1
                newClass.set_meetingTime(data.get_meetingTimes()[randrange(0, len(data.get_meetingTimes()))])
                newClass.set_room(data.get_rooms()[randrange(0, len(data.get_rooms()))])
                newClass.set_instructor(courses[j].get_instructors()[randrange(0, len(courses[j].get_instructors()))])
                self._classes.append(newClass)
        return self

    

    def __str__(self):
        returnValue = ""
        for i in range(len(self._classes)-1):
            returnValue += str(self._classes[i]) + ', '
        returnValue += str(self._classes[len(self._classes)-1])
        return returnValue

class Population:
    def __init__(self, size):
        self._size: size
        self._data = data
        self._schedules = [Schedule().initialize() for _ in range(size)]

    def get_schedules(self): return self._schedules

@dataclass(frozen=True)
class DisplayMgr:
    def print_available_data(self):
        print("> All available data")
        self.print_dept()
        self.print_course()
        self.print_room()
        self.print_instructor()
        self.print_meeting_times()

    def print_dept(self):
        depts = data.get_depts()
        availableDeptsTable = PrettyTable(['dept', 'courses'])
        for i in range(len(depts)):
            courses = depts.__getitem__(i).get_courses()
            tempStr = '['
            for j in range(len(courses)-1):
                tempStr += courses[j].__str__() + ', '
            tempStr += courses[len(courses) - 1].__str__() + ']'
            availableDeptsTable.add_row([depts.__getitem__(i).get_name(), tempStr])
        print(availableDeptsTable)

    def print_course(self):
        availableCoursesTable = PrettyTable(['id', 'course #', 'max # of students', 'instructors'])
        courses = data.get_courses()
        for i in range(len(courses)):
            instructors = courses[i].get_instructors()
            tempStr = ''
            for j in range(len(instructors)-1):
                tempStr += instructors[j].__str__() + ', '
            tempStr += instructors[len(instructors) - 1].__str__()
            availableCoursesTable.add_row([courses[i].get_number(), courses[i].get_name(), str(courses[i].get_maxNumbOfStudents()), tempStr])
        print(availableCoursesTable)

    def print_instructor(self):
        availableInstructorsTable = PrettyTable(['id', 'instructor'])
        instructors = data.get_instructors()
        for i in range(len(instructors)):
            availableInstructorsTable.add_row([instructors[i].get_id(), instructors[i].get_name()])
        print(availableInstructorsTable)

    def print_room(self):
        availableRoomsTable = PrettyTable(['room #', 'max seating capacity'])
        rooms = data.get_rooms()
        for i in range(len(rooms)):
            availableRoomsTable.add_row([str(rooms[i].get_number()), str(rooms[i].get_seatingCapacity())])
        print(availableRoomsTable)

    def print_meeting_times(self):
        availableMeetingTimeTable = PrettyTable(['id', 'Meeting time'])
        meetingTimes = data.get_meetingTimes()
        for i in range(len(meetingTimes)):
            availableMeetingTimeTable.add_row([meetingTimes[i].get_id(), meetingTimes[i].get_time()])
        print(availableMeetingTimeTable)

    def print_generation(self, population):
        generationTable = PrettyTable(['schedule #', 'fitness', '# of conflicts', 'classes [dept, class, room, instructor, meeting-time]'])
        schedules = population.get_schedules()
        for i in range(len(schedules)):
            generationTable.add_row([str(i), round(schedules[i].get_fitness(), 3), f'{schedules[i].get_numbOfConflicts()}',
                                     f"{schedules[i].get_classes()[0]},{schedules[i].get_classes()[1]},{schedules[i].get_classes()[2]},{schedules[i].get_classes()[3]}"])
        print(generationTable)

    def  print_schedule_as_table(self, schedule):
        classes = schedule.get_classes()
        table = PrettyTable(['Class #', 'Dept', 'Course (number, max # of students]', 'Room (capacity)', 'Instructor (Id)', 'Meeting Time'])
        for i in range(len(classes)):
            table.add_row([str(i), classes[i].get_dept().get_name(),
                           f"{classes[i].get_course().get_name()} ({classes[i].get_course().get_number()}, {str(classes[i].get_course().get_maxNumbOfStudents())})",
                           f"{classes[i].get_room().get_number()} ({str(classes[i].get_room().get_seatingCapacity())})",
                           f"{classes[i].get_instructor().get_id()} ({str(classes[i].get_instructor())})",
                           f"{classes[i].get_meetingTime().get_time()} ({str(classes[i].get_meetingTime().get_id())})"])
        print(table)

data = Data()
displayMgr = DisplayMgr()
displayMgr.print_available_data()
generationNumber = 0
print(f"\n> Generation #{generationNumber}")
population = Population(POPULATION_SIZE)
population.get_schedules().sort(key=lambda x: x.get_fitness(), reverse=True)
displayMgr.print_generation(population)
count = 0
for k in range(POPULATION_SIZE):
    if population.get_schedules()[k].get_fitness() == 1:
        displayMgr.print_schedule_as_table(population.get_schedules()[k])

geneticAlgorithm = GeneticAlgorithm()

while population.get_schedules()[0].get_fitness() != 1 or count <=7:
    generationNumber += 1
    print(f"\n> Generation # {generationNumber}")
    population = geneticAlgorithm.evolve(population)
    population.get_schedules().sort(key=lambda x: x.get_fitness(), reverse=True)
    displayMgr.print_generation(population)
    # displayMgr.print_schedule_as_table(population.get_schedules()[0])
    for k in range(POPULATION_SIZE):
        if population.get_schedules()[k].get_fitness() == 1:
            displayMgr.print_schedule_as_table(population.get_schedules()[k])
        count = count + 1
print('\n\n')