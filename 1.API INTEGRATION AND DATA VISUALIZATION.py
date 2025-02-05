import requests
import matplotlib.pyplot as plt
import seaborn as sns

name = input("Enter your name: ")
print(f"Welcome, {name}! Fetching weather data...")

API_KEY = "YOUR_OPENWEATHERMAP_API_KEY"
CITY = "New York"
URL = f"http://api.openweathermap.org/data/2.5/forecast?q={CITY}&appid={API_KEY}&units=metric"

response = requests.get(URL)
data = response.json()

dates = [item['dt_txt'] for item in data['list']]
temps = [item['main']['temp'] for item in data['list']]

plt.figure(figsize=(10, 5))
sns.lineplot(x=dates, y=temps, marker="o", color="b")
plt.xticks(rotation=45)
plt.xlabel("Date & Time")
plt.ylabel("Temperature (°C)")
plt.title(f"Weather Forecast for {CITY}")
plt.grid()
plt.show()

print(f"Thank you for using, {name}!")
