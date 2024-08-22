def study_schedule(permanence_period, target_time):
    if not all(
        isinstance(period, tuple) and len(period) == 2
        for period in permanence_period
    ):
        return None

    if not all(
        isinstance(period[0], int) and isinstance(period[1], int)
        for period in permanence_period
    ):
        return None

    if not isinstance(target_time, int):
        return None

    return sum(
        1 for start, end in permanence_period if start <= target_time <= end
    )
