from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *
from data.department import DepartmentService
from data.discipline import DisciplineService
from data.student import StudentService
from data.teacher import TeacherService
from pages.exceptions.error_dialog import ErrorException


class AdminWindow(QMainWindow):
    def __init__(self):
        self.window = []
        QMainWindow.__init__(self)

        self.depart_service = DepartmentService()
        self.disp_service = DisciplineService()
        self.student_service = StudentService()
        self.teacher_service = TeacherService()

        data_rows = []
        departs = self.depart_service.get()
        for depart in departs:
            data_rows.append(
                [depart['id'], depart['name'], depart['phone']])

        self.size = QSize(940, 800)
        self.setFixedSize(self.size)
        self.setWindowTitle('Админская панель')

        menuBar = QMenuBar(self)
        self.setMenuBar(menuBar)

        toolbar = QToolBar('My main toolbar')
        toolbar.setIconSize(QSize(16, 16))
        self.addToolBar(toolbar)

        toolbar_button_create = QAction(QIcon('img/ui/plus.png'), 'Добавить', self)
        toolbar_button_create.setStatusTip('добавить')
        toolbar_button_create.setCheckable(True)
        toolbar_button_create.triggered.connect(self.call_create_depart)
        toolbar.addAction(toolbar_button_create)
        self.setStatusBar(QStatusBar(self))

        toolbar.addSeparator()

        toolbar_button_delete = QAction(QIcon('img/ui/minus.png'), 'Удалить', self)
        toolbar_button_delete.setStatusTip('Удалить')
        toolbar_button_delete.setCheckable(True)
        toolbar_button_delete.triggered.connect(self.call_form_delete)
        toolbar.addAction(toolbar_button_delete)
        self.setStatusBar(QStatusBar(self))

        toolbar.addSeparator()

        toolbar_button_discipline = QAction(QIcon('img/ui/books.png'), 'Дисциплины', self)
        toolbar_button_discipline.setStatusTip('Дисциплины')
        toolbar_button_discipline.setCheckable(True)
        toolbar_button_discipline.triggered.connect(self.call_discipline)
        toolbar.addAction(toolbar_button_discipline)
        self.setStatusBar(QStatusBar(self))

        toolbar.addSeparator()

        toolbar_button_students = QAction(QIcon('img/ui/user.png'), 'Студенты', self)
        toolbar_button_students.setStatusTip('Студенты')
        toolbar_button_students.setCheckable(True)
        toolbar_button_students.triggered.connect(self.call_students)
        toolbar.addAction(toolbar_button_students)
        self.setStatusBar(QStatusBar(self))

        toolbar.addSeparator()

        toolbar_button_teachers = QAction(QIcon('img/ui/book-alt.png'), 'Преподаватели', self)
        toolbar_button_teachers.setStatusTip('Преподаватели')
        toolbar_button_teachers.setCheckable(True)
        toolbar_button_teachers.triggered.connect(self.call_teachers)
        toolbar.addAction(toolbar_button_teachers)
        self.setStatusBar(QStatusBar(self))

        toolbar.addSeparator()

        toolbar_button_update_table = QAction(QIcon('img/ui/refresh.png'), 'Обновить таблицу', self)
        toolbar_button_update_table.setStatusTip('Обновить таблицу')
        toolbar_button_update_table.setCheckable(True)
        toolbar_button_update_table.triggered.connect(self.callUpdateTable)
        toolbar.addAction(toolbar_button_update_table)
        self.setStatusBar(QStatusBar(self))

        toolbar.addSeparator()

        central = QWidget(self)
        self.setCentralWidget(central)
        self.grid = QGridLayout(self)
        central.setLayout(self.grid)

        self.table = QTableWidget(self)
        self.table.setColumnCount(3)
        self.table.setRowCount(15)
        self.table.setHorizontalHeaderLabels(['ID', 'Имя', 'Телефон'])
        departs = self.depart_service.get()
        self.table.setRowCount(50)
        for i, v in enumerate(departs):
            self.table.setItem(i, 0, QTableWidgetItem(str(v['id'])))
            self.table.setItem(i, 1, QTableWidgetItem(str(v['name'])))
            self.table.setItem(i, 2, QTableWidgetItem(str(v['phone'])))

        self.grid.addWidget(self.table, 0, 0)

        self.show()

    def callUpdateTable(self, state):
        if state:
            self.close()
            a = AdminWindow()
            self.window.append(a)
            a.show()

    def call_discipline(self, state):
        if state:
            a = Discipline()
            self.window.append(a)
            a.show()

    def call_students(self, state):
        if state:
            a = StudentsWindow()
            self.window.append(a)
            a.show()

    def call_create_depart(self, state):
        if state:
            a = FormCreateDepart()
            self.window.append(a)
            a.show()

    def call_form_delete(self, state):
        if state:
            a = FormDelete()
            self.window.append(a)
            a.show()

    def call_teachers(self, state):
        if state:
            a = Teachers()
            self.window.append(a)
            a.show()


