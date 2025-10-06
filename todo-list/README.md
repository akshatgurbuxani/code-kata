# Todo List Kata

A programming kata that implements a simple todo list application with task management functionality.

## Rules

Create a todo list system with the following components:

- **Task class** that represents individual tasks with description and completion status
- **Todo class** that manages a collection of tasks
- Support for adding, retrieving, and completing tasks
- Index-based task operations with proper bounds checking
- Immutable task list returns to prevent external modification

## Example Output

```
# Creating and managing tasks
todo = Todo()
task1 = Task("Learn Python")
task2 = Task("Build a project")

todo.add_task(task1)
todo.add_task(task2)

print(len(todo.get_tasks()))  # 2
print(todo.is_completed(0))   # False

todo.complete_task(0)
print(todo.is_completed(0))   # True
```

## Run

```bash
python src/todo.py
```

## Test

```bash
pytest src/test_todo.py -v
```