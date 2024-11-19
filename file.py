import sys


def main():
    # Check if filename was provided
    if len(sys.argv) != 2:
        print("Error: Please provide a filename as argument")
        sys.exit(1)

    filename = sys.argv[1]

    try:
        with open(filename, 'r') as file:
            for line_number, line in enumerate(file, 1):
                # Strip whitespace and split the line
                values = line.strip().split()

                # Check if we have exactly 2 values
                if len(values) != 2:
                    print(f"Error on line {line_number}: Expected 2 values, got {len(values)}")
                    continue

                try:
                    # Convert strings to floats and calculate sum
                    num1 = float(values[0])
                    num2 = float(values[1])
                    print(f"Line {line_number} sum: {num1 + num2}")
                except ValueError:
                    print(f"Error on line {line_number}: Invalid number format")
                    continue

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found")
        sys.exit(1)
    except PermissionError:
        print(f"Error: Permission denied to read file '{filename}'")
        sys.exit(1)


if __name__ == "__main__":
    main()