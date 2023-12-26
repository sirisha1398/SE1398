import matplotlib.pyplot as plt
a = 0.01
b = -0.5
c = 25
humidity = 79.0
temperature_range = range(0, 31)
precipitation_values = [a * temp**2 + b * humidity + c for temp in
temperature_range]
plt.figure(figsize=(8, 6))
plt.plot(temperature_range, precipitation_values, marker='o', linestyle='-', color='red',
label='Precipitation')plt.xlabel('Temperature (°C)')
plt.ylabel('Precipitation (mm)')
plt.title('Relationship between Temperature and Precipitation')
plt.grid(True)
plt.legend()
plt.show()
