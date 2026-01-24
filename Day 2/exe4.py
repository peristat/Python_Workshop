while True:
    try:
        age = int(input("Enter age: "))
        break # Exit loop if input is valid
    except ValueError:
        print("Please enter a valid number (e.g., 25).")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
