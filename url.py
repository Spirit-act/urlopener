import urllib3
from time import sleep

# Define URL
url = 'http://example.com/file.php'

conn = urllib3.PoolManager()

while True:
	try:
		res = conn.request('GET', url)
		res.status
		print(res.status, res.reason)
	except Exception as e:
		raise e
	sleep(5)
