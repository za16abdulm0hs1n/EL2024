from pynotifier import Notification, NotificationClient
from pynotifier.backends import platform
import psutil

def battery_percentage():
    battery = psutil.sensors_battery()
    percent = battery.percent
    return(percent)

def battery_notify(percent):
    c = NotificationClient()
    c.register_backend(platform.Backend())
    title = "Battery Percentage"
    message = str(percent)+"% Percentage Remaining"
    duration = 10
    notification = Notification(title=title, message = message, duration=duration)
    c.notify_all(notification)


percent = battery_percentage()
battery_notify(percent)