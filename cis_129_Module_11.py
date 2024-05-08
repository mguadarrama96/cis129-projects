# 9.1
def save_grades():
  grades = []
  print("Enter grades one by one. Type 'done' when finished:")

  # Loop to collect grades
  while True:
      grade = input("Enter grade (or 'done'): ")
      if grade.lower() == 'done':
          break
      try:
          # Validate and store the grade
          grades.append(float(grade))
      except ValueError:
          print("Please enter a valid number or 'done'.")

  # Save grades to a file
  with open('grades.txt', 'w') as file:
      for grade in grades:
          file.write(f"{grade}\n")

  print("Grades saved to grades.txt")

# Call the function to start the process
save_grades()

# 9.2
def read_and_calculate_grades():
    try:
        # Read grades from the file
        with open('grades.txt', 'r') as file:
            grades = [float(line.strip()) for line in file.readlines()]

        # Calculate total, count, and average
        total = sum(grades)
        count = len(grades)
        average = total / count if count > 0 else 0

        # Display individual grades and their total, count, and average
        print("Grades:")
        for grade in grades:
            print(grade)
        print(f"Total: {total}")
        print(f"Count: {count}")
        print(f"Average: {average:.2f}")

    except FileNotFoundError:
        print("The grades.txt file does not exist.")

# Call the function to start the process
read_and_calculate_grades()

# 9.3
import csv

# Function to write records to the CSV file
def write_grades_to_csv():
    with open('grades.csv', mode='w', newline='') as file:
        writer = csv.writer(file)

        # Loop to collect and write student grade information
        while True:
            first_name = input("Enter student's first name (or type 'exit' to finish): ")
            if first_name.lower() == 'exit':
                break

            last_name = input("Enter student's last name: ")
            grades = []
            for i in range(1, 4):
                while True:
                    try:
                        grade = int(input(f"Enter grade for exam {i}: "))
                        grades.append(grade)
                        break
                    except ValueError:
                        print("Please enter a valid integer grade.")

            # Write the student's information to the CSV file
            writer.writerow([first_name, last_name] + grades)
            print(f"Record for {first_name} {last_name} added to grades.csv.")

    print("All records have been written to grades.csv")

# Call the function to start the process
write_grades_to_csv()
