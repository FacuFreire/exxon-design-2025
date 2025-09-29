#!/usr/bin/env python3
"""
Reusable string filtering utilities using predicates
Requirements: No built-in reduce APIs
"""

class StringFilter:
    """A reusable class for filtering strings based on predicate functions"""
    
    @staticmethod
    def filter_by_predicate(string_list, predicate):
        """
        Filter strings using a custom predicate function
        
        Args:
            string_list (list): List of strings to filter
            predicate (function): Function that takes a string and returns True/False
            
        Returns:
            list: Strings for which predicate returns True
        """
        result = []
        for string in string_list:
            if string and predicate(string):  # Only test non-empty strings
                result.append(string)
        return result
    
    @staticmethod
    def filter_by_starting_character(string_list, character, case_sensitive=False):
        """
        Filter strings by starting character using predicate approach
        
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
        
        def starts_with_char(s):
            if case_sensitive:
                return s[0] == character
            else:
                return s[0].upper() == character.upper()
        
        return StringFilter.filter_by_predicate(string_list, starts_with_char)
    
    @staticmethod
    def filter_by_ending_character(string_list, character, case_sensitive=False):
        """Filter strings by ending character using predicate approach"""
        if not isinstance(character, str) or len(character) != 1:
            raise ValueError("Character must be a single character string")
        
        def ends_with_char(s):
            if case_sensitive:
                return s[-1] == character
            else:
                return s[-1].upper() == character.upper()
        
        return StringFilter.filter_by_predicate(string_list, ends_with_char)
    
    @staticmethod
    def filter_by_length(string_list, min_length=None, max_length=None):
        """Filter strings by length using predicate approach"""
        def length_predicate(s):
            length = len(s)
            return (min_length is None or length >= min_length) and \
                   (max_length is None or length <= max_length)
        
        return StringFilter.filter_by_predicate(string_list, length_predicate)
    
    @staticmethod
    def filter_by_contains(string_list, substring, case_sensitive=False):
        """Filter strings by substring using predicate approach"""
        def contains_predicate(s):
            if case_sensitive:
                return substring in s
            else:
                return substring.upper() in s.upper()
        
        return StringFilter.filter_by_predicate(string_list, contains_predicate)
    
    @staticmethod
    def combine_predicates_and(pred1, pred2):
        """Combine two predicates with AND logic"""
        return lambda x: pred1(x) and pred2(x)
    
    @staticmethod
    def combine_predicates_or(pred1, pred2):
        """Combine two predicates with OR logic"""
        return lambda x: pred1(x) or pred2(x)
    
    @staticmethod
    def negate_predicate(predicate):
        """Negate a predicate (NOT logic)"""
        return lambda x: not predicate(x)


# ============================================
# Predicate Functions for Common Use Cases
# ============================================

def starts_with_e(text):
    """Predicate: Does text start with 'E' (case-insensitive)?"""
    return text[0].upper() == 'E' if text else False

def starts_with_vowel(text):
    """Predicate: Does text start with a vowel?"""
    return text[0].upper() in 'AEIOU' if text else False

def is_longer_than_5(text):
    """Predicate: Is text longer than 5 characters?"""
    return len(text) > 5

def is_shorter_than_4(text):
    """Predicate: Is text shorter than 4 characters?"""
    return len(text) < 4

def contains_double_letters(text):
    """Predicate: Does text contain consecutive identical letters?"""
    for i in range(len(text) - 1):
        if text[i].upper() == text[i + 1].upper():
            return True
    return False

def has_uppercase_letters(text):
    """Predicate: Does text contain any uppercase letters?"""
    for char in text:
        if char.isupper():
            return True
    return False

def is_all_alphabetic(text):
    """Predicate: Does text contain only alphabetic characters?"""
    for char in text:
        if not char.isalpha():
            return False
    return True


# ============================================
# Legacy Compatibility Function
# ============================================

def filter_strings_starting_with_e(string_list):
    """
    Legacy function: Filter a list of strings to return only those that begin with "E"
    This function is kept for backward compatibility
    
    Args:
        string_list (list): List of strings to filter
        
    Returns:
        list: List of strings that begin with "E"
    """
    return StringFilter.filter_by_predicate(string_list, starts_with_e)
    

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
    
    # Using the legacy function (backward compatibility)
    filtered_strings_legacy = filter_strings_starting_with_e(strings)
    print("Using legacy function:")
    print(filtered_strings_legacy)
    
    # Using the new predicate-based approach
    filtered_strings_predicate = StringFilter.filter_by_predicate(strings, starts_with_e)
    print("Using predicate approach:")
    print(filtered_strings_predicate)
    
    # Using the starting character method
    filtered_strings_method = StringFilter.filter_by_starting_character(strings, 'E')
    print("Using starting character method:")
    print(filtered_strings_method)
    print()
    
    # ============================================
    # Demonstrate predicate reusability
    # ============================================
    print("="*60)
    print("PREDICATE-BASED FILTERING DEMONSTRATIONS")
    print("="*60)
    
    # Test individual predicates
    print("1. Using individual predicates:")
    test_strings = ["Eagle", "Apple", "Banana", "Elephant", "Programming", "Code"]
    print(f"Test list: {test_strings}")
    
    e_words = StringFilter.filter_by_predicate(test_strings, starts_with_e)
    vowel_words = StringFilter.filter_by_predicate(test_strings, starts_with_vowel)
    long_words = StringFilter.filter_by_predicate(test_strings, is_longer_than_5)
    short_words = StringFilter.filter_by_predicate(test_strings, is_shorter_than_4)
    
    print(f"   Starting with 'E': {e_words}")
    print(f"   Starting with vowel: {vowel_words}")
    print(f"   Longer than 5 chars: {long_words}")
    print(f"   Shorter than 4 chars: {short_words}")
    print()
    
    # Test compound predicates
    print("2. Combining predicates:")
    # Words that start with vowel AND are longer than 5 characters
    vowel_and_long = StringFilter.combine_predicates_and(starts_with_vowel, is_longer_than_5)
    result1 = StringFilter.filter_by_predicate(test_strings, vowel_and_long)
    print(f"   Vowel start AND long: {result1}")
    
    # Words that start with 'E' OR are shorter than 4 characters
    e_or_short = StringFilter.combine_predicates_or(starts_with_e, is_shorter_than_4)
    result2 = StringFilter.filter_by_predicate(test_strings, e_or_short)
    print(f"   Start with 'E' OR short: {result2}")
    
    # Words that do NOT start with a vowel
    not_vowel = StringFilter.negate_predicate(starts_with_vowel)
    result3 = StringFilter.filter_by_predicate(test_strings, not_vowel)
    print(f"   NOT starting with vowel: {result3}")
    print()
    
    # Test more complex predicates
    print("3. Complex predicate examples:")
    complex_test = ["Programming", "Apple", "Exxon", "Book", "aardvark", "TEST123", "Hello"]
    print(f"Test list: {complex_test}")
    
    double_letter_words = StringFilter.filter_by_predicate(complex_test, contains_double_letters)
    uppercase_words = StringFilter.filter_by_predicate(complex_test, has_uppercase_letters)
    alphabetic_words = StringFilter.filter_by_predicate(complex_test, is_all_alphabetic)
    
    print(f"   Contains double letters: {double_letter_words}")
    print(f"   Has uppercase letters: {uppercase_words}")
    print(f"   All alphabetic: {alphabetic_words}")
    print()
    
    # Test lambda predicates (inline predicates)
    print("4. Lambda (inline) predicates:")
    contains_a = lambda s: 'a' in s.lower()
    ends_with_ing = lambda s: s.lower().endswith('ing')
    has_exactly_4_chars = lambda s: len(s) == 4
    
    a_words = StringFilter.filter_by_predicate(complex_test, contains_a)
    ing_words = StringFilter.filter_by_predicate(complex_test, ends_with_ing)
    four_char_words = StringFilter.filter_by_predicate(complex_test, has_exactly_4_chars)
    
    print(f"   Contains 'a': {a_words}")
    print(f"   Ends with 'ing': {ing_words}")
    print(f"   Exactly 4 characters: {four_char_words}")
    print()
    
    # ============================================
    # Method-based filtering (still using predicates internally)
    # ============================================
    print("="*60)
    print("METHOD-BASED FILTERING (Using predicates internally)")
    print("="*60)
    
    method_test = ["Apple", "Banana", "Cherry", "Avocado", "Blueberry", "Citrus"]
    print(f"Test list: {method_test}")
    
    # Test different starting characters
    for char in ['A', 'B', 'C']:
        result = StringFilter.filter_by_starting_character(method_test, char)
        print(f"   Starting with '{char}': {result}")
    
    # Test ending characters
    ending_test = ["Apple", "Orange", "Grape", "Banana", "Cherry"]
    print(f"\nEnding test list: {ending_test}")
    ending_with_e = StringFilter.filter_by_ending_character(ending_test, 'e')
    ending_with_a = StringFilter.filter_by_ending_character(ending_test, 'a')
    print(f"   Ending with 'e': {ending_with_e}")
    print(f"   Ending with 'a': {ending_with_a}")
    
    # Test length filtering
    print(f"\nLength test list: {method_test}")
    short_method = StringFilter.filter_by_length(method_test, max_length=5)
    long_method = StringFilter.filter_by_length(method_test, min_length=7)
    medium_method = StringFilter.filter_by_length(method_test, min_length=5, max_length=6)
    print(f"   Short (≤5): {short_method}")
    print(f"   Long (≥7): {long_method}")
    print(f"   Medium (5-6): {medium_method}")
    
    # Test substring filtering
    substring_test = ["Programming", "Development", "Software", "Hardware", "Network"]
    print(f"\nSubstring test list: {substring_test}")
    contains_ing = StringFilter.filter_by_contains(substring_test, 'ing')
    contains_ware = StringFilter.filter_by_contains(substring_test, 'ware')
    print(f"   Contains 'ing': {contains_ing}")
    print(f"   Contains 'ware': {contains_ware}")
    print()
    
    # ============================================
    # Error handling demonstration
    # ============================================
    print("="*60)
    print("ERROR HANDLING DEMONSTRATIONS")
    print("="*60)
    
    # Test error handling
    print("Error handling:")
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
    safe_result = StringFilter.filter_by_predicate(problematic_list, starts_with_e)
    print(f"   Safe predicate filtering result: {safe_result}")
    print()
    
    # ============================================
    # Performance comparison demonstration
    # ============================================
    print("="*60)
    print("PREDICATE ADVANTAGES")
    print("="*60)
    
    print("Advantages of predicate-based approach:")
    print("1. ✓ Highly reusable - same predicate works everywhere")
    print("2. ✓ Composable - combine predicates with AND, OR, NOT")
    print("3. ✓ Testable - easy to unit test individual predicates")
    print("4. ✓ Readable - clear, named conditions")
    print("5. ✓ Flexible - create predicates dynamically with lambdas")
    print("6. ✓ Maintainable - centralized filtering logic")
    print("7. ✓ No built-in reduce APIs - meets requirements!")
    print()
    
    # ============================================
    # Legacy compatibility test
    # ============================================
    print("="*60)
    print("LEGACY COMPATIBILITY")
    print("="*60)
    
    # Additional test cases for legacy function
    test_cases = [
        ["Eagle", "bird", "Elephant", "cat", "Emu"],
        ["apple", "banana", "cherry"],
        ["Energy", "electricity", "Engine", "motor"],
        ["", "Empty", "full", "Endless"],
        []
    ]
    
    for i, test_case in enumerate(test_cases, 1):
        print(f"Legacy test case {i}: {test_case}")
        result = filter_strings_starting_with_e(test_case)
        print(f"Result: {result}")
        if i < len(test_cases):
            print()
    
if __name__ == "__main__":
    main()