class FormCreateDepart(QMainWindow):
    def __init__(self):
        self.window = []
        QMainWindow.__init__(self)

        self.depart_service = DepartmentService()

        self.setMinimumSize(QSize(320, 270))
        self.setWindowTitle('Создание кафедры')

        self.name_label = QLabel(self)
        self.name_label.setText("Имя")
        self.name_label.move(20, 20)

        self.name = QLineEdit(self)
        self.name.move(110, 20)
        self.name.resize(200, 32)

        self.phone_label = QLabel(self)
        self.phone_label.setText("Телефон")
        self.phone_label.move(20, 60)

        self.phone = QLineEdit(self)
        self.phone.move(110, 60)
        self.phone.resize(200, 32)

        button = QPushButton('Создать', self)
        button.clicked.connect(self.clickMetod)
        button.resize(200, 32)
        button.move(80, 225)

    def clickMetod(self):
        id = self.depart_service.count() + 1
        print(id)
        name = self.name.text()
        phone = self.phone.text()
        self.depart_service.create(id, name, phone)
        self.close()

        a = ErrorException(title='Успех', text='Студент создан')
        self.window.append(a)
        a.show()


class FormDelete(QMainWindow):
    def __init__(self):
        self.window = []
        QMainWindow.__init__(self)

        self.depart_service = DepartmentService()

        self.setMinimumSize(QSize(320, 180))
        self.setWindowTitle('Удалить кафедру')

        self.idLabel = QLabel(self)
        self.idLabel.setText('ID:')
        self.idLabel.move(20, 20)

        self.idLine = QComboBox(self)
        for item in self.depart_service.get():
            self.idLine.addItem(str(item['id']))

        self.idLine.move(80, 20)
        self.idLine.resize(200, 32)

        button = QPushButton('Удалить', self)
        button.clicked.connect(self.clickMetod)
        button.resize(200, 32)
        button.move(80, 120)

    def clickMetod(self):
        self.depart_service.delete(int(self.idLine.currentText()))
        self.idLine.clear()
        self.close()

        a = ErrorException(title='Успех', text='Удалено')
        self.window.append(a)
        a.show()


