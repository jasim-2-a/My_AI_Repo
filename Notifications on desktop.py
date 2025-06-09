import time
from plyer import notification


title = " Prayer Reminder"
message = "Time to take a short break fo prayer!"
interval = 60 * 30  

def send_notification():
    notification.notify(
        title=title,
        message=message,
        timeout=10  
    )

def main():
    print("🔔 Notification Scheduler Started!")
    try:
        while True:
            send_notification()
            time.sleep(interval)
    except KeyboardInterrupt:
        print("🛑 Notification Scheduler Stopped")

if __name__ == "__main__":
    main()

