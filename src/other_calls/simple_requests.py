#!/usr/bin/python3.7

import json
from src.libs.master_setup import master_setup, unpack_d
from src.libs.setup_top import get_top
from src.libs.send_req import SendRequest


class SimpleRequests(object):

    def __init__(self):
        machine = 1     #   machine = 1   # 1 for west, 0 for kathy

        settings_d, sender_etc_dd, self.receivers = master_setup(machine)
        self.chain, self.url3, self.sender, self.pw = unpack_d(settings_d, sender_etc_dd)
        self.url4 = settings_d.get('url4')
        self.remark = "transfer to account"
        self.asset = 1
        self.id = 99999
        
        self.emp_list = []

    def doit(self, method_nm, p_list, four=0):   #use url for url4
        if four:
            url = self.url4
        else:
            url = self.url3
        request = get_top(method_nm, p_list, url)
        response_d = SendRequest.send_request(request)

        print("  ANSWER to query ", method_nm, " is: ")
        print(url)
        print(" ---------> The response is: " + json.dumps(response_d) + " ---------> \n\n")

    def get_the_best_block(self):
        method_nm = "getBestBlockHeader"
        p = [self.chain]
        self.doit(method_nm, p)

    def get_chain_info(self):
        method_nm = "getChainInfo"
        p = [self.chain]
        self.doit(method_nm, p)

    def get_account(self, acct):
        method_nm = "getAccount"
        p = [self.chain, acct]
        self.doit(method_nm, p)

    def get_accountLedgerList(self, acct):
        method_nm = "getAccount"
        p = [self.chain, acct]
        self.doit(method_nm, p)

    def get_tx(self, tx_hash):
        method_nm = "getTx"
        p = [self.chain, tx_hash]
        self.doit(method_nm, p)


if __name__ == "__main__":
    s = SimpleRequests()
    # s.get_account('MWTIdGs2sv2p82qEM7mehidAPHSnJKaXi5pPv')
    # s.get_chain_info()
    s.get_the_best_block()


