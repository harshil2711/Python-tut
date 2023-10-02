import time
import datetime
from win10toast import ToastNotifier

init_watertime = time.time()
init_eyetime = time.time()
init_phyexetime = time.time()


def notification(text):
    toaster = ToastNotifier()
    toaster.show_toast("Notification", text, duration=5)

while True:
    if time.time() - init_watertime > 30*60:
        notification("Drink water reminder")
        init_watertime = time.time()

    elif time.time() - init_phyexetime > 60*60:
        notification("Physical exercise reminder")
        init_phyexetime = time.time()

    elif time.time() - init_eyetime > 40*60:
        notification("Eye time reminder")
        init_eyetime = time.time()




