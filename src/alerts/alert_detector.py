TEMPERATURE_THRESHOLD = 40
WIND_THRESHOLD = 15


def check_alert(weather_data):
    alerts = []

    temperature = weather_data["temperature"]
    wind_speed = weather_data["wind_speed"]
    weather = weather_data["weather"]

    if temperature >= TEMPERATURE_THRESHOLD:
        alerts.append(
            f"Extreme heat detected: {temperature}°C"
        )

    if wind_speed >= WIND_THRESHOLD:
        alerts.append(
            f"Strong wind detected: {wind_speed} m/s"
        )

    if weather in ["Thunderstorm", "Tornado"]:
        alerts.append(
            f"Severe weather detected: {weather}"
        )

    return alerts