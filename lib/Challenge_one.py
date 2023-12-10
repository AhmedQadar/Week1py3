# function that takes in hour, minute add period ass parameters and returns the time in 24 hour format
def convert_to_24_hour(hour, minute, period):
    # check if the period is pm and the hour is not 12 then add 12 to the hour
    if period.lower() == "pm" and hour != 12:
        hour += 12
        # check if the period is am and the hour is 12 then set the hour to 0
    elif period.lower() == "am" and hour == 12:
        hour = 0

      # return the hour and minute in 24 hour format
    return f"{hour:02d}{minute:02d}"


# test cases
print(convert_to_24_hour(5, 30, "pm"))