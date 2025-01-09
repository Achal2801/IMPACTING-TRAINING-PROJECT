class Node:
    def __init__(self, data):
        self.data = data  # The task (data)
        self.next = None  # Pointer to the next node (task)

class LinkedList:
    def __init__(self):
        self.head = None

    def add_task(self, task):
        new_node = Node(task)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def display_tasks(self):
        current = self.head
        if not current:
            print("No tasks available.")
        else:
            print("Current tasks in the list:")
            while current:
                print(f"- {current.data}")
                current = current.next


class Stack:
    def __init__(self):
        self.stack = []

    def push(self, task):
        self.stack.append(task)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            return "Stack is empty."

    def is_empty(self):
        return len(self.stack) == 0

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        return "Stack is empty."


class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, task):
        self.queue.append(task)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        else:
            return "Queue is empty."

    def is_empty(self):
        return len(self.queue) == 0

    def display(self):
        if not self.is_empty():
            print("Tasks in the queue (FIFO):")
            for task in self.queue:
                print(f"- {task}")
        else:
            print("No tasks in the queue.")


# Main Application using the data structures
class ToDoApp:
    def __init__(self):
        self.stack = Stack()
        self.queue = Queue()
        self.linked_list = LinkedList()

    def add_task_to_stack(self, task):
        self.stack.push(task)
        print(f"Task '{task}' added to stack.")

    def remove_task_from_stack(self):
        task = self.stack.pop()
        print(f"Task '{task}' removed from stack.")

    def add_task_to_queue(self, task):
        self.queue.enqueue(task)
        print(f"Task '{task}' added to queue.")

    def remove_task_from_queue(self):
        task = self.queue.dequeue()
        print(f"Task '{task}' removed from queue.")

    def add_task_to_linked_list(self, task):
        self.linked_list.add_task(task)
        print(f"Task '{task}' added to linked list.")

    def display_linked_list_tasks(self):
        self.linked_list.display_tasks()

    def display_queue_tasks(self):
        self.queue.display()


# Example of using the To-Do List Manager
if __name__ == "__main__":
    todo_app = ToDoApp()

    # Adding tasks to the stack
    todo_app.add_task_to_stack("Buy groceries")
    todo_app.add_task_to_stack("Read a book")
    todo_app.add_task_to_stack("Write code")

    # Display the current task in stack
    print("Latest task in the stack: ", todo_app.stack.peek())

    # Removing tasks from the stack
    todo_app.remove_task_from_stack()

    # Adding tasks to the queue
    todo_app.add_task_to_queue("Go for a walk")
    todo_app.add_task_to_queue("Clean the house")

    # Display tasks in the queue
    todo_app.display_queue_tasks()

    # Add tasks to linked list
    todo_app.add_task_to_linked_list("Finish homework")
    todo_app.add_task_to_linked_list("Buy a new laptop")
    todo_app.display_linked_list_tasks()
