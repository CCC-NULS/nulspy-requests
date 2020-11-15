#!/usr/bin/python3.7

import requests
import random


def get_top(method, plist, url, met_type='POST'):
    method_type = 'POST'
    if met_type == 3:
        method_type = 'GET'
    print("method_type is:  ", method_type)
    idd = 900000 + random.randrange(1, 99)
    head = dict([("Content-Type", "application/json;charset=UTF-8",)])
    reqr = requests.Request(method_type, url, headers=head)
    reqr.json = {"jsonrpc": "2.0", "method": method, "params": plist, "id": idd}
    return reqr
