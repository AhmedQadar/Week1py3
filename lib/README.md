# CHALLENGE 1 :
 
    1-    Check if the given period is "pm" and the hour is not already 12:
          If true, increment the hour by 12. This is because in the 12-hour format, "pm" adds 12 hours to the hour.


    2-    Check if the given period is "am" and the hour is already 12:
          If true, set the hour to 0. This is because in the 12-hour format, "am" at 12:00 am corresponds to 00:00 in the 24-hour format.
          Return the formatted 24-hour time as a string:

    3-    Using an f-string, format the hour and minute as a string with two digits each. The :02d formatting ensures that       each component (hour and minute) will have at least two digits, with leading zeros if necessary.



# CHALLENGE 2 :

    1-        Initialize a variable positive_count to keep track of the number of positive integers.

    2-        Check if each of the three numbers (a, b, and c) is greater than 0:

                If a is greater than 0, increment positive_count by 1.
                If b is greater than 0, increment positive_count by 1.
                If c is greater than 0, increment positive_count by 1.
                Return True if positive_count is equal to 2, indicating that exactly two out of the three numbers are positive.

    3-        If positive_count is not equal to 2, return False. 


# CHALLENGE 3 : 
     
    1-          Initialize variables and data structures:

                vowels: A string containing the vowels.

                consonant_values: An empty list to store consonant values.

                char_positions: A dictionary mapping characters to their positions in the alphabet.

                current_consonant_value: A variable to keep track of the current consonant value.



    2-          Iterate through each character in the input string (s):

                If the character is not a vowel, add its position in the alphabet to the current_consonant_value.

                If the character is a vowel, check if there was a previous consonant sequence. If yes, append it to consonant_values and reset current_consonant_value to 0.

                Check for a consonant at the end of the string:

    3-          If there is a non-zero current_consonant_value at the end of the string, append it to consonant_values.



    4-
                Return the maximum value of consonant substrings using the max function, with a default value of 0 in case there are no consonants in the string.