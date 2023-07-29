f = ['apple', 'banana', 'cherry', 'mango', 'orange']
import time
for x in f:
    print(x)
    time.sleep(2)
    if x == 'mango':
        break