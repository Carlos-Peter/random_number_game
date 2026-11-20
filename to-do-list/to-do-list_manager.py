from pathlib import Path


def load_tasks(path):
    tasks = {}
    if path.exists():
        with open(path, "r") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                if ":" not in line:
                    continue
                name, text = line.split(":", 1)
                tasks[name.strip()] = text.strip()

    else:
        path.touch()
    return tasks


def save_tasks(tasks, path):
    lines = [f"{key}:{text}\n" for key, text in tasks.items()]
    with open(path, "w") as f:
        f.writelines(lines)


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

    tasks[next_key] = new_task.strip()


def show_tasks(tasks):
    if tasks:
        for key in tasks:
            print(f"{key} is {tasks.get(key)}")
    else:
        print("no tasks")


def get_index(tasks):
    while True:
        try:
            number = int(input("Task number: "))
        except ValueError:
            print("please enter a number")
            continue
        key = f"task {number}"
        if key in tasks:
            return key
        print("no such task")


def mark_done(tasks):
    if not tasks:
        print("No tasks")
    else:
        key = get_index(tasks)
        if not tasks[key].endswith(" [Done]"):
            tasks[key] += " [Done]"


def delete_task(tasks):
    if not tasks:
        print("No tasks")
    else:
        key = get_index(tasks)
        del tasks[key]


# main
def main():

    path = Path(__file__).parent / "saved_tasks.txt"

    tasks = load_tasks(path)

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
                user_input = int(input("Your choice (1-5): "))
            except ValueError:
                print("please enter a number ")
                continue

            if user_input >= 1 and user_input <= 5:
                break
            print("please enter a number between 1 - 5")

        if user_input == 1:
            print()
            add_task(tasks)
            save_tasks(tasks, path)
            print()
        elif user_input == 2:
            print()
            show_tasks(tasks)
            print()
        elif user_input == 3:
            mark_done(tasks)
            save_tasks(tasks, path)
            print()

        elif user_input == 4:
            delete_task(tasks)
            print()
            save_tasks(tasks, path)

        elif user_input == 5:
            print("have a good day! goodbye.")
            save_tasks(tasks, path)
            break


# calling main
main()
