#!/usr/bin/python3.7

from src.libs.master_setup import master_setup, unpack_d
from src.libs.setup_top import get_top
from src.libs.send_req import SendRequest


class CallContract(object):

    def __init__(self):
        machine = 1     #   machine = 1   # 1 for west, 0 for kathy

        settings_d, sender_etc_dd, self.receivers = master_setup(machine)
        self.chain, self.url3, self.sender, self.pw = unpack_d(settings_d, sender_etc_dd)
        self.url4 = settings_d.get('url4')
        self.asset = 1
        self.id = 99999

        self.contract = sender_etc_dd.get('contract')
        self.contract_desc = "(String productId, String reviewComments) return LReviewContract$Review;"

    def call_contract(self, val, args):
        multiplier = (10**8)
        value_asset = val * multiplier
        gas_limit = 9900000
        gas_price = 25                            # anything 25 or over will work
        remark = "call contract"

        method_nm = "contractCall"
        contract_methodname = "writeReview"
        p_list = [self.chain, self.sender, self.pw, value_asset, gas_limit, gas_price,
                  self.contract, contract_methodname, self.contract_desc, args, remark]
        request = get_top(method_nm, p_list, self.url4)
        resp1 = SendRequest.send_request(request)
        results_d, rstr = resp1.get("result")
        print(rstr)
        return rstr


if __name__ == "__main__":
    c = CallContract()
    my_review = ["swimsuits", "too large"]
    value_of_asset = 25     # cost to review
    g = c.call_contract(value_of_asset, my_review)
    print(g)



#valueofasset, gaslimit, gas=25