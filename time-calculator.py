def add_time(start, duration, start_day = ''):
    lists, listd = [], []
    lists = start.split(':')
    lists[1] = lists[1].split(' ')
    listd = duration.split(':')

    # Turn times into integers
    listd = [int(i) for i in listd]
    lists[0] = int(lists[0])
    lists[1][0] = int(lists[1][0])

    # Initialise variables
    new_hours = new_mins = days = temp = hours_left = 0
    new_day = new_time = '' 
    wkdays = ('monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday')
    watch = lists[1][1]

    # Actual calculation
    new_mins = lists[1][0] + listd[1]
    if new_mins > 59:
        new_mins -= 60
        new_hours += 1

    new_hours += lists[0] + listd[0]
    days += new_hours // 24
    hours_left += new_hours % 24

    if hours_left > 11 and watch == 'AM':
        hours_left -= 12
        watch = "PM"
    elif hours_left > 11 and watch == 'PM':
        hours_left -= 12
        days += 1
        watch = 'AM'
    if hours_left == 0:
        hours_left = 12
    
    # Calculate the days
    start_day = start_day.lower()
    if start_day != '':
        idx = wkdays.index(start_day)
        temp = days % 7
        new_idx = idx + temp
        if new_idx > 6:
            new_idx = new_idx % 7
            new_day = ', ' + wkdays[new_idx].capitalize()
        else: 
            new_day = ', ' + wkdays[new_idx].capitalize()

    # Return strings in proper form
    if days == 0:
        if start_day != '':
            new_day = start_day.lower()
            new_time = f"{hours_left}:{new_mins:02d} {watch}, {new_day.capitalize()}"
        else:
            new_time = f"{hours_left}:{new_mins:02d} {watch}"
    elif days == 1:
         new_time = f"{hours_left}:{new_mins:02d} {watch}{new_day} (next day)"
    else:
        new_time = f"{hours_left}:{new_mins:02d} {watch}{new_day} ({days} days later)"

    return new_time