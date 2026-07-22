# 🌦️ Weather App

A Python command-line Weather Application that fetches real-time weather data using the OpenWeather API.

---

## Features

- 🌍 Search weather by city
- 🌡️ Celsius and Fahrenheit support
- ☀️ Weather icons (emoji)
- 📅 Current date and time
- 🌅 Sunrise and sunset timings
- 💨 Wind speed
- 💧 Humidity
- 📈 Atmospheric pressure
- 📝 Search history
- 🗑️ Clear search history
- ⚠️ Error handling for invalid city, API key, and network issues

---

## Technologies Used

- Python 3
- OpenWeather API
- Requests
- python-dotenv

---

## Project Structure

```
Weather-App/
│
├── main.py
├── weather.py
├── config.py
├── history.py
├── utils.py
├── history.txt
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
```

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/Weather-App.git
```

### 2. Open the project

```bash
cd Weather-App
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

Windows:

```bash
venv\Scripts\activate
```

Linux/macOS:

```bash
source venv/bin/activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Create a `.env` file

```text
API_KEY=YOUR_OPENWEATHER_API_KEY
```

### 7. Run the application

```bash
python main.py
```

---

## Example Menu

```
1. Search Weather
2. View Search History
3. Clear Search History
4. Exit
```

---

## Example Output

```
🌤 Weather Report

City          : Chennai
Country       : IN
Temperature   : 32.5 °C
Feels Like    : 35.0 °C
Humidity      : 68%
Pressure      : 1008 hPa
Wind Speed    : 5.4 m/s
Sunrise       : 05:48:12 AM
Sunset        : 06:37:45 PM
```

---

## Future Improvements

- 5-Day Forecast
- Air Quality Index (AQI)
- Streamlit Web Interface
- Weather Maps
- Location Detection
- Graphical Charts

---

## License

This project is for learning and educational purposes.
