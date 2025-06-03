import time
import string
from itertools import product

# Take password input
password = input("Enter Password: ")
start = time.time()

# Character set to use in brute force
chars = string.ascii_letters + string.digits + string.punctuation

def brute_force(pwd, chars):
    max_length = 10  # Adjust this to support longer passwords
    for length in range(1, max_length + 1):
        for attempt in product(chars, repeat=length):
            guess = ''.join(attempt)
            print(f"\rTrying: {guess}", end='')  # Overwrites the same line
            if guess == pwd:
                return guess
    return None

# Call brute-force function
result = brute_force(password, chars)
end = time.time()

# Output result
if result:
    print(f"\nPassword found: {result}")
else:
    print("\nPassword not found (too complex or too long)")

print(f'Time taken: {round(end - start, 2)} seconds')
