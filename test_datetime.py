import time
from datetime import datetime, timezone, timedelta

start = time.time()             #number of seconds since 1970

print (datetime.now())
print (datetime.now(timezone.utc))

today = datetime.now()
tomorrow = today + timedelta(days=1)

print (today)
print (tomorrow)

print(today.strftime('%d-%m-%Y %H:%M:%S'))

end = time.time()
print (end - start)

import timeit

print(timeit.timeit('[x**2 for x in range (10)]'))



