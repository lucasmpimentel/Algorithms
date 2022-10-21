def study_schedule(permanence_period, target_time):
    count = 0
    try:
        for a, b in permanence_period:
            if a <= target_time <= b:
                count += 1
        return count

    except TypeError:
        return None
