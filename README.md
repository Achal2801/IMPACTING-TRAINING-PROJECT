# To-Do List Manager - Python Project

## Project Overview

This project is a **To-Do List Manager** application implemented in Python. The core objective of the project is to demonstrate the use of fundamental data structures (stack, queue, and linked list) in managing a to-do list. The application simulates a task management system that allows users to:

- Add and remove tasks using a **stack** (LIFO - Last In, First Out).
- Add and remove tasks using a **queue** (FIFO - First In, First Out).
- Maintain tasks in a **linked list**, where each task points to the next one, creating a chain of tasks.

## Features

- **Stack**: Tasks are added to the stack using the `push()` method and removed using `pop()`. The stack operates in a Last-In-First-Out (LIFO) manner, meaning the most recent task added is the first to be removed.
- **Queue**: Tasks are added to the queue using `enqueue()` and removed using `dequeue()`. The queue operates in a First-In-First-Out (FIFO) manner, meaning the oldest task is removed first.
- **Linked List**: A linked list structure is used to store tasks where each task is a node that points to the next task. Tasks are added to the list, and the entire list can be displayed using a `display()` method.

## Technologies Used

- **Python**: The project is implemented in Python 3.x, utilizing object-oriented programming to create classes for Stack, Queue, and Linked List.
- **Data Structures**: The project implements basic data structures like **Stack**, **Queue**, and **Linked List** to store and manage tasks efficiently.

## Installation

1. **Clone the repository** or download the project files to your local machine.
2. Ensure you have Python 3.x installed on your system.
3. No additional libraries are needed, as this project uses only built-in Python data structures and features.

To run the project, navigate to the project directory in your terminal and run:

```bash
python todo_app.py
```

## How It Works

- **Task Management with Stack**:
  - Tasks are added to the stack using `push()`, and the most recently added task can be removed using `pop()`.
  - The `peek()` method is used to view the most recent task without removing it.

- **Task Management with Queue**:
  - Tasks are added to the queue using `enqueue()`, and tasks are removed using `dequeue()`.
  - The tasks are displayed in a First-In-First-Out (FIFO) order.

- **Task Management with Linked List**:
  - Each task is stored as a node in the linked list. Tasks can be added to the list using the `add_task()` method, and the list of tasks can be displayed using the `display_tasks()` method.

### Example Usage

```python
# Example of using the To-Do List Manager
todo_app = ToDoApp()

# Adding tasks to the stack
todo_app.add_task_to_stack("Buy groceries")
todo_app.add_task_to_stack("Read a book")
todo_app.add_task_to_stack("Write code")

# Removing tasks from the stack
todo_app.remove_task_from_stack()

# Adding tasks to the queue
todo_app.add_task_to_queue("Go for a walk")
todo_app.add_task_to_queue("Clean the house")

# Display tasks in the queue
todo_app.display_queue_tasks()

# Add tasks to the linked list
todo_app.add_task_to_linked_list("Finish homework")
todo_app.add_task_to_linked_list("Buy a new laptop")
todo_app.display_linked_list_tasks()
```

### Example Output

```bash
Task 'Buy groceries' added to stack.
Task 'Read a book' added to stack.
Task 'Write code' added to stack.
Latest task in the stack:  Write code
Task 'Write code' removed from stack.
Task 'Go for a walk' added to queue.
Task 'Clean the house' added to queue.
Tasks in the queue (FIFO):
- Go for a walk
- Clean the house
Task 'Finish homework' added to linked list.
Task 'Buy a new laptop' added to linked list.
Current tasks in the list:
- Finish homework
- Buy a new laptop
```

## Solution and Conclusion

### **Solution:**
This Python project effectively uses three essential data structures—**Stack**, **Queue**, and **Linked List**—to manage and organize tasks in different manners. The project demonstrates the use of these structures for task management:

1. **Stack**: This is ideal for scenarios where you need to work with the most recently added tasks, like undo operations or reviewing the last added task.
2. **Queue**: This is ideal for scenarios where tasks should be handled in the order they were added, such as in a queue of items waiting for processing.
3. **Linked List**: This provides a flexible structure for storing a sequence of tasks, where each task is connected to the next, allowing for dynamic additions and removals.

### **Conclusion:**
This project successfully demonstrates the implementation and practical applications of stack, queue, and linked list data structures in Python. By applying these data structures to a real-world use case (task management), we can observe their strengths in different scenarios, such as managing tasks in a LIFO (stack), FIFO (queue), or linked sequence (linked list). These data structures provide efficient ways of organizing, accessing, and removing data, making them essential tools for a variety of software solutions.
