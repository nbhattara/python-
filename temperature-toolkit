from temperature_toolkit import TemperatureRecord, convert, average_temperature_across_days

record1 = TemperatureRecord("2025-05-01", [20.0, 22.5, 19.0], "celsius")
record2 = TemperatureRecord("2025-05-02", [68.0, 70.0, 66.0], "fahrenheit")
record2.convert_to("celsius")

print("Record 1 Summary:", record1.get_summary())
print("Record 2 Summary:", record2.get_summary())

records = [record1, record2]
print("Overall Average:", average_temperature_across_days(records))
