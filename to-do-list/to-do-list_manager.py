from pathlib import Path


def load_taks(path):
    tasks = {}
    if path.exists():
        with open(path, "r") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                name, text = line.split(":", 1)
                tasks[name.strip()] = text.strip()

    else:
        path.touch()
    return tasks


def save_tasks(tasks, path):
    current_highest_task = 0
    with open(path, "r") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            label = line.split(":", 1)[0]

            number = int(label.replace("task", "").strip())
            current_highest_task = max(current_highest_task, number)

    next_task_number = current_highest_task + 1

    with open(path, "a") as f:
        for key in tasks:
            key_number = int(key.replace("task", "").strip())
            if key_number >= next_task_number:
                f.write(f"task {key_number}:{tasks.get(key)}\n")


def add_task(tasks):
    while True:
        new_task = input("Enter the task: ")
        if new_task.strip() != "":
            break

    if tasks:
        last_key = list(tasks)[-1]
        next_num = int(last_key.replace("task", "").strip()) + 1
    else:
        next_num = 1
    next_key = f"task {next_num}"

    tasks[next_key] = new_task


def show_tasks(tasks):
    if tasks:
        for key in tasks:
            print(f"{key} is {tasks.get(key)}")
    else:
        print("no tasks")


def mark_done(tasks, task_done):
    for key in list(tasks):
        if int(key.replace("task", "").strip()) == task_done:
            tasks[key] = "done"


def delete_task(tasks, task_to_delete):
    for key in list(tasks):
        if int(key.replace("task", "").strip()) == task_to_del:
            del tasks[key]


# main

path = Path(__file__).parent / "saved_tasks.txt"

tasks = load_taks(path)

while True:
    print("--- TO-DO list ---")
    print("1. add a task")
    print("2. show all tasks")
    print("3. mark a task as done")
    print("4. delete a task")
    print("5. Quit")
    print()

    while True:
        try:
            user_input = int(input("You choice (1-5): "))
        except ValueError:
            print("please enter a number ")
            continue

        if user_input >= 1 and user_input <= 5:
            break
        print("please enter a number between 1 - 5")

    if user_input == 1:
        print()
        add_task(tasks)
        print()
    elif user_input == 2:
        print()
        show_tasks(tasks)
        print()
    elif user_input == 3:
        while True:
            try:
                task_done = int(input("which task is done: "))
                break
            except ValueError:
                print("please enter a number")

        mark_done(tasks, task_done)
        print()

    elif user_input == 4:
        while True:
            try:
                task_to_del = int(input("which task to delete: "))
                break
            except ValueError:
                print("please enter a number")

        delete_task(tasks, task_to_del)
        print()

    elif user_input == 5:
        print("have a good day! goodbye.")
        save_tasks(tasks, path)
        break
