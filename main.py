from time import sleep
i = 10
while i >= 0:
    print(i)
    sleep(1)
    if i == 0:
        print("The End")
    i = i - 1