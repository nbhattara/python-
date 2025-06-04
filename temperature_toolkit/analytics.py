def average_temperature_across_days(records):
    all_temps = []
    for record in records:
        all_temps.extend(record.readings)
    if not all_temps:
        return 0
    return round(sum(all_temps) / len(all_temps), 2)

def hottest_day(records):
    if not records:
        return ""
    max_avg = float('-inf')
    hottest = ""
    for record in records:
        if record.readings:
            avg = sum(record.readings) / len(record.readings)
            if avg > max_avg:
                max_avg = avg
                hottest = record.date
    return hottest

def detect_extreme_days(records, threshold):
    extreme_dates = []
    for record in records:
        if any(temp > threshold for temp in record.readings):
            extreme_dates.append(record.date)
    return extreme_dates

def temperature_range_for_each_day(records):
    ranges = {}
    for record in records:
        if record.readings:
            ranges[record.date] = (min(record.readings), max(record.readings))
        else:
            ranges[record.date] = (0, 0)
    return ranges

def temperature_trend(temps):
    if len(temps) < 2:
        return []
    trends = []
    for i in range(1, len(temps)):
        if temps[i] > temps[i-1]:
            trends.append('up')
        elif temps[i] < temps[i-1]:
            trends.append('down')
        else:
            trends.append('same')
    return trends

def detect_spike(temps, *, threshold=5):
    if len(temps) < 2:
        return False
    for i in range(1, len(temps)):
        if abs(temps[i] - temps[i-1]) >= threshold:
            return True
    return False
