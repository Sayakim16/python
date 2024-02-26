def sum_of_singles(arr):
    # Create a dictionary to count occurrences of each number
    count_dict = {}
    for num in arr:
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1
            
    # Calculate the sum of numbers that occur exactly once
    sum_single = sum(num for num, count in count_dict.items() if count == 1)
    
    return sum_single

# Test cases
test_cases = [
    [4, 5, 7, 5, 4, 8],      # Example 1
    [1, 1, 2, 2, 3, 3, 4, 5], # Example 2
    [10, 20, 30, 40, 10, 20, 30, 50], # Example 3
    [0, 0, 0, 12, -1, -1, 2, 2]       # Example 4
]

# Iterate through each test case and print the result
for i, test in enumerate(test_cases, start=1):
    result = sum_of_singles(test)
    print(f"Test Case {i}: Sum of singles in {test} = {result}")