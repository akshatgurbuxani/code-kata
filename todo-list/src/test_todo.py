import pytest
from task import Task
from todo import Todo

class TestTaskTodoIntegration:
    """Integration tests between Task and Todo classes."""
    
    def test_task_independence(self):
        """Test that tasks maintain independence when added to todo."""
        task1 = Task("Independent task 1")
        task2 = Task("Independent task 2")
        
        todo = Todo()
        todo.add_task(task1)
        todo.add_task(task2)
        
        assert not task1.is_completed()
        assert not task2.is_completed()
        assert not todo.is_completed(0)
        assert not todo.is_completed(1)
        
        # Complete one task directly
        task1.complete_task()
        
        # Check states
        assert task1.is_completed()
        assert not task2.is_completed()
        assert todo.is_completed(0)
        assert not todo.is_completed(1)
    
    def test_same_task_in_multiple_todos(self):
        """Test behavior when the same task is added to multiple todos."""
        task = Task("Shared task")
        
        todo1 = Todo()
        todo2 = Todo()
        
        todo1.add_task(task)
        todo2.add_task(task)
        
        assert not todo1.is_completed(0)
        assert not todo2.is_completed(0)

        # Complete in first todo
        todo1.complete_task(0)
        
        # Should be completed in both todos (same object)
        assert todo1.is_completed(0)
        assert todo2.is_completed(0)
        assert task.is_completed()
    
    def test_delete_task(self):
        """Test deleting a task."""
        todo = Todo()
        task1 = Task("First task")
        task2 = Task("Second task")
        task3 = Task("Third task")
        
        todo.add_task(task1)
        todo.add_task(task2)
        todo.add_task(task3)
        
        # Initially 3 tasks
        assert len(todo.get_tasks()) == 3
        
        # Delete middle task (index 1)
        todo.delete_task(1)
        
        # Should have 2 tasks now
        assert len(todo.get_tasks()) == 2
        
        # Remaining tasks should be first and third
        assert todo.get_task(0).get_task() == "First task"
        assert todo.get_task(1).get_task() == "Third task"