class StudentsWindow(QMainWindow):
    def __init__(self):
        self.window = []
        QMainWindow.__init__(self)

        self.students_service = StudentService()

        data_rows = []
        students = self.students_service.get()
        for student in students:
            data_rows.append(
                [student['id'], student['number_book'], student['full_name'], student['group_name'], student['city']])

        self.size = QSize(600, 750)
        self.setFixedSize(self.size)
        self.setWindowTitle('AdminWindow')

        menuBar = QMenuBar(self)
        self.setMenuBar(menuBar)

        toolbar = QToolBar('My main toolbar')
        toolbar.setIconSize(QSize(16, 16))
        self.addToolBar(toolbar)

        toolbar_button_create = QAction(QIcon('img/ui/plus.png'), 'Добавить студента', self)
        toolbar_button_create.setStatusTip('Добавить студента')
        toolbar_button_create.setCheckable(True)
        toolbar_button_create.triggered.connect(self.create_student)
        toolbar.addAction(toolbar_button_create)
        self.setStatusBar(QStatusBar(self))

        toolbar.addSeparator()

        toolbar_button_create = QAction(QIcon('img/ui/minus.png'), 'Удалить студента', self)
        toolbar_button_create.setStatusTip('Удалить студента')
        toolbar_button_create.setCheckable(True)
        toolbar_button_create.triggered.connect(self.delete_student)
        toolbar.addAction(toolbar_button_create)
        self.setStatusBar(QStatusBar(self))

        toolbar.addSeparator()

        toolbar_button_update_table = QAction(QIcon('img/ui/refresh.png'), 'Обновить таблицу', self)
        toolbar_button_update_table.setStatusTip('Обновить таблицу')
        toolbar_button_update_table.setCheckable(True)
        toolbar_button_update_table.triggered.connect(self.callUpdateTable)
        toolbar.addAction(toolbar_button_update_table)
        self.setStatusBar(QStatusBar(self))

        toolbar.addSeparator()

        central = QWidget(self)
        self.setCentralWidget(central)
        self.grid = QGridLayout(self)
        central.setLayout(self.grid)

        self.table = QTableWidget(self)
        self.table.setColumnCount(5)
        self.table.setRowCount(50)
        self.table.setHorizontalHeaderLabels(['ID', 'Номер', 'ФИО', 'Группа', 'Город'])
        for i, v in enumerate(self.students_service.get()):
            self.table.setItem(i, 0, QTableWidgetItem(str(v['id'])))
            self.table.setItem(i, 1, QTableWidgetItem(str(v['number_book'])))
            self.table.setItem(i, 2, QTableWidgetItem(str(v['full_name'])))
            self.table.setItem(i, 3, QTableWidgetItem(str(v['group_name'])))
            self.table.setItem(i, 4, QTableWidgetItem(str(v['city'])))

        self.grid.addWidget(self.table, 0, 0)

        self.show()

    def callUpdateTable(self, state):
        if state:
            self.close()
            a = StudentsWindow()
            self.window.append(a)
            a.show()

    def create_student(self, state):
        if state:
            a = FormCreateStudent()
            self.window.append(a)
            a.show()

    def delete_student(self, state):
        if state:
            a = FormDeleteStudent()
            self.window.append(a)
            a.show()


class FormCreateStudent(QMainWindow):
    def __init__(self):
        self.window = []
        QMainWindow.__init__(self)

        self.student_service = StudentService()

        self.setMinimumSize(QSize(320, 270))
        self.setWindowTitle('Создание пользователя')

        self.stud_number_label = QLabel(self)
        self.stud_number_label.setText("Номер студ")
        self.stud_number_label.move(20, 20)

        self.stud_number = QLineEdit(self)
        self.stud_number.move(110, 20)
        self.stud_number.resize(200, 32)

        self.fio_label = QLabel(self)
        self.fio_label.setText("ФИО")
        self.fio_label.move(20, 60)

        self.fio = QLineEdit(self)
        self.fio.move(110, 60)
        self.fio.resize(200, 32)

        self.group = QLineEdit(self)
        self.group.move(110, 125)
        self.group.resize(200, 32)

        self.group_label = QLabel(self)
        self.group_label.setText("Группа")
        self.group_label.move(20, 125)

        self.city = QLineEdit(self)
        self.city.move(110, 160)
        self.city.resize(200, 32)

        self.line_name_label = QLabel(self)
        self.line_name_label.setText("Город")
        self.line_name_label.move(20, 160)

        button = QPushButton('Создать', self)
        button.clicked.connect(self.clickMetod)
        button.resize(200, 32)
        button.move(80, 225)

    def clickMetod(self):
        id = self.student_service.count() + 1
        stud_number = self.stud_number.text()
        fio = self.fio.text()
        group = self.group.text()
        city = self.city.text()
        self.student_service.create(id, stud_number, fio, group, city)
        self.close()

        a = ErrorException(title='Успех', text='Студент создан')
        self.window.append(a)
        a.show()


class FormDeleteTeacher(QMainWindow):
    def __init__(self):
        self.window = []
        QMainWindow.__init__(self)

        self.teacher_service = TeacherService()

        self.setMinimumSize(QSize(320, 180))
        self.setWindowTitle('Удалить преподавателя')

        self.idLabel = QLabel(self)
        self.idLabel.setText('ID:')
        self.idLabel.move(20, 20)

        self.idLine = QComboBox(self)
        for item in self.teacher_service.get():
            self.idLine.addItem(str(item['teacher_number']))

        self.idLine.move(80, 20)
        self.idLine.resize(200, 32)

        button = QPushButton('Удалить', self)
        button.clicked.connect(self.clickMetod)
        button.resize(200, 32)
        button.move(80, 120)

    def clickMetod(self):
        self.teacher_service.delete(int(self.idLine.currentText()))
        self.idLine.clear()
        self.close()

        a = ErrorException(title='Успех', text='Удалено')
        self.window.append(a)
        a.show()


