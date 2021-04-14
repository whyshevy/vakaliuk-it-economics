from tkinter import *
from tkinter import messagebox

import psycopg2

root = Tk()
root.title("AutomationOfTheFaculty Table (PostgreSQL)")


def save_new_values(subjects, teacherCourses, tasks, result):
    conn = psycopg2.connect(dbname="postgres", user="postgres",
                            password="pass", host="localhost", port="5432")
    cursor = conn.cursor()
    query = '''INSERT INTO AutomationOfTheFaculty(Subjects, TeacherCourses, Tasks, Result) VALUES (%s, %s, %s, %s)'''
    cursor.execute(query, (subjects, teacherCourses, tasks, result))
    messagebox.showinfo(title=None, message="Data successfully inserted")

    conn.commit()
    conn.close()

    display_values()


def delete_values(id):
    conn = psycopg2.connect(dbname="postgres", user="postgres",
                            password="pass", host="localhost", port="5432")
    cursor = conn.cursor()
    query = '''DELETE FROM AutomationOfTheFaculty WHERE Id=%s'''
    cursor.execute(query, (id))
    messagebox.showinfo(title=None, message="Data successfully deleted")

    conn.commit()
    conn.close()
    display_values()


def update_values(subjects, teacherCourses, tasks, result, id):
    conn = psycopg2.connect(dbname="postgres", user="postgres",
                            password="pass", host="localhost", port="5432")
    cursor = conn.cursor()
    query = '''UPDATE AutomationOfTheFaculty SET Subjects=%s, TeacherCourses=%s, Tasks=%s, Result=%s WHERE Id=%s;'''
    cursor.execute(query, (subjects, teacherCourses, tasks, result, id))
    messagebox.showinfo(title=None, message="Data successfully updated")
    conn.commit()
    conn.close()
    display_values()


def search(id):
    conn = psycopg2.connect(dbname="postgres", user="postgres",
                            password="pass", host="localhost", port="5432")
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
    conn = psycopg2.connect(dbname="postgres", user="postgres",
                            password="pass", host="localhost", port="5432")
    cursor = conn.cursor()
    query = '''SELECT * FROM AutomationOfTheFaculty'''
    cursor.execute(query)

    row = cursor.fetchall()

    listbox = Listbox(frame, width=140, height=5)
    listbox.grid(row=10, columnspan=4, sticky=W + E)
    for x in row:
        listbox.insert(END, x)

    conn.commit()
    conn.close()


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
button = Button(frame, text="Add", command=lambda: save_new_values(
    entry_subjects.get(), entry_teacher_courses.get(), entry_tasks.get(), entry_result.get()))
button.grid(row=5, column=1, sticky=W + E)

button = Button(frame, text="Update",
                command=lambda: update_values(entry_subjects.get(), entry_teacher_courses.get(), entry_tasks.get(),
                                              entry_result.get(), id_search.get()))
button.grid(row=5, column=3, sticky=W + E)

# Search
label = Label(frame, text="Search Data")
label.grid(row=6, column=1)

label = Label(frame, text="Search By ID")
label.grid(row=7, column=0)

id_search = Entry(frame)
id_search.grid(row=7, column=1)

button = Button(frame, text="Search", command=lambda: search(id_search.get()))
button.grid(row=7, column=2)

button = Button(frame, text="Delete", command=lambda: delete_values(id_search.get()))
button.grid(row=5, column=2, sticky=W + E)

display_values()
root.mainloop()
