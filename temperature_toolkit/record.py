class TemperatureRecord:
    def __init__(self, date, readings, scale):
        self.date = date
        self.readings = readings if readings else []
        self.scale = scale.lower()

    def convert_to(self, target_scale):
        from temperature_toolkit.converter import convert
        target_scale = target_scale.lower()
        if target_scale == self.scale:
            return
        if target_scale not in ['celsius', 'fahrenheit', 'kelvin']:
            raise ValueError("Invalid target scale")
        self.readings = [convert(temp, self.scale, target_scale) for temp in self.readings]
        self.scale = target_scale

    def get_summary(self):
        if not self.readings:
            return {
                'date': self.date,
                'scale': self.scale,
                'min': 0,
                'max': 0,
                'avg': 0
            }
        return {
            'date': self.date,
            'scale': self.scale,
            'min': min(self.readings),
            'max': max(self.readings),
            'avg': round(sum(self.readings) / len(self.readings), 2)
        }

    def is_above_threshold(self, threshold):
        if not self.readings:
            return False
        return all(temp > threshold for temp in self.readings)