from src.notifications.discord_notifier import send_discord_notification

message = "🚨 TEST ALERT\nSmart Weather Bot is connected successfully!"

send_discord_notification(message)

print("Discord notification sent successfully!")