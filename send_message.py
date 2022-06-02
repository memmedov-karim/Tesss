import requests
import time
res = requests.get('https://jsonplaceholder.typicode.com/todos').json()
time.sleep(2)
id1 = int(input("Please enter id for information..."))
time.sleep(1)
count = 0
for i in res:
    if i['userId'] == id1:
        count+=1
        print(count,"::",i['title'])
        time.sleep(0.5)

