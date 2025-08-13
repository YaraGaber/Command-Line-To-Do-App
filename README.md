Command-Line To-Do App

## 1\. Project Overview

his is a simple command-line To-Do application built in Python. It allows users to add, list, mark as done, and delete tasks. The application persists tasks to a JSON file, ensuring your to-do list is saved between sessions.



This version includes the following bonus features:

* **Priorities:** You can assign a priority (low, medium, high) to each task.

* **Tags:** The app automatically generates tags for each task based on its description.

* **Creation Timestamps:** Each task is automatically stamped with the date and time it was created.







-----

## 2\. How to Run the Program

1.  **Ensure you have Python installed.** This program was developed with Python 3.

2.  **Save the code.** Copy the provided Python code and save it as a file named `todo_app.py`.

3.  **Run from the terminal.** Open a terminal or command prompt, navigate to the directory where you saved `.py`, and run the following command:

    ```bash
    python todo_app.py
    ```

4.  **Use the commands.** The program will start and prompt you for commands. The available commands are:

      * `add`: Adds a new task.
      * `list`: Displays all current tasks.
      * `done <task_number>`: Marks a specific task as complete.
      * `delete <task_number>`: Permanently deletes a task.

-----

## 3\. Language and Tools

  * **Language:** Python 3
  * **Tools:** Standard Python libraries including `json`, `os`, `re`, and `datetime`. No external libraries are required.

-----

## 4\. Extra Features & Notes

  * **Data Persistence:** Tasks are saved to a file named `tasks.json` in the same directory. This means your to-do list will be preserved even if you close the application.
  * **Automatic Tagging:** When you add a new task, the application automatically generates **tags** by extracting keywords from your task description and filtering out common "stop words" like "a," "the," "in," etc. This can help with future organization or searching if the application were to be expanded.
  * **Timestamps:** Each task is automatically stamped with the date and time it was created, providing a useful record of when a task was added.
  * **Error Handling:** The program includes basic error handling for invalid commands and non-existent task numbers, providing helpful feedback to the user.

-----