class FormDeleteStudent(QMainWindow):
    def __init__(self):
        self.window = []
        QMainWindow.__init__(self)

        self.student_service = StudentService()

        self.setMinimumSize(QSize(320, 180))
        self.setWindowTitle('Удалить студента')

        self.idLabel = QLabel(self)
        self.idLabel.setText('ID:')
        self.idLabel.move(20, 20)

        self.idLine = QComboBox(self)
        for item in self.student_service.get():
            self.idLine.addItem(str(item['id']))

        self.idLine.move(80, 20)
        self.idLine.resize(200, 32)

        button = QPushButton('Удалить', self)
        button.clicked.connect(self.clickMetod)
        button.resize(200, 32)
        button.move(80, 120)

    def clickMetod(self):
        self.student_service.delete(int(self.idLine.currentText()))
        self.idLine.clear()
        self.close()

        a = ErrorException(title='Успех', text='Удалено')
        self.window.append(a)
        a.show()


class Teachers(QMainWindow):
    def __init__(self):
        self.window = []
        QMainWindow.__init__(self)

        self.teachers_service = TeacherService()

        data_rows = []
        teachers = self.teachers_service.get()
        for teacher in teachers:
            data_rows.append(
                [teacher['teacher_number'], teacher['full_name'], teacher['academic_degree'], teacher['department_id'],
                 teacher['discipline_id']])

        self.size = QSize(600, 750)
        self.setFixedSize(self.size)
        self.setWindowTitle('Преподаватели')

        menuBar = QMenuBar(self)
        self.setMenuBar(menuBar)

        toolbar = QToolBar('My main toolbar')
        toolbar.setIconSize(QSize(16, 16))
        self.addToolBar(toolbar)

        toolbar_button_update_table = QAction(QIcon('img/ui/plus.png'), 'Создать учителя', self)
        toolbar_button_update_table.setStatusTip('Создать учителя')
        toolbar_button_update_table.setCheckable(True)
        toolbar_button_update_table.triggered.connect(self.call_create_teacher)
        toolbar.addAction(toolbar_button_update_table)
        self.setStatusBar(QStatusBar(self))

        toolbar.addSeparator()

        toolbar_button_update_table = QAction(QIcon('img/ui/minus.png'), 'Удалить преподавателя', self)
        toolbar_button_update_table.setStatusTip('Удалить преподавателя')
        toolbar_button_update_table.setCheckable(True)
        toolbar_button_update_table.triggered.connect(self.call_delete_teacher)
        toolbar.addAction(toolbar_button_update_table)
        self.setStatusBar(QStatusBar(self))

        toolbar.addSeparator()

        toolbar_button_update_table = QAction(QIcon('img/ui/refresh.png'), 'Обновить таблицу', self)
        toolbar_button_update_table.setStatusTip('Обновить таблицу')
        toolbar_button_update_table.setCheckable(True)
        toolbar_button_update_table.triggered.connect(self.callUpdateTable)
        toolbar.addAction(toolbar_button_update_table)
        self.setStatusBar(QStatusBar(self))

        toolbar.addSeparator()

        central = QWidget(self)
        self.setCentralWidget(central)
        self.grid = QGridLayout(self)
        central.setLayout(self.grid)

        self.table = QTableWidget(self)
        self.table.setColumnCount(5)
        self.table.setRowCount(50)
        self.table.setHorizontalHeaderLabels(['ID', 'ФИО', 'Степень', 'ID кафедры', 'ID дисциплины'])
        for i, v in enumerate(self.teachers_service.get()):
            print(v)
            self.table.setItem(i, 0, QTableWidgetItem(str(v['teacher_number'])))
            self.table.setItem(i, 1, QTableWidgetItem(str(v['full_name'])))
            self.table.setItem(i, 2, QTableWidgetItem(str(v['academic_degree'])))
            self.table.setItem(i, 3, QTableWidgetItem(str(v['department_id'])))
            self.table.setItem(i, 4, QTableWidgetItem(str(v['discipline_id'])))
        self.grid.addWidget(self.table, 0, 0)

        self.show()

    def callUpdateTable(self, state):
        if state:
            self.close()
            a = Teachers()
            self.window.append(a)
            a.show()

    def call_create_teacher(self, state):
        if state:
            a = FormCreateTeacher()
            self.window.append(a)
            a.show()

    def call_delete_teacher(self, state):
        if state:
            a = FormDeleteTeacher()
            self.window.append(a)
            a.show()


