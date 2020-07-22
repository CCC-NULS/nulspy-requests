#!/usr/bin/python3.7

# curl -s -X POST -H -v 'Content-Type: application/json' --data '{"jsonrpc":"2.0","method":"get_chain_info","params":[], "id":1234}' http://78.47.206.255:18003

# data:{"jsonrpc":"2.0","method":"invokeView","params":[24442,
# "TTSETeCA3FueL9cKCiDR8vAiRiGVtVCJksEsstM","getRe iews","(String productId) return Ljava/util/List;",["baseballcap"]],"id":904}

# params is first list
# 2nd list is items_list or last_list


from src.libs.master_setup import master_setup, unpack_d
from src.libs.setup_top import get_top
from src.libs.send_req import SendRequest
import json

class CheckContract(object):

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
        the_answer = SendRequest.send_request(request)

        print("stat: ", the_answer)
        print("  ANSWER to query ", method_nm, " is: ")
#        print(" ---------> The response is: " + the_answer.text + " ---------> \n\n")
        return the_answer

    def req_get_all_prod_ids(self, contract):   # uses invoke_view
        method_nm = "invokeView"
        method_inner = "getAllProductIds"  # goes in params list
        return_str = "() return String"
        params_list = [self.chain, contract, method_inner, return_str, self.emp_list]  # 4 items
        self.doit(method_nm, params_list)

    def req_get_reviews(self, contract):  # "invokeView"
        method_nm = "invokeView"
        method_inner = "getReviews"
        return_val_str = "(String productId) return Ljava/util/List;"
        product_list = ["req_get_all_prod_ids"]  # 4 items
        params_list = [self.chain, contract, method_inner,
                       return_val_str, product_list]  # 4
        rlist = self.doit(method_nm, params_list)
        return rlist

    def view_reviews(self, contract):  # "invokeView"
        method_nm = "invokeView"
        method_inner = "getReviews"
        return_val_str = "(String productId) return Ljava/util/List;"
        params_list = [self.chain, contract, method_inner, return_val_str, ["golfball"]]  # 4
        rlist = self.doit(method_nm, params_list)
        return rlist

    def req_get_contract(self, addr):
        method_nm = "getContract"
        params_list = [self.chain, addr]  # 4 items
        self.doit(method_nm, params_list)

    def req_get_writer(self, contract):
        method_nm = "getWriter"
        params_list = [self.chain, contract]  # 4 items
        self.doit(method_nm, params_list)

    def get_account_ledger_list(self, contract):
        method_nm = "getAccountLedgerList"
        p = [self.chain, contract]
        self.doit(method_nm, p)


if __name__ == "__main__":
    c = CheckContract()
    contract
    address: SPEXdKRT4yJrChYu5KfusRJrLMpJ8qRmitSHxe

    ctr = 'TTbKRT5DVddw7rDN1UrS9Wo3xGLFszwYwMLR'
    r = c.view_reviews(ctr)
    json_formatted_str = json.dumps(r, indent=2)
    print(json_formatted_str)




