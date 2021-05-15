import src.user_inputs.sender_etc as sender_etc
import src.user_inputs.receiver_list as receiver_list

import requests
import random
import logging
import time
import json


def master_setup(machine, tchain_id, urltype='url3'):
    sender_etc_dd = sender_etc.get_sender_etc_dict(machine)
    receivers = receiver_list.get_receiver_list()
    return sender_etc_dd, receivers


def prepare_top_section(method, param_list, the_url, method_type='POST'):
    tmp_id = 900000 + random.randrange(1, 99)
    head = dict([("Content-Type", "application/json;charset=UTF-8",)])
    my_request = requests.Request(method_type, the_url, headers=head)
    my_request.json = {"jsonrpc": "2.0", "method": method, "params": param_list, "id": tmp_id}
    return my_request


def setup_logging():
    the_level = logging.INFO
    tss = str(time.time())[:9]
    fname = "balanceTransfers" + tss + ".log"
    logging.basicConfig(filename=fname, level=the_level)


def unpack_d(settingsd, sender_etc_dd):
    chain = settingsd.get('chain')
    url3 = settingsd.get('url3')
    sender = sender_etc_dd.get('sender')
    pw = sender_etc_dd.get('pw')
    return chain, url3, sender, pw


def unpack_etc(sender_etc_dd):
    sender = sender_etc_dd.get('sender')
    pw = sender_etc_dd.get('pw')
    print("sender: ", sender, " pw: ", pw)
    return sender, pw

class SendRequest(object):

    @staticmethod
    def send_request(the_request):
        session = requests.Session()
        the_response = session.send(the_request)
        results_d = json.loads(the_response.text)
        #print(the_request.body)
        return results_d, the_response.text