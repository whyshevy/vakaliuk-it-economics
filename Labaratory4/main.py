from tkinter import *
from tkinter import messagebox, ttk
import pyodbc
import sqlite3
from PythonBackendLabs.Labaratory4.DatabaseSettings import *
import psycopg2

root = Tk()
root.title("AutomationOfTheFaculty Table (PostgreSQL)")


def save_new_values(subjects, teacherCourses, tasks, result):
    conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER,
                            password=DB_PASSWORD, host=DB_HOST, port=DB_PORT)
    cursor = conn.cursor()
    query = '''INSERT INTO AutomationOfTheFaculty(Subjects, TeacherCourses, Tasks, Result) VALUES (%s, %s, %s, %s)'''
    cursor.execute(query, (subjects, teacherCourses, tasks, result))
    messagebox.showinfo(title=None, message="Data successfully inserted")

    conn.commit()
    conn.close()

    display_values()


def delete_values(id):
    conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER,
                            password=DB_PASSWORD, host=DB_HOST, port=DB_PORT)
    cursor = conn.cursor()
    query = '''DELETE FROM AutomationOfTheFaculty WHERE Id=%s'''
    cursor.execute(query, (id))
    messagebox.showinfo(title=None, message="Data successfully deleted")

    conn.commit()
    conn.close()
    display_values()


conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER,
                        password=DB_PASSWORD, host=DB_HOST, port=DB_PORT)


def update_values(subjects, teacherCourses, tasks, result, id):
    cursor = conn.cursor()
    query = '''UPDATE AutomationOfTheFaculty SET Subjects=%s, TeacherCourses=%s, Tasks=%s, Result=%s WHERE Id=%s;'''
    cursor.execute(query, (subjects, teacherCourses, tasks, result, id))
    messagebox.showinfo(title=None, message="Data successfully updated")
    conn.commit()
    conn.close()
    display_values()


def search(id):
    conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER,
                            password=DB_PASSWORD, host=DB_HOST, port=DB_PORT)
    cursor = conn.cursor()
    query = '''SELECT * FROM AutomationOfTheFaculty where Id=%s'''
    cursor.execute(query, id)

    row = cursor.fetchone()
    print(row)
    display_search_result(row)

    conn.commit()
    conn.close()


def display_search_result(row):
    listbox = Listbox(frame, width=20, height=1)
    listbox.grid(row=9, columnspan=4, sticky=W + E)
    listbox.insert(END, row)


def display_values():
    conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER,
                            password=DB_PASSWORD, host=DB_HOST, port=DB_PORT)
    cursor = conn.cursor()
    query = '''SELECT * FROM AutomationOfTheFaculty'''
    cursor.execute(query)

    row = cursor.fetchall()

    listbox = Listbox(frame, width=140, height=5)
    listbox.grid(row=10, columnspan=4, sticky=W + E)
    for x in row:
        listbox.insert(END, x)

    print(row)
    conn.commit()
    conn.close()


def migrate_from_postgresql_to_sqlite():
    window = Toplevel(root)
    window.title("Migration From PostgreSQL To SQLite")
    window.geometry("1000x400")
    migrateToMSSQL = Button(window, text="Migrate", bg="orange", font=5, command=migration_from_sqlite_to_mssql)
    tree = ttk.Treeview(window, columns=('Id', 'Subjects', 'TeacherCourses', 'Tasks', 'Result'),
                        height=20, show='headings')
    migrateToMSSQL.place(x=0, y=0)

    tree.column('Id', width=130, anchor=CENTER)
    tree.column('Subjects', width=150, anchor=CENTER)
    tree.column('TeacherCourses', width=235, anchor=CENTER)
    tree.column('Tasks', width=155, anchor=CENTER)
    tree.column('Result', width=155, anchor=CENTER)

    tree.heading('Id', text='Id')
    tree.heading('Subjects', text='Subjects')
    tree.heading('TeacherCourses', text='TeacherCourses')
    tree.heading('Tasks', text='Tasks')
    tree.heading('Result', text='Result')

    tree.pack()

    sqliteConnection = sqlite3.connect("Sample.db")
    sqliteCursor = sqliteConnection.cursor()
    # connect to postgresql
    pgConnection = psycopg2.connect(dbname=DB_NAME, user=DB_USER,
                                    password=DB_PASSWORD, host=DB_HOST, port=DB_PORT)
    pgCursor = pgConnection.cursor()

    # select from the table
    pgCursor.execute("SELECT * FROM AutomationOfTheFaculty")
    rows = pgCursor.fetchall()

    # loop and insert into sqlite
    sqliteCursor.execute('''DROP TABLE AutomationOfTheFaculty''')
    sqliteCursor.execute('''CREATE TABLE IF NOT EXISTS AutomationOfTheFaculty(Id integer, 
        Subjects varchar(256), TeacherCourses varchar(256), Tasks varchar(256), Result varchar(256))''')
    for row in rows:
        sqliteCursor.execute(
            '''INSERT INTO AutomationOfTheFaculty (Id, Subjects, TeacherCourses, Tasks, Result) VALUES (:Id, 
            :Subjects, :TeacherCourses, :Tasks, :Result)''',
            {"Id": row[0], "Subjects": row[1], "TeacherCourses": row[2], "Tasks": row[3], "Result": row[4]})
        sqliteConnection.commit()

    sqliteCursor.execute('''SELECT * FROM AutomationOfTheFaculty''')
    [tree.delete(i) for i in tree.get_children()]
    [tree.insert('', 'end', values=valuesRow) for valuesRow in sqliteCursor.fetchall()]

    print(rows)

    # close all connections
    sqliteConnection.close()
    pgConnection.close()


