from dataclasses import dataclass, field

@dataclass
class Task:

    task_id: int
    created_at: str
    description : str
    is_completed : bool

    _task_id: int = field(init=False, repr=False)
    _created_at: str = field(init=False, repr=False)
    _description: str = field(init=False, repr=False)
    _is_completed: bool = field(init=False, repr=False)


    @property
    def task_id(self) -> int:
        return self._task_id

    @task_id.setter
    def task_id(self, task_id: int):
        self._task_id = task_id

    @property
    def created_at(self) -> str:
        return self._created_at

    @created_at.setter
    def created_at(self, created_at: str):
        self._created_at = created_at

    @property
    def description(self) -> str:
        return self._description

    @description.setter
    def description(self, description: str):
        self._description = description

    @property
    def is_completed(self) -> bool:
        return self._is_completed

    @is_completed.setter
    def is_completed(self, is_completed: bool):
        self._is_completed = is_completed