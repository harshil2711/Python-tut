# To start the executing funciton parellely

import threading
import time


def function1(seconds):
    print(f"sleeping for {seconds} seconds")
    time.sleep(seconds)


# Normal code
# function1(4)
time1 = time.perf_counter()

t1 = threading.Thread(target=function1 ,args=[4])
t2 = threading.Thread(target=function1 ,args=[3])
t3 = threading.Thread(target=function1 ,args=[2])

# It will just start the all the execution parelly. It will run  in background.
t1.start()
t2.start()
t3.start()

#Join funciton wait till the function complete the execution. t1 will till t1 complete the execution.
t1.join()
t2.join()
t3.join()

time2 = time.perf_counter()
print(time2-time1)



# To see the results use concurrent.futures module