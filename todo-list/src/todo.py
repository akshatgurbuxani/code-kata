from task import Task

class Todo:
    def __init__(self):
        self.tasks: list[Task] = []
    
    def add_task(self, task: Task) -> None:
        self.tasks.append(task)
    
    def get_tasks(self) -> list[Task]:
        """
        Returns the list of tasks.
        """
        return self.tasks.copy()
    
    def get_task(self, index: int) -> Task:
        """
        Returns the task at the given index.
        """
        if 0 <= index < len(self.tasks):
            return self.tasks[index]
        raise IndexError("Index out of range")
    
    def complete_task(self, index: int) -> None:
        """
        Completes the task at the given index.
        """
        if 0 <= index < len(self.tasks):
            self.tasks[index].complete_task()
            return
        raise IndexError("Index out of range")
    def is_completed(self, index: int) -> bool:
        """
        Returns True if the task at the given index is completed, False otherwise.
        """
        if 0 <= index < len(self.tasks):
            return self.tasks[index].is_completed()
        raise IndexError("Index out of range")
    
    def delete_task(self, index: int) -> None:
        """
        Deletes the task at the given index.
        """
        if 0 <= index < len(self.tasks):
            del self.tasks[index]
            return
        raise IndexError("Index out of range")