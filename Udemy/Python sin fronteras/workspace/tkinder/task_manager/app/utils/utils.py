from constants.constants import *
from domain.task import Task
from typing import List

def isTaskComplete(booleanOrIntegerValue: int or bool):
    return INCOMPLETE_TASK if booleanOrIntegerValue is 0 or booleanOrIntegerValue is INCOMPLETE_TASK else COMPLETED_TASK

def getTaskById(id: int, listOfTask: List[Task]):
    return next((task for task in listOfTask if task.task_id == id), None)
