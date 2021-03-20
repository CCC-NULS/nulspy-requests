#!/usr/bin/python3.7

from src.libs.master_setup import master_setup, unpack_d
from src.libs.setup_top import prepare_top_section
from src.libs.send_req import SendRequest
import logging


class AccountKeys(object):

    def __init__(self):
        machine = 1     #   machine = 1   # 1 for west, 0 for kathy

        settings_d, sender_etc_dd, self.receivers = master_setup(machine)
        self.chain, self.url3, self.sender, self.pw = unpack_d(settings_d, sender_etc_dd)
        self.url4 = settings_d.get('url4')
        self.remark = "none"
        self.asset = 1
        self.id = 99999

    def get_pri_key(self, addr, pww):
        method_nm = "getPriKey"

        p_list = [self.chain, addr, pww]
        request = prepare_top_section(method_nm, p_list, self.url4)
        resp_d, rstr = SendRequest.send_request(request)
        return resp_d.get('result')

    def get_account_byprikey(self, pk):
        method_nm = "getAddressByPriKey"
        p_list = [self.chain, pk]
        request = prepare_top_section(method_nm, p_list, self.url3)
        resp_d, rstr = SendRequest.send_request(request)
        return resp_d.get('result')

    def import_pri_key(self, pri_key):
        method_nm = "importPriKey"
        p_list = [self.chain, pri_key, self.pw]
        request = prepare_top_section(method_nm, p_list, self.url3)
        resp_d, rstr = SendRequest.send_request(request)
        return resp_d.get('result')

    def check_keys(self, addr):
        for i in self.receivers:
            key = self.get_pri_key(addr)
            bigstr = i + " pk: " + key
            print(bigstr)
            logging.info(bigstr)


if __name__ == "__main__":
    pw = 'password123'
    addrs = 'TTSETeCA3FWPueNuqEcKUNoxsuKZArhTA7Q2ecZ'
    c = AccountKeys()
    c.get_pri_key(addrs, pw)

   # buyer = 'TTbKRT4vrHMQdyQCATrdu6godeo1FJWSFVVk'
