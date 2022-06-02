import requests
import time
res = requests.get('https://jsonplaceholder.typicode.com/todos').json()
count = 0
def display_choise():
    print('[01]::Azerbaycan',' ','[02]::Russiya','red')
    time.sleep(0.3)
    print('[03]::Almaniya',' ','[04]::Albaniya')
    time.sleep(0.3)
    print('[05]::Yaponiya',' ','[06]::Cin')
    time.sleep(0.3)
    print('[07]::Sinqapur',' ','[08]::Hollandiya')
    time.sleep(0.3)
    print('[09]::Norvec',' ','[10]::Isvec')
    time.sleep(0.3)
    print('[11]::Another information')
display_choise()
choise = input()
if choise == '01':
    print("Azerbaycan")
if choise == '02':
    print("Russiya")
if choise == '03':
    print("Almaniya")
if choise == '04':
    print("Albaniya")
if choise == '05':
    print("Yaponiya")
if choise == '06':
    print("Cin")
if choise == '07':
    print("Sinqapur")
if choise == '08':
    print("Hollandiya")
if choise == '09':
    print("Norvec")
if choise == '10':
    print("Isvec")
if choise == '11':
    print("You want to get some information ")
    time.sleep(1)
    id1 = int(input("Please enter id of information::"))
    for i in res:
        if i['userId'] == id1:
            count+=1
            print(count,"::",i['title'])
            time.sleep(0.5)
    


