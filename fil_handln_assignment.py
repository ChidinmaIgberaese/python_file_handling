# File Creation
try:
    # Create and write to a new file
    with open("my_file.txt", 'w') as file:
        file.write("First line: Hello, World!\n")
        file.write("Second line: 12345\n")
        file.write("Third line: Python is great!\n")
    print("File created and text written successfully.")

    # File Reading and Display
    with open("my_file.txt", 'r') as file:
        content = file.read()
        print("\n--- Reading File Content ---")
        print(content)

    # File Appending
    with open("my_file.txt", 'a') as file:
        file.write("Fourth line: Adding more text.\n")
        file.write("Fifth line: Appending is fun!\n")
        file.write("Sixth line: Numbers: 67890\n")
    print("\nText appended successfully.")

    # Reading the file again after appending
    with open("my_file.txt", 'r') as file:
        updated_content = file.read()
        print("\n--- Updated File Content ---")
        print(updated_content)

except FileNotFoundError:
    print("Error: The file was not found.")
except PermissionError:
    print("Error: You do not have permission to access the file.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
finally:
    print("\nFile handling process completed.")
