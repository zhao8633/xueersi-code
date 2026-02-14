import time

def newprint(words, sleep_time = 0.1):
    for i in words:
        print(i , end = '',flush=True)
        time.sleep(sleep_time)
    print("",end="\n")

def newinput(words, sleep_time = 0.1):
    for i in words:
        print(i , end = '',flush=True)
        time.sleep(sleep_time)
    print("",end="\n")
    i = input()
    return(i)