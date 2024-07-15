import os

def total_salary(path):
   
    try:
        # Open the file to read
        file = open(path, 'r')
        # Read all lines from the file
        lines = file.readlines()
        # Close the file
        file.close()

        salaries = []
        for line in lines:
            # Split the line into parts
            parts = line.split(',')
            # Get the salary from the line and convert it to an integer
            salary = int(parts[1])
            # Add the salary to the list
            salaries.append(salary)

        # Calculate the total sum of salaries
        total = sum(salaries)
        
        # Calculate the average salary
        average = total / len(salaries) if salaries else 0

        return total, average

    except FileNotFoundError:
        # Handling the case when the file is not found
        print("File is not found")
        return 0, 0
    except ValueError:
        # Handling the case when the data is incorrect in the file
        print("Incorrect data format in the file")
        return 0, 0
    except Exception as e:
        # Handling other types of errors
        print("Error:", e)
        return 0, 0

current_directory = os.path.dirname(__file__)
file_path = os.path.join(current_directory, "salary_file.txt")

# Example of using the function
total, average = total_salary("salary_file.txt")
print(f"The total sum of salaries: {total}, Average salary: {average}")
