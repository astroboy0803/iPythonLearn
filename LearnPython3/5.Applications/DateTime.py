import calendar
import time
from datetime import datetime, timedelta, timezone

# 其它時間相關module
# third-party
# import pytz
# import dateutil

# time interval
tick = time.time()
print(f"tick since 1200am, January 1, 1970:{tick}")

# timetuple
timeTuple = time.localtime()
print(timeTuple)
print(timeTuple[0])

structTime = time.struct_time
print(structTime)

# current time
currentTime = time.localtime(time.time())
print(f"Local current time: {currentTime}")

# simple format - asctime
currentASCTime = time.asctime(currentTime)
print(f"Local Current ASC time: {currentASCTime}")

# calendar
cal = calendar.month(2016, 2)
print(f"Calendar: \n{cal}")

# datetime
now = datetime.now()
print(now)

aDate = datetime(2022, 2, 28, 0, 30)
print(aDate)
print(aDate.timestamp())
print(datetime.fromtimestamp(aDate.timestamp()))
print(datetime.utcfromtimestamp(aDate.timestamp()))

dateString = "2022-6-15 18:22:35"
toDate = datetime.strptime(dateString, "%Y-%m-%d %H:%M:%S")
print(toDate)
print(toDate.strftime("%a, %b %d %H:%M"))

af10DayDate = aDate + timedelta(days=10)
print(af10DayDate)
bf2HourDate = aDate - timedelta(hours=2)
print(bf2HourDate)

tz_utc_8 = timezone(timedelta(hours=8))
print(tz_utc_8)
print(now)

# 強制加上時區, 只是練習, 實際上要先轉為UTC+0再轉
print(now.replace(tzinfo=tz_utc_8))

utcNow = datetime.utcnow().replace(tzinfo=timezone.utc)
print(utcNow)
utc8Now = utcNow.replace(tzinfo=tz_utc_8)
print(utc8Now)
print(utc8Now.astimezone(tz_utc_8))
