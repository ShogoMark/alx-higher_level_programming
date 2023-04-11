#!/usr/bin/python3
#Python scripts that fetches url

import urllib.request

if __name__ == "__main__":

#Opening the URL
	with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as response:
#reading the URL
		res = response.read()
print("	- {}".format(res))
