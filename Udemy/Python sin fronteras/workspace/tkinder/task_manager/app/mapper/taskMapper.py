from domain.task import Task
from constants.constants import *
from utils import utils
from typing import List

class TaskMapper:

    def __init__(self):
        pass

    def returnTaskFromRow(self, rowOfTask: tuple):
        task = None
        if rowOfTask is not None and len(rowOfTask) > 0:
            task = Task()
            task.task_id = rowOfTask[0]
            task.created_at = rowOfTask[1]
            task.description = rowOfTask[2]
            task.is_completed = utils.isTaskComplete(rowOfTask[3])

        return task

    def returnTaskListFromRowList(self, rowOfTaskList: List[tuple]):
        listOfTask: List[Task] = []

        for rowOfTask in rowOfTaskList:
            task = self.returnTaskFromRow(rowOfTask)
            listOfTask.append(task)

        return listOfTask