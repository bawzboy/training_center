import re

def main():
    print(convert_hours(input("Hours: ")))

def convert_hours(time_range):
    try:
        starting_time, ending_time = time_range.split(" to ")
    except ValueError:
        raise ValueError("Invalid format")
    
    start_24 = convert_to_24_hour(starting_time)
    end_24 = convert_to_24_hour(ending_time)
    return f"{start_24} to {end_24}"

def convert_to_24_hour(time_fragment):
    matches = re.search(r"(1[0-2]|0?[1-9]):?([0-5]\d)?", time_fragment)
    if not matches:
        raise ValueError("Invalid time format")
    
    hours = int(matches.group(1))
    minutes = matches.group(2)

    if minutes is None:
        minutes = 0
    else:
        minutes = int(minutes)

    if not (1 <= hours <= 12):
        raise ValueError("Invalid hours value")
    if not (0 <= minutes <= 59):
        raise ValueError("Invalid minute value")
    # Those do not seem to work...

    if time_fragment.endswith(" PM") and hours != 12:
        hours += 12
    elif time_fragment.endswith(" AM") and hours == 12:
        hours = 0

    return f"{hours:02}:{minutes:02}"

if __name__ == "__main__":
    main()
    