import time
wait_time=1
max_retries=5
attems=0

while attems<max_retries:
    print(f"Attems {attems+1} - wait time {wait_time}")
    time.sleep(wait_time)
    wait_time *=2
    attems +=1