def solve(s):
    # Define  vowels
    vowels = "aeiou"
    # Define a list to store the consonant values
    consonant_values = []

    # Define mapping of characters to their positions in the alphabet
    char_positions = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 
                      'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 
                      't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26}
    
    # Initialize the current consonant value
    current_consonant_value = 0
    for char in s:
        if char not in vowels:
            # Check if the character is not a vowel, add its position in the alphabet to the value
            current_consonant_value += char_positions.get(char, 0)
        else:
            # Chreck if the character is a vowel, store the current consonant value and reset it
            if current_consonant_value:
                consonant_values.append(current_consonant_value)
                current_consonant_value = 0

    # Check for a consonant at the end of the string
    if current_consonant_value:
        consonant_values.append(current_consonant_value)

    # Return the maximum value of consonant substrings
    return max(consonant_values, default=0)

# Test cases
print(solve("zodiacs"))   # Output: 26
print(solve("strength"))  # Output: 57
