#!/usr/bin/env python3
"""
Python script to filter strings that begin with "E"
Requirements: No built-in reduce APIs
"""

def filter_strings_starting_with_e(string_list):
    """
    Filter a list of strings to return only those that begin with "E"
    
    Args:
        string_list (list): List of strings to filter
        
    Returns:
        list: List of strings that begin with "E"
    """
    result = []
    
    for string in string_list:
        if string and string[0].upper() == 'E':
            result.append(string)
    
    return result


def main():
    """Main function to demonstrate the filtering functionality"""
    
    # Given list of strings
    strings = ["Exxon", "Mobil", "Bangalore", "Bdd", "Encapsulation"]
    
    print("Original list:")
    print(strings)
    
    # Filter strings that begin with "E"
    filtered_strings = filter_strings_starting_with_e(strings)
    
    print("\nStrings that begin with 'E':")
    print(filtered_strings)
    
    # Additional test cases
    print("\n" + "="*50)
    print("Additional test cases:")
    
    test_cases = [
        ["Eagle", "bird", "Elephant", "cat", "Emu"],
        ["apple", "banana", "cherry"],
        ["Energy", "electricity", "Engine", "motor"],
        ["", "Empty", "full", "Endless"],
        []
    ]
    
    for i, test_case in enumerate(test_cases, 1):
        print(f"\nTest case {i}: {test_case}")
        result = filter_strings_starting_with_e(test_case)
        print(f"Result: {result}")


if __name__ == "__main__":
    main()