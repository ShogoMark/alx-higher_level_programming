#!/usr/bin/python3
#Python scripts that fetches url

import urllib.request


if __name__ == "__main__":

#Opening the URL
	with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as response:
#reading the URL
		res = response.read()
print("Body response:")
print("\t- type: {}".format((type(res)))
print("\t- content: {}".format(res))
print("\t- utf8 content: {}".format(res.decode('utf-8'))