def migration_from_sqlite_to_mssql():
    window = Toplevel(root)
    window.title("Migration From SQLite To MS SQL")

    tree = ttk.Treeview(window, columns=('Id', 'Subjects', 'TeacherCourses', 'Tasks', 'Result'),
                        height=20, show='headings')
    tree.column('Id', width=130, anchor=CENTER)
    tree.column('Subjects', width=150, anchor=CENTER)
    tree.column('TeacherCourses', width=235, anchor=CENTER)
    tree.column('Tasks', width=155, anchor=CENTER)
    tree.column('Result', width=155, anchor=CENTER)

    tree.heading('Id', text='Id')
    tree.heading('Subjects', text='Subjects')
    tree.heading('TeacherCourses', text='TeacherCourses')
    tree.heading('Tasks', text='Tasks')
    tree.heading('Result', text='Result')

    tree.pack()

    sqliteConnection = sqlite3.connect("Sample.db")
    sqliteCursor = sqliteConnection.cursor()
    mssqlConnection = pyodbc.connect(
        'DRIVER={SQL Server};SERVER=DESKTOP-LLQ6EQ7\SQLEXPRESS;PORT=1433;DATABASE=SampleDB;UID=Bogdan4ik;PWD=1234;Trusted_Connection=yes;')
    mssqlCursor = mssqlConnection.cursor()
    sqliteCursor.execute("SELECT * FROM AutomationOfTheFaculty")
    rows = sqliteCursor.fetchall()
    mssqlCursor.execute('''DROP TABLE AutomationOfTheFaculty ''')
    mssqlCursor.execute('''CREATE TABLE AutomationOfTheFaculty(Id int, 
            Subjects varchar(256), TeacherCourses varchar(256), Tasks varchar(256), Result varchar(256))''')
    for row in rows:
        mssqlCursor.execute(
            '''INSERT INTO AutomationOfTheFaculty (Id, Subjects, TeacherCourses, Tasks, Result) VALUES (?, 
            ?, ?, ?, ?)''', row[0], row[1], row[2], row[3], row[4])
        print(row)
        mssqlConnection.commit()

    mssqlCursor.execute('''SELECT * FROM AutomationOfTheFaculty''')
    [tree.delete(i) for i in tree.get_children()]
    [tree.insert('', 'end', values=valuesRow) for valuesRow in mssqlCursor.fetchall()]
    mssqlConnection.commit()

    sqliteConnection.close()
    mssqlConnection.close()

# Canvas
canvas = Canvas(root, height=500, width=1000)
canvas.pack()

frame = Frame()
frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)

label = Label(frame, text="Add values")
label.grid(row=0, column=1)

# Name Input
label = Label(frame, text="Subject")
label.grid(row=1, column=0)

entry_subjects = Entry(frame)
entry_subjects.grid(row=1, column=1, )
entry_subjects.focus()

# Age
label = Label(frame, text="Teacher Courses")
label.grid(row=2, column=0)

entry_teacher_courses = Entry(frame)
entry_teacher_courses.grid(row=2, column=1)

# Address
label = Label(frame, text="Tasks")
label.grid(row=3, column=0)

entry_tasks = Entry(frame)
entry_tasks.grid(row=3, column=1)

#
label = Label(frame, text="Result")
label.grid(row=4, column=0)

entry_result = Entry(frame)
entry_result.grid(row=4, column=1)
# Button
button = Button(frame, text="Add", bg="lightgreen", command=lambda: save_new_values(
    entry_subjects.get(), entry_teacher_courses.get(), entry_tasks.get(), entry_result.get()))
button.grid(row=5, column=0, sticky=W + E)

button = Button(frame, text="Update", bg="yellow",
                command=lambda: update_values(entry_subjects.get(), entry_teacher_courses.get(), entry_tasks.get(),
                                              entry_result.get(), id_search.get()))
button.grid(row=5, column=1, sticky=W + E)

button = Button(frame, text="Delete", bg="red", command=lambda: delete_values(id_search.get()))
button.grid(row=5, column=2, sticky=W + E)

button = Button(frame, text="Migrate to SQLite3", bg="orange", command=lambda: migrate_from_postgresql_to_sqlite())
button.grid(row=8, column=1, sticky=W + E)

# Search
label = Label(frame, text="Search Data")
label.grid(row=6, column=1)

label = Label(frame, text="Search By ID")
label.grid(row=7, column=0)

id_search = Entry(frame)
id_search.grid(row=7, column=1)

button = Button(frame, text="Search", command=lambda: search(id_search.get()))
button.grid(row=7, column=2)

display_values()
root.mainloop()
