#!/usr/bin/python3.7

from src.libs.master_setup import master_setup, unpack_d
from src.libs.setup_top import get_top
from src.libs.send_req import SendRequest
import json
from io import StringIO


class GetContractProdReviews(object):

    def __init__(self):
        machine = 1     #   machine = 1   # 1 for west, 0 for kathy

        settings_d, sender_etc_dd, self.receivers = master_setup(machine)
        self.chain, self.url3, self.sender, self.pw = unpack_d(settings_d, sender_etc_dd)
        self.url4 = settings_d.get('url4')
        self.asset = 1
        self.id = 99999

    def get_contract_prod_reviews(self, contract):
        return_type = "() return String"

        method_nm = "invokeView"
        contract_methodname = "getAllProductIds"
        args = []
        p_list = [self.chain, contract, contract_methodname, return_type, args]
        request = get_top(method_nm, p_list, self.url3)
        resp1 = SendRequest.send_request(request)

        return_type = "(String productId) return Ljava/util/List;";
        request_type = "getReviews"

        thelist = resp1[0].get("result").get("result")
        res = json.loads(thelist)

        for item in res:
            args = [item]
            p_list = [self.chain, contract, request_type, return_type, args]
            request = get_top(method_nm, p_list, self.url3)
            ans1, ans2 = SendRequest.send_request(request)
            newstr = ans1.get("result").get("result")
            # print("old: ", newstr)
            listem = ["\r\n", '\n', '\\']
            for i in listem:
                newstr = newstr.replace(i, '')

            io = StringIO(newstr)
            newj = json.load(io)
            print(newj[0].get("productId"))

            for j in newj:
                print('-->', j.get("comments"))
            print()


            # print(ndict.get("productId"))
            # cstr = ndict[0].get("comments")
            # dstr = cstr.strip("\r").strip("\n").strip("\\s")
            # print(dstr)
            # print()
        return


if __name__ == "__main__":
    prods_obj = GetContractProdReviews()
    contract_id = "TTbKRT5DVddw7rDN1UrS9Wo3xGLFszwYwMLR"
    prods_obj.get_contract_prod_reviews(contract_id)
    # print(g)

# #      async getAllProductIds() {
#           let RET_TYPE = "() return String";
#           let METHOD_D = "invokeView";
#           let REQUEST_TYPE = "getAllProductIds"
#           let LASTLIST = [];
#
#           let ID_D = 900033;
#           let PARAMS = [CHAINID_w, CONT_ADDY_w, REQUEST_TYPE, RET_TYPE, LASTLIST];

#valueofasset, gaslimit, gas=25