# variables of number of seconds in:
YEAR = 365 * 24 * 60 * 60
DAY = 24 * 60 * 60
HOUR = 60 * 60
MINUTE = 60


def format_duration(seconds):
    years = seconds // YEAR
    days = (seconds % YEAR) // DAY
    hours = (seconds % DAY) // HOUR
    minutes = (seconds % HOUR) // MINUTE
    secs = seconds % MINUTE

    if years > 0:
        if years == 1:
            f_years = "1 year"
        else:
            f_years = f"{years} years"
    else:
        f_years = None

    if days > 0:
        if days == 1:
            f_days = "1 day"
        else:
            f_days = f"{days} days"
    else:
        f_days = None

    if hours > 0:
        if hours == 1:
            f_hours = "1 hour"
        else:
            f_hours = f"{hours} hours"
    else:
        f_hours = None

    if minutes > 0:
        if minutes == 1:
            f_minutes = "1 minute"
        else:
            f_minutes = f"{minutes} minutes"
    else:
        f_minutes = None

    if secs > 0:
        if secs == 1:
            f_seconds = "1 second"
        else:
            f_seconds = f"{secs} seconds"
    else:
        f_seconds = None

    result = ""
    components = [item for item in [f_years, f_days, f_hours, f_minutes, f_seconds] if item]

    if len(components) == 1:
        result = components[-1]
    elif len(components) == 2:
        result = f"{components[-2]} and {components[-1]}"
    elif len(components) == 3:
        result = f"{components[-3]}, {components[-2]} and {components[-1]}"
    elif len(components) == 4:
        result = f"{components[-4]}, {components[-3]}, {components[-2]} and {components[-1]}"
    elif len(components) == 5:
        result = f"{components[-5]}, {components[-4]}, {components[-3]}, {components[-2]} and {components[-1]}"
    else:
        result = "now"
    return result


print(format_duration(120))
