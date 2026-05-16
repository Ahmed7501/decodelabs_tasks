def main():
    """Run the expense tracker loop."""
    total = 0  # Initialize total OUTSIDE the loop

    print("=" * 40)
    print("       Expense Tracker")
    print("=" * 40)

    while True:
        user_input = input("\nEnter expense amount (or 'quit' to exit): ")

        if user_input.lower() == "quit":
            break

        try:
            expense = float(user_input)
            total += expense  # Add valid amount to running total
            print(f"  Added: ${expense:.2f}")
            print(f"  Running Total: ${total:.2f}")
        except ValueError:
            print("  Invalid input. Please enter a numeric value.")

    print("\n" + "=" * 40)
    print(f"  Final Total: ${total:.2f}")
    print("=" * 40)
    print("Thank you for using Expense Tracker!")


if __name__ == "__main__":
    main()
