import psycopg2.extras
from tkinter import *
from Labaratory4.DatabaseSettings import *

connection = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST)

cur = connection.cursor(cursor_factory=psycopg2.extras.DictCursor)
cur.execute("CREATE TABLE AutomationOfTheFaculty (Id SERIAL PRIMARY KEY, Subjects VARCHAR(256), TeacherCourses "
            "VARCHAR(256), Tasks VARCHAR(256), Result VARCHAR(256));")
cur.execute("DROP TABLE AutomationOfTheFaculty;")

cur.execute("INSERT INTO AutomationOfTheFaculty (Subjects, TeacherCourses, Tasks, Result) "
            "VALUES('Math Analysis', 'Probability theory and statistics','Find the stochastic result in student "
            "assignments', 'Done'), ('Objected-Oriental Programming', 'Native programming on C++', "
            "'Teach students to work with classes, pointers and functions', 'In Progress'), ('Backend Programming on "
            "Python', 'Django/Flask frameworks Introduction','Show how to create test application, using Django or "
            "Flask', 'Done'), ('Computer Science', 'Transfer Protocols','Introduce students to DNS and Mikrotik "
            "services', 'In Progress');")

connection.commit()
connection.close()
