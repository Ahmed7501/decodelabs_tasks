def main():
    my_tasks = []

    while True:
        task = input("Enter a task (or 'quit' to exit): ")

        if task == 'quit':
            break

        my_tasks.append(task)

        print("\nYour Tasks:")
        for index, item in enumerate(my_tasks, start=1):
            print(f"{index}. {item}")
        print()


if __name__ == "__main__":
    main()
