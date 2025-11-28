#!/usr/bin/env python3

# Starting and ending numbers for the prime number search range
start_number = 1
end_number = 250


def is_prime(number: int) -> bool:
    """
    Returns True if the given number is prime, False otherwise.

    A prime number is greater than or equal to 2 and only divisible
    by 1 and itself. For efficiency, the divisor check runs up to
    the square root of the number.
    """
    if number < 2:
        return False

    # Check divisibility from 2 up to sqrt(number)
    for divisor in range(2, int(number ** 0.5) + 1):
        if number % divisor == 0:
            return False

    return True


def main():
    try:
        print(f"Searching for prime numbers between {start_number} and {end_number}...")
        prime_list = []

        # Collect all prime numbers in the range
        for number in range(start_number, end_number + 1):
            if is_prime(number):
                prime_list.append(number)

        # Extra safety: confirm the list is not empty
        if not prime_list:
            print("No prime numbers were found in the specified range.")
            return

        print(f"Total prime numbers found: {len(prime_list)}\n")
        print("List of prime numbers:\n")

        # Display primes in columns, 10 per line
        for index, prime in enumerate(prime_list, start=1):
            print(f"{prime:4}", end="  ")
            if index % 10 == 0:
                print()

        print("\n")

        # Output file required by the lab instructions
        output_file = "results.txt"
        print(f"Saving results to '{output_file}'...")

        # Handle file write errors
        try:
            with open(output_file, "w", encoding="utf-8") as file:
                file.write("PRIME NUMBERS BETWEEN 1 AND 250\n")
                file.write(f"Total prime numbers found: {len(prime_list)}\n\n")
                file.write("Complete list of prime numbers:\n")

                for index, prime in enumerate(prime_list, start=1):
                    file.write(f"{prime:4}  ")
                    if index % 10 == 0:
                        file.write("\n")

            print(f"File successfully created: {output_file}")

        except OSError as e:
            print("Error while trying to write to the file:")
            print(f"Exception type: {type(e).__name__}")
            print(f"Details: {e}")
            return

    except Exception as e:
        # Captures unexpected errors in execution
        print("An unexpected error occurred during script execution.")
        print(f"Exception type: {type(e).__name__}")
        print(f"Details: {e}")


if __name__ == "__main__":
    # Ensures main() executes only when the script is run directly
    main()