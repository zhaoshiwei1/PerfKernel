import time
from limitor import TokenBucket

bucket = TokenBucket()

failed = 0

success = 0

time.sleep(1)

print(time.time())
for i in range(0, 10000):
    if bucket.consume(500, 1):
        success += 1
    else:
        failed += 1
    time.sleep(0.001)
print(time.time())

print(success)
