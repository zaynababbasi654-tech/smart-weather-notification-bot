import time
import schedule

from src.data.weather_api import get_weather
from src.alerts.alert_detector import check_alert
from src.notifications.discord_notifier import send_discord_notification


CITIES = [
    "Islamabad",
    "Rawalpindi",
    "Lahore",
    "Karachi",
    "Murree",
    "Multan",
    "Abbottabad",
    "Sialkot",
    "Peshawar",
    "Quetta",
    "Faisalabad",
    "Gujranwala",
    "Hyderabad",
    "Bahawalpur",
    "Sukkur",
    "Muzaffarabad",
    "Gilgit",
    "Skardu",
    "Nathiagali",
    "Swat",
    "Dubai",
    "Abu Dhabi",
    "Doha",
    "London",
    "New York",
]


def check_all_cities():
    print("\n" + "=" * 50)
    print("🌤️ SMART WEATHER BOT")
    print("=" * 50)

    for city in CITIES:
        try:
            print(f"\n📍 Checking weather for {city}...")

            weather_data = get_weather(city)

            print(f"Temperature: {weather_data['temperature']}°C")
            print(f"Feels Like: {weather_data['feels_like']}°C")
            print(f"Humidity: {weather_data['humidity']}%")
            print(f"Condition: {weather_data['description']}")
            print(f"Wind Speed: {weather_data['wind_speed']} m/s")

            alerts = check_alert(weather_data)

            if alerts:
                print("\n🚨 ALERTS:")

                message = f"🚨 WEATHER ALERT — {city}\n\n"

                for alert in alerts:
                    print(f"- {alert}")
                    message += f"• {alert}\n"

                send_discord_notification(message)

                print("🔔 Alert sent to Discord!")

            else:
                print("✅ No dangerous weather conditions detected.")

        except Exception as e:
            print(f"❌ Could not get weather for {city}")
            print(f"Error: {e}")

    print("\n✅ Weather check completed.")


def run_scheduler():
    # Run immediately when the bot starts
    check_all_cities()

    # Check all cities every 30 minutes
    schedule.every(30).minutes.do(check_all_cities)

    print("\n⏰ Scheduler started.")
    print("🔄 Weather will be checked every 30 minutes.")

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    run_scheduler()