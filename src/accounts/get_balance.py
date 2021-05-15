#!/usr/bin/python3.7

import json
from src.libs.master_setup import master_setup, unpack_d
from src.old_code.old_setup_top import prepare_top_section
from src.old_code.old_send_req import SendRequest


class GetBalance(object):

    def __init__(self, machine=4, chainid=2):  # tchain_id=chainId
        settings_d, sender_etc_dd, self.receivers = master_setup(machine, chainid)
        self.unused, self.url3, self.sender, self.pw = unpack_d(settings_d, sender_etc_dd)
        self.url4 = settings_d.get('url4')
        self.remark = "request"
        self.chain, self.url3, self.sender, self.pw = unpack_d(settings_d, sender_etc_dd)
        self.remark = "get balance"
        self.asset = 1
        self.id = 99999

    def get_account_balance(self):
        method_nm = "getAccountBalance"  # getAccountBalance

        # @ Parameter(parameterName="chainId", requestType= @ TypeDescriptor(value=int. class ), parameterDes = "链ID"),
        # @ Parameter(parameterName = "assetChainId", requestType = @ TypeDescriptor(value = int.class ), parameterDes = "资产的链ID"),
        # @ Parameter(parameterName = "assetId", requestType = @ TypeDescriptor(value = int.class ), parameterDes = "资产ID"),
        # @ Parameter(parameterName = "address", requestType = @ TypeDescriptor(value = String.class ), parameterDes = "账户地址")


        for receiver in self.receivers:
            p_list = [self.chainid, self.assetChainId, self.assetId, receiver, "nmsTx"]

            #p_list = [self.chain, self.chain, self.asset, receiver]
            request = prepare_top_section(method_nm, p_list, self.url3)
            response = SendRequest.send_request(request)
            results_d, rstr = json.loads(response.text)

            total_balance = results_d.get("totalBalance")
            print("totalBalance: " + receiver + ":  " + str(total_balance))


if __name__ == "__main__":
    c = GetBalance(4, 4810)
    c.get_account_balance()
# machine = 4  # machine = 1   # 1 for west, 0 for kathy
