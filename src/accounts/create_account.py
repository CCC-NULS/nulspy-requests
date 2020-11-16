#!/usr/bin/python3.7


import logging
from src.libs.master_setup import master_setup, unpack_d
from src.libs.setup_top import get_top
from src.libs.send_req import SendRequest
from src.accounts.account_keys import AccountKeys


class CreateAccount(object):

    def __init__(self):
        machine = 0     #   machine = 1   # 1 for west, 0 for kathy

        settings_d, sender_etc_dd, self.receivers = master_setup(machine)
        self.chain, self.url3, self.sender, self.pw = unpack_d(settings_d, sender_etc_dd)
        self.url4 = settings_d.get('url4')
        self.remark = "transfer to account"
        self.asset = 1
        self.id = 99999

        self.aks_obj = AccountKeys()

    def create_account(self):
        rg = 1
        for i in range(rg):
            method_nm = "createAccount"
            p_list = [self.chain, 1, self.pw]
            request = get_top(method_nm, p_list, self.url4)
            response, rstr  = SendRequest.send_request(request)
            results_d = response.get("result")

            addr = results_d[0]
            pri_key = self.aks_obj.get_pri_key(addr, self.pw)
            response2 = self.aks_obj.import_pri_key(pri_key)
            bigstr = "\n---created this account: " + addr + "  prikey: " + pri_key + "  pw: " + self.pw
            print("-----" + bigstr)
            logging.info(bigstr)

        print(rstr)
        # return response2



# "method":"importPriKey",
# "params":[chain, priKey, password],
# "method":"getPriKey",
# "params":[chain, address, password],

if __name__ == "__main__":
    c = CreateAccount()
    c.create_account()
    # c.check_keys()
    # print(k + " : " + g + " pw: ")
    # c.get_pri_key("TTbKRT4vrHMQdyQCATrdu6godeo1FJWSFVVk")
#  47e9ea04abfcf9e92f91db11726a73a8864b6c1cdd98642c9acf8883855712af
