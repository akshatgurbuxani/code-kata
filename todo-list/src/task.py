class Task:
    def __init__(self, task: str, completed: bool = False):
        self.task = task
        self.completed = completed

    def get_task(self) -> str:
        return self.task

    def complete_task(self) -> None:
        self.completed = True
    
    def is_completed(self) -> bool:
        return self.completed