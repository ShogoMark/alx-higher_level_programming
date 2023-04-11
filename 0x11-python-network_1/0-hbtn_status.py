#!/usr/bin/python3
#Python scripts that fetches url

import urllib.request


if __name__ == "__main__":
"""Function not to run if not in main"""

	with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as response:
	"""Opening the URL"""
		res = response.read()
		"""Reading the URL"""
print("Body response:")
print("\t- type: {}".format((type(res)))
print("\t- content: {}".format(res))
print("\t- utf8 content: {}".format(res.decode('utf-8'))
