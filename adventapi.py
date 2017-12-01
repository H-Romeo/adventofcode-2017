#!/usr/bin/env python

import requests
import sys

def getinput(level):
    with open('cookie.txt', 'r') as f:
        cookie = f.read().rstrip()

    cookies = dict(session=cookie)
    url = 'http://adventofcode.com/2017/day/{}/input'.format(level)
    return requests.get(url, cookies=cookies).text.rstrip()

def main():
    if len(sys.argv) > 1:
        level = sys.argv[1]
        print(getinput(level))
    else:
        print('Usage: ./adventapi.py <level>')

if __name__ == '__main__':
    main()
