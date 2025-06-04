def convert(value, from_unit, to_unit):
    from_unit = from_unit.lower()
    to_unit = to_unit.lower()
    if from_unit not in ['celsius', 'fahrenheit', 'kelvin'] or to_unit not in ['celsius', 'fahrenheit', 'kelvin']:
        raise ValueError("Invalid unit")
    if from_unit == to_unit:
        return round(value, 2)
    
    # Convert to Celsius first
    if from_unit == 'fahrenheit':
        celsius = (value - 32) * 5 / 9
    elif from_unit == 'kelvin':
        celsius = value - 273.15
    else:
        celsius = value
    
    # Convert from Celsius to target unit
    if to_unit == 'fahrenheit':
        result = (celsius * 9 / 5) + 32
    elif to_unit == 'kelvin':
        result = celsius + 273.15
    else:
        result = celsius
    
    return round(result, 2)