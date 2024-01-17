class Task:
    def __init__(self, title, status="Not Started"):
        self.title = title
        self.status = status

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, title):
        new_task = Task(title)
        self.tasks.append(new_task)
        print(f"Task '{title}' added successfully!")

    def view_tasks(self):
        for i, task in enumerate(self.tasks):
            print(f"{i+1}. {task.title} - {task.status}")

    def update_task(self, task_number, status):
        if task_number > 0 and task_number <= len(self.tasks):
            self.tasks[task_number-1].status = status
            print(f"Task '{self.tasks[task_number-1].title}' updated successfully!")
        else:
            print("Invalid task number.")

    def delete_task(self, task_number):
        if task_number > 0 and task_number <= len(self.tasks):
            print(f"Task '{self.tasks[task_number-1].title}' deleted successfully!")
            del self.tasks[task_number-1]
        else:
            print("Invalid task number.")

def main():
    todo_list = ToDoList()
    while True:
        print("\n1. Add Task\n2. View Tasks\n3. Update Task\n4. Delete Task\n5. Quit")
        option = int(input("Select an option: "))
        if option == 1:
            title = input("Enter task title: ")
            todo_list.add_task(title)
        elif option == 2:
            todo_list.view_tasks()
        elif option == 3:
            task_number = int(input("Enter task number to update: "))
            status = input("Enter new status: ")
            todo_list.update_task(task_number, status)
        elif option == 4:
            task_number = int(input("Enter task number to delete: "))
            todo_list.delete_task(task_number)
        elif option == 5:
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
