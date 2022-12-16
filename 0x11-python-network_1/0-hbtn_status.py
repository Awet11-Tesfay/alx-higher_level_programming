#!/usr/bin/python3
"""python script that fetches from https://alx-intranet.hbtn.io/status"""

if __name__ == "__main__":
    import urllib.request
    from urllib.request import Request, urlopen
    req = 'https://alx-intranet.hbtn.io/status'
    with urllib.request.urlopen(req) as response:
        con = response.read()

        print("Body response:")
        print("\t- type: {}".format(type(con)))
        print("\t- content: {}".format(con))
        print("\t- utf8 content:".format(con.decode("utf-8")))