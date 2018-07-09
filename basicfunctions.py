def minutes_to_hours(minutes):
    hours = minutes / 60.0
    return hours


def seconds_to_hours(seconds):
    hours = seconds / 3600
    return hours


print(minutes_to_hours(70) + 10)
print(seconds_to_hours(3895) + 20)

print(seconds_to_hours(7380))
print(seconds_to_hours(300))
