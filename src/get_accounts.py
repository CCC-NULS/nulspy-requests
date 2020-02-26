#!/usr/bin/python3.7


from src.libs.master_setup import master_setup, unpack_d
from src.libs.setup_top import get_top
from src.libs.send_req import SendRequest


class GetAccounts(object):

    def __init__(self):
        machine = 0     #   machine = 1   # 1 for west, 0 for kathy

        settings_d, sender_etc_dd, self.receivers = master_setup(machine)
        self.chain, self.url3, self.sender, self.pw = unpack_d(settings_d, sender_etc_dd)
        self.url4 = settings_d.get('url4')
        self.remark = "transfer to account"
        self.asset = 1
        self.id = 99999

    def getaccounts(self):
        method_nm = "getAccountList"
        length = 87
        p_list = [self.chain, self.asset, length]
        request = get_top(method_nm, p_list, self.url3)
        resp1 = SendRequest.send_request(request)
        results_d = resp1.get("result")


if __name__ == "__main__":
    c = GetAccounts()
    c.getaccounts()
