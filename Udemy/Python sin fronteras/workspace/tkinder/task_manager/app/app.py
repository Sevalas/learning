from tkinter import *
from db.task_manager_db_connection import DbConnection
from constants.constants import *
from domain.task import Task
from typing import List

def getListOfTask():
    taskList: List(Task) = DbConnection().returnTaskList()
    return taskList

def insertTask():
    if taskEntry.get():
        task = Task(
            task_id=None,
            created_at=None,
            description=taskEntry.get(),
            is_completed=INCOMPLETE_TASK)
        DbConnection().insertTask(task)
        taskEntry.delete(0,END)
        renderTasks()

def updateTaskState(id: int):
    def _updateTaskState():
        DbConnection().updateTaskState(id)
        renderTasks()
    return _updateTaskState

def deleteTask(id: int):
    def _deleteTask():
        DbConnection().deleteTask(id)
        renderTasks()
    return _deleteTask

def renderTasks():
    taskList = getListOfTask()
    selectedTask: Task

    for widget in frame.winfo_children():
            widget.destroy()

    for indexOfTaskList in range(len(taskList)):
        selectedTask = taskList[indexOfTaskList]
        descriptionColor = '#969696' if selectedTask.is_completed else '#000000'

        taskCheckBox = Checkbutton(
            frame,
            text=selectedTask.description,
            width=42,
            anchor='w',
            fg=descriptionColor,
            command=updateTaskState(selectedTask.task_id)
        )

        taskCheckBox.select() if selectedTask.is_completed else taskCheckBox.deselect()
        taskCheckBox.grid(row=indexOfTaskList,column=0,sticky='w')

        deleteButton = Button(frame, text='Remove', command=deleteTask(selectedTask.task_id))
        deleteButton.grid(row=indexOfTaskList, column=1)

root = Tk()
root.title('Welcome to Task Manager')
root.grid()

taskLabel = Label(root, text='Task')
taskLabel.grid(row=0,column=0)

taskEntry = Entry(root,width=40)
taskEntry.grid(row=0,column=1)

addTaskButton = Button(root, text='Add', width=10, command=insertTask)
addTaskButton.grid(row=0,column=2)

frame = LabelFrame(root, text='My Task\'s', padx=5, pady=5)
frame.grid(row=1,column=0,columnspan=3,sticky='nswe',padx=5)

renderTasks()
taskEntry.focus()

root.bind("<Return>",lambda bind :insertTask())
root.mainloop()