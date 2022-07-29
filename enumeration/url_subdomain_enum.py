import requests
import sys

sub_list = open("wordlist.txt").read()
subdoms = sub_list.splitlines()

for sub in subdoms:
    sub_domain = f"http://{sub}.{sys.argv[1]}"

    try:
        requests.get(sub_domain)
    except Exception as e:
        pass
    else:
        print("Valid domain: ", sub_domain)