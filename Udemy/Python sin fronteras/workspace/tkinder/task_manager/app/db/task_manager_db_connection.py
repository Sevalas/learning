import sqlite3
from domain.task import Task
from mapper.taskMapper import TaskMapper
from typing import List
import pathlib


filepath = pathlib.Path(__file__).resolve().parent.__str__()+'\\todo.db'

dbConnection = sqlite3.connect(filepath)
dbCursor = dbConnection.cursor()

dbCursor.execute(
    """
        CREATE TABLE if not exists todo (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
            description TEXT NOT NULL,
            is_completed BOOLEAN NOT NULL
        );
    """
)
dbConnection.commit()

class DbConnection:

    def __init__(self):
        pass

    def returnTaskById(self, id: int):
        task: Task

        rowOfTask = dbCursor.execute(
            """
            SELECT *
            FROM todo
            WHERE id = ?
            """,
            (id, )
        ).fetchone()

        task = TaskMapper().returnTaskFromRow(rowOfTask)
        return task

    def insertTask(self, task: Task):
        dbCursor.execute(
            """
            INSERT INTO todo (description, is_completed)
            VALUES (?, ?);
            """,
            (task.description, task.is_completed)
        )
        dbConnection.commit()

    def returnTaskList(self):
        taskList: List[Task]

        rowOfTaskList = dbCursor.execute(
            """
            SELECT *
            FROM todo
            """).fetchall()

        taskList = TaskMapper().returnTaskListFromRowList(rowOfTaskList)
        return taskList

    def updateTaskState(self, id: int):
        task: Task
        task = self.returnTaskById(id)

        dbCursor.execute(
            """
            UPDATE todo
            SET is_completed = ?
            WHERE id = ?
            """,
            (not task.is_completed, id)
        )
        dbConnection.commit()

    def deleteTask(self, id: int):
        dbCursor.execute(
            """
            DELETE
            FROM todo
            WHERE id = ?
            """,
            (id, )
        )
        dbConnection.commit()