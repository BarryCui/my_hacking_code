import requests
import sys

sub_list = open("wordlist.txt").read()
directories = sub_list.splitlines()

for i in directories:
    url_dir = f"http://{sys.argv[1]}/{i}.html"
    response = requests.get(url_dir)
    if response.status_code == 404:
        pass
    else:
        print("Valid directory: ", url_dir)