class FormCreateTeacher(QMainWindow):
    def __init__(self):
        self.window = []
        QMainWindow.__init__(self)

        self.teachers_service = TeacherService()
        self.depart_service = DepartmentService()
        self.discipline_service = DisciplineService()

        self.setMinimumSize(QSize(320, 270))
        self.setWindowTitle('Создание преподавателя')

        self.fio_label = QLabel(self)
        self.fio_label.setText("Фио")
        self.fio_label.move(20, 20)

        self.fio = QLineEdit(self)
        self.fio.move(110, 20)
        self.fio.resize(200, 32)

        self.degree_label = QLabel(self)
        self.degree_label.setText("Степень")
        self.degree_label.move(20, 60)

        self.degree = QLineEdit(self)
        self.degree.move(110, 60)
        self.degree.resize(200, 32)

        self.depart = QComboBox(self)
        for teacher in self.depart_service.get():
            self.depart.addItem(str(teacher['id']))
        self.depart.move(110, 125)
        self.depart.resize(200, 32)

        self.combo_box_label_end = QLabel(self)
        self.combo_box_label_end.setText("ID кафедры")
        self.combo_box_label_end.move(20, 125)

        self.combo_box_label_user = QLabel(self)
        self.combo_box_label_user.setText("ID дисциплины")
        self.combo_box_label_user.move(20, 160)

        self.combo_discipline = QComboBox(self)
        for discipline in self.discipline_service.get():
            self.combo_discipline.addItem(str(discipline['subject_code']))
        self.combo_discipline.move(110, 160)
        self.combo_discipline.resize(200, 32)

        button = QPushButton('Создать', self)
        button.clicked.connect(self.clickMetod)
        button.resize(200, 32)
        button.move(80, 225)

    def clickMetod(self):
        fio = self.fio.text()
        degree = self.degree.text()
        depart = self.depart.currentText()
        disc = self.combo_discipline.currentText()
        self.teachers_service.create(fio, degree, depart, disc)
        self.close()

        a = ErrorException(title='Успех', text='Создано')
        self.window.append(a)
        a.show()


class Discipline(QMainWindow):
    def __init__(self):
        self.window = []
        QMainWindow.__init__(self)

        self.discipline_service = DisciplineService()

        data_rows = []
        discipline = self.discipline_service.get()
        for dis in discipline:
            data_rows.append(
                [dis['subject_code'], dis['subject_name'], dis['hours'], dis['student_id']])

        self.size = QSize(600, 750)
        self.setFixedSize(self.size)
        self.setWindowTitle('Дисциплины')

        menuBar = QMenuBar(self)
        self.setMenuBar(menuBar)

        toolbar = QToolBar('My main toolbar')
        toolbar.setIconSize(QSize(16, 16))
        self.addToolBar(toolbar)

        toolbar_button_update_table = QAction(QIcon('img/ui/plus.png'), 'Создать дисциплину', self)
        toolbar_button_update_table.setStatusTip('Создать дисциплину')
        toolbar_button_update_table.setCheckable(True)
        toolbar_button_update_table.triggered.connect(self.call_create_discipline)
        toolbar.addAction(toolbar_button_update_table)
        self.setStatusBar(QStatusBar(self))

        toolbar.addSeparator()

        toolbar_button_update_table = QAction(QIcon('img/ui/minus.png'), 'Удалить дисциплину', self)
        toolbar_button_update_table.setStatusTip('Удалить дисциплину')
        toolbar_button_update_table.setCheckable(True)
        toolbar_button_update_table.triggered.connect(self.call_delete_discipline)
        toolbar.addAction(toolbar_button_update_table)
        self.setStatusBar(QStatusBar(self))

        toolbar.addSeparator()

        toolbar_button_update_table = QAction(QIcon('img/ui/refresh.png'), 'Обновить таблицу', self)
        toolbar_button_update_table.setStatusTip('Обновить таблицу')
        toolbar_button_update_table.setCheckable(True)
        toolbar_button_update_table.triggered.connect(self.callUpdateTable)
        toolbar.addAction(toolbar_button_update_table)
        self.setStatusBar(QStatusBar(self))

        toolbar.addSeparator()

        central = QWidget(self)
        self.setCentralWidget(central)
        self.grid = QGridLayout(self)
        central.setLayout(self.grid)

        self.table = QTableWidget(self)
        self.table.setColumnCount(4)
        self.table.setRowCount(50)
        self.table.setHorizontalHeaderLabels(['Код дисциплины', 'Наименование', 'Часы', 'ID студента'])
        for i, v in enumerate(self.discipline_service.get()):
            self.table.setItem(i, 0, QTableWidgetItem(str(v['subject_code'])))
            self.table.setItem(i, 1, QTableWidgetItem(str(v['subject_name'])))
            self.table.setItem(i, 2, QTableWidgetItem(str(v['hours'])))
            self.table.setItem(i, 3, QTableWidgetItem(str(v['student_id'])))
        self.grid.addWidget(self.table, 0, 0)

        self.show()

    def callUpdateTable(self, state):
        if state:
            self.close()
            a = Discipline()
            self.window.append(a)
            a.show()

    def call_create_discipline(self, state):
        if state:
            a = FormCreateDiscipline()
            self.window.append(a)
            a.show()

    def call_delete_discipline(self, state):
        if state:
            a = FormDeleteDiscipline()
            self.window.append(a)
            a.show()


