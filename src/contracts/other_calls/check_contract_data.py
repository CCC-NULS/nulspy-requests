#!/usr/bin/python3.7

# params is first list
# 2nd list is items_list or last_list


from src.libs.master_setup import master_setup, unpack_d, unpack_etc
from src.libs.setup_top import get_top
from src.libs.send_req import SendRequest
import json


class CheckContract:

    def __init__(self, machine=1, chainid=0, urltype='url3'):
        settings_main_dd, sender_etc_dd, self.receivers = master_setup(machine, chainid, urltype)
        self.cid, self.url = unpack_d(settings_main_dd)
        self.sender, self.pw = unpack_etc(sender_etc_dd)
        self.remark = "transfer to account"
        self.asset = 1
        self.id = 99999
        self.emp_list = []

    # def doit(self, method_nm, p_list, four=0):   #use url for url4
    def doit(self, method_nm, p_list, method_type='POST'):  # use url for url4

        request = get_top(method_nm, p_list, self.url, method_type)  # 0 = get, 1=post
        the_answer = SendRequest.send_request(request)
        print("stat: ", the_answer)
        print("  ANSWER to query ", method_nm, " is: ")
        #  print(" ---------> The response is: " + the_answer.text + " ---------> \n\n")
        return the_answer

    def req_get_all_prod_ids(self, contract):   # uses invoke_view
        method_nm = "invokeView"
        method_inner = "getAllProductIds"  # goes in params list
        return_str = "() return String"
        params_list = [self.cid, contract, method_inner, return_str, self.emp_list]  # 4 items
        self.doit(method_nm, params_list)

    def req_get_reviews(self, contract):  # "invokeView"
        method_nm = "invokeView"
        method_inner = "getReviews"
        return_val_str = "(String productId) return Ljava/util/List;"
        product_list = ["req_get_all_prod_ids"]  # 4 items
        params_list = [self.cid, contract, method_inner,
                       return_val_str, product_list]  # 4
        rlist = self.doit(method_nm, params_list)
        return rlist

    def view_reviews(self, contract):  # "invokeView"
        method_nm = "invokeView"
        method_inner = "getReviews"
        return_val_str = "(String productId) return Ljava/util/List;"
        params_list = [self.cid, contract, method_inner, return_val_str, ["golfball"]]  # 4
        rlist = self.doit(method_nm, params_list)
        return rlist

    def req_get_contract(self, addr):
        method_nm = "getContract"
        params_list = [self.cid, addr]  # 4 items
        self.doit(method_nm, params_list)

    def req_get_writer(self, contract):
        method_nm = "getWriter"
        params_list = [self.cid, contract]  # 4 items
        self.doit(method_nm, params_list)

    def get_account_ledger_list(self, contract):
        method_nm = "getAccountLedgerList"
        p = [self.cid, contract]
        self.doit(method_nm, p)


if __name__ == "__main__":
    ctr = 'SPEXdKRT4zmkrCMcwQKfWEQfmCCKSboHp4TCdC'
    c = CheckContract()
    r = c.req_get_all_prod_ids(ctr)
    r = c.req_get_contract(ctr)
    json_formatted_str = json.dumps(r, indent=2)
    print(json_formatted_str)




