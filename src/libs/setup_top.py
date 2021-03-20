#!/usr/bin/python3.7

import requests
import random
import logging
import time


def prepare_top_section(method, param_list, the_url, method_type='POST'):
    tmp_id = 900000 + random.randrange(1, 99)
    my_request = requests.Request(method_type, the_url, headers=dict([("Content-Type", "application/json;charset=UTF-8",)]))
    my_request.json = {"jsonrpc": "2.0", "method": method, "params": param_list, "id": tmp_id}
    return my_request


def setup_logging():
    the_level = logging.INFO
    tss = str(time.time())[:9]
    fname = "balanceTransfers" + tss + ".log"
    logging.basicConfig(filename=fname, level=the_level)

# class SetupLog:
#     @staticmethod
#     def setup_logging():
#         the_level = logging.INFO
#         tss = str(time.time())[:9]
#         fname = "balanceTransfers" + tss + ".log"
#         logging.basicConfig(filename=fname, level=the_level)