class FormCreateDiscipline(QMainWindow):
    def __init__(self):
        self.window = []
        QMainWindow.__init__(self)

        self.dis_service = DisciplineService()
        self.student_service = StudentService()

        self.setMinimumSize(QSize(320, 270))
        self.setWindowTitle('Создание дисциплины')

        self.name_label = QLabel(self)
        self.name_label.setText("Наименование")
        self.name_label.move(20, 20)

        self.name = QLineEdit(self)
        self.name.move(110, 20)
        self.name.resize(200, 32)

        self.hours_label = QLabel(self)
        self.hours_label.setText("Часы")
        self.hours_label.move(20, 60)

        self.hours = QLineEdit(self)
        self.hours.move(110, 60)
        self.hours.resize(200, 32)

        self.combo_box_label_user = QLabel(self)
        self.combo_box_label_user.setText("ID студента")
        self.combo_box_label_user.move(20, 125)

        self.combo_discipline = QComboBox(self)
        for student in self.student_service.get():
            self.combo_discipline.addItem(str(student['id']))
        self.combo_discipline.move(110, 125)
        self.combo_discipline.resize(200, 32)

        button = QPushButton('Создать', self)
        button.clicked.connect(self.clickMetod)
        button.resize(200, 32)
        button.move(80, 225)

    def clickMetod(self):
        id = self.dis_service.count() + 1
        name = self.name.text()
        hours = self.hours.text()
        student = self.combo_discipline.currentText()
        self.dis_service.create(id, name, hours, student)
        self.close()

        a = ErrorException(title='Успех', text='Дисциплина создана')
        self.window.append(a)
        a.show()


class FormDeleteDiscipline(QMainWindow):
    def __init__(self):
        self.window = []
        QMainWindow.__init__(self)

        self.dis = DisciplineService()

        self.setMinimumSize(QSize(320, 180))
        self.setWindowTitle('Удалить дисциплину')

        self.idLabel = QLabel(self)
        self.idLabel.setText('ID:')
        self.idLabel.move(20, 20)

        self.idLine = QComboBox(self)
        for item in self.dis.get():
            self.idLine.addItem(str(item['subject_code']))

        self.idLine.move(80, 20)
        self.idLine.resize(200, 32)

        button = QPushButton('Удалить', self)
        button.clicked.connect(self.clickMetod)
        button.resize(200, 32)
        button.move(80, 120)

    def clickMetod(self):
        self.dis.delete(int(self.idLine.currentText()))
        self.idLine.clear()
        self.close()

        a = ErrorException(title='Успех', text='Удалено')
        self.window.append(a)
        a.show()
