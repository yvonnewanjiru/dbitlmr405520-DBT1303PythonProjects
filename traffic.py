import json
import requests
import pandas as pd
import time
import matplotlib.pyplot as plt
from datetime import datetime

roads={
    1:"Road A",
    2:"Road B",
    3:"Road C"
    }

print(
    "1 For Road A\n"
    "2 For Road B\n"
    "3 For Road C\n"
    "4 For Road D\n"
)

road_in=int(input("Please Select Road To Monitor: "))

print(roads[road_in])

weekDay={
1:["Mon","Monday"],
2:["Tue","Tuesday"],
3:["Wed","Wednesday"],
4:["Thu","Thursday"],      
5:["Fri","Friday"],
6:["Sat","Saturday"],
7:["Sun","Sunday"]
}

week_no=(datetime.today().weekday())
current_day=weekDay[week_no][1]
day_abb=weekDay[week_no][0]
print("Please Wait As We generate A Graph\n")
print(f"Road: {roads[road_in]} \nDay Of Week: {current_day}")
time.sleep(4.5)
day=[]
congestion=[]
date=[]
week=[]

congestion_url="https://api.midway.tomtom.com/ranking/dailyStats/ITA_milan"
jams_url="https://api.midway.tomtom.com/ranking/liveHourly/ITA_milan"
limit=15
data_request=requests.get(congestion_url)
feedback=data_request.json()

for data in feedback:
    date.append(data["date"])
    day.append(data["weekday"])
    week.append(data["week"])
    congestion.append(data["congestion"])

fig_shape=plt.figure(figsize=(5,7))
plt.bar(day[:week_no],congestion[:week_no])
plt.show()

for conges,day in zip(congestion,day):
    if(day==day_abb):
      print(f"The Congestion is: {conges}% For {day}")
      break
