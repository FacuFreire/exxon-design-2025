#!/usr/bin/env python3
"""
Reusable string filtering utilities
Requirements: No built-in reduce APIs
"""

class StringFilter:
    """A reusable class for filtering strings based on various criteria"""
    
    @staticmethod
    def filter_by_starting_character(string_list, character, case_sensitive=False):
        """
        Filter a list of strings to return only those that begin with a specific character
        
        Args:
            string_list (list): List of strings to filter
            character (str): The character to filter by (single character)
            case_sensitive (bool): Whether the comparison should be case-sensitive
            
        Returns:
            list: List of strings that begin with the specified character
            
        Raises:
            ValueError: If character is not a single character
        """
        if not isinstance(character, str) or len(character) != 1:
            raise ValueError("Character must be a single character string")
        
        result = []
        target_char = character if case_sensitive else character.upper()
        
        for string in string_list:
            if string:  # Check if string is not None or empty
                first_char = string[0] if case_sensitive else string[0].upper()
                if first_char == target_char:
                    result.append(string)
        
        return result
    

def main():
    """Main function to demonstrate the filtering functionality"""
    
    # Given list of strings
    strings = ["Exxon", "Mobil", "Bangalore", "Bdd", "Encapsulation"]
    
    print("Original list:")
    print(strings)
    print()
    
    # ============================================
    # Original requirement demonstration
    # ============================================
    print("="*60)
    print("ORIGINAL REQUIREMENT: Strings that begin with 'E'")
    print("="*60)
    
    # Using the new reusable class
    filtered_strings_new = StringFilter.filter_by_starting_character(strings, 'E')
    print("Using new reusable StringFilter class:")
    print(filtered_strings_new)
    print()
    
    # ============================================
    # Demonstrate enhanced reusability
    # ============================================
    print("="*60)
    print("ENHANCED REUSABILITY DEMONSTRATIONS")
    print("="*60)
    
    # Test different starting characters
    print("1. Filter by different starting characters:")
    test_strings = ["Apple", "Banana", "Cherry", "Avocado", "Blueberry", "Citrus"]
    print(f"Test list: {test_strings}")
    
    for char in ['A', 'B', 'C']:
        result = StringFilter.filter_by_starting_character(test_strings, char)
        print(f"   Starting with '{char}': {result}")
    print()
    
    # Test case sensitivity
    print("2. Case sensitivity options:")
    mixed_case = ["apple", "Apple", "APPLE", "banana", "Banana"]
    print(f"Mixed case list: {mixed_case}")
    case_insensitive = StringFilter.filter_by_starting_character(mixed_case, 'a', case_sensitive=False)
    case_sensitive = StringFilter.filter_by_starting_character(mixed_case, 'a', case_sensitive=True)
    print(f"   Case insensitive (default): {case_insensitive}")
    print(f"   Case sensitive: {case_sensitive}")
    print()
    

    
    # ============================================
    # Error handling demonstration
    # ============================================
    print("="*60)
    print("ERROR HANDLING DEMONSTRATIONS")
    print("="*60)
    
    # Test error handling
    print("6. Error handling:")
    try:
        StringFilter.filter_by_starting_character(strings, "AB")  # Invalid: multiple characters
    except ValueError as e:
        print(f"   Caught expected error for multiple characters: {e}")
    
    try:
        StringFilter.filter_by_starting_character(strings, "")  # Invalid: empty string
    except ValueError as e:
        print(f"   Caught expected error for empty string: {e}")
    
    # Test with None and empty strings
    problematic_list = ["Valid", None, "", "Another", ""]
    print(f"   Test with problematic list: {problematic_list}")
    safe_result = StringFilter.filter_by_starting_character(problematic_list, 'V')
    print(f"   Safe filtering result: {safe_result}")
    
if __name__ == "__main__":
    main()