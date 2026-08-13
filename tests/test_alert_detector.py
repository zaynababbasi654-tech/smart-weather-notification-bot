from src.alerts.alert_detector import check_alert


test_weather = {
    "temperature": 42,
    "wind_speed": 8,
    "weather": "Clear"
}

alerts = check_alert(test_weather)

print(alerts)