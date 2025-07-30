"""
Python String and Numeric Operations Demo
=========================================
This script demonstrates basic Python operations including:
- String manipulation with upper() and lower() methods
- Numeric operations with proper rounding for age values
- Variable assignment and type handling
- Print statements for output display

Author: Student practicing Python fundamentals
Purpose: Learning string methods and numeric rounding in Python
"""

# String variables demonstrating different cases
name_self = "kritthapath"           # Original name in lowercase
name_self_v2 = "KRITTHAPATH"        # Name in uppercase

# String method demonstrations
name_upper = name_self.upper()      # Call function .upper() to convert to uppercase
name_lower = name_self_v2.lower()   # Call function .lower() to convert to lowercase

# Display the string variables and their transformations
print(name_self)        # Output: kritthapath (original lowercase)
print(name_upper)       # Output: KRITTHAPATH (converted to uppercase)
print(name_lower)       # Output: kritthapath (converted to lowercase from name_self_v2)

# Age handling with decimal precision (year.month format)
age = 18.7              # Age represented as 18 years and 7 months (18.7)
result_age_floor = age.__floor__() # Using __floor__() to get the integer part (18)
result_age = round(age) # Use round() instead of floor() for better rounding accuracy
result_age_ceil = age.__ceil__()   # Using __ceil__() to get the next whole number (19)

# Display age information and data types
print(age)              # Output: 18.7 (original decimal age)
print(result_age_floor) # Output: 18 (using __floor__(), not recommended for age)
print(result_age)       # Output: 19 (rounded to nearest whole number)
print(result_age_ceil)  # Output: 19 (using __ceil__(), not recommended for age)
print(type(result_age)) # Output: <class 'int'> (data type of rounded age)

"""
Code Explanation:
================
1. String Operations:
   - name_self: stores a name in lowercase
   - name_self_v2: stores the same name in uppercase (kept as "KRITTHAPATH")
   - name_upper: demonstrates the .upper() method to convert strings to uppercase
   - name_lower: demonstrates the .lower() method to convert name_self_v2 to lowercase

2. Age Processing:
   - age: stores age as a decimal (18.7 = 18 years, 7 months)
   - result_age: uses round() function instead of __floor__() for proper rounding
   - round(18.7) = 19 (rounds to nearest integer for more accurate age representation)

3. Output Display:
   - Shows original values, transformed values, and data types
   - Demonstrates the difference between decimal and integer representations

The round() function provides better accuracy than floor() because:
- floor() always rounds down: 18.7 becomes 18
- round() rounds to nearest: 18.7 becomes 19 (more mathematically accurate)
"""