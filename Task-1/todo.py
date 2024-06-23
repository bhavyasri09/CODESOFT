import json

class Task:
    def __init__(self, description):
        self.description = description
        self.completed = False

    def mark_complete(self):
        self.completed = True

    def __str__(self):
        return f"[{'x' if self.completed else ' '}] {self.description}"

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, description):
        task = Task(description)
        self.tasks.append(task)

    def view_tasks(self):
        for i, task in enumerate(self.tasks):
            print(f"{i + 1}. {task}")

    def mark_task_complete(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].mark_complete()

    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            del self.tasks[index]

    def save_to_file(self, filename):
        with open(filename, 'w') as file:
            tasks_data = [{"description": task.description, "completed": task.completed} for task in self.tasks]
            json.dump(tasks_data, file)

    def load_from_file(self, filename):
        try:
            with open(filename, 'r') as file:
                tasks_data = json.load(file)
                self.tasks = [Task(data["description"]) for data in tasks_data]
                for i, data in enumerate(tasks_data):
                    if data["completed"]:
                        self.tasks[i].mark_complete()
        except FileNotFoundError:
            print("File not found. Starting with an empty list.")

def main():
    todo_list = ToDoList()
    filename = "tasks.json"

    # Load tasks from the file
    todo_list.load_from_file(filename)

    while True:
        print("\nTo-Do List Application")
        print("1. Add a task")
        print("2. View all tasks")
        print("3. Mark a task as complete")
        print("4. Delete a task")
        print("5. Save tasks")
        print("6. Load tasks")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            description = input("Enter the task description: ")
            todo_list.add_task(description)
        elif choice == "2":
            todo_list.view_tasks()
        elif choice == "3":
            index = int(input("Enter the task number to mark as complete: ")) - 1
            todo_list.mark_task_complete(index)
        elif choice == "4":
            index = int(input("Enter the task number to delete: ")) - 1
            todo_list.delete_task(index)
        elif choice == "5":
            todo_list.save_to_file(filename)
        elif choice == "6":
            todo_list.load_from_file(filename)
        elif choice == "7":
            todo_list.save_to_file(filename)
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
