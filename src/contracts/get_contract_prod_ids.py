#!/usr/bin/python3.7

from src.libs.master_setup import master_setup, unpack_d
from src.libs.setup_top import prepare_top_section
from src.libs.send_req import SendRequest


class GetContractProdIds(object):

    def __init__(self):
        machine = 1     #   machine = 1   # 1 for west, 0 for kathy

        settings_d, sender_etc_dd, self.receivers = master_setup(machine)
        self.chain, self.url3, self.sender, self.pw = unpack_d(settings_d, sender_etc_dd)
        self.url4 = settings_d.get('url4')
        self.asset = 1
        self.id = 99999

    def get_contract_prod_ids(self, contract):
        return_type = "() return String"

        method_nm = "invokeView"
        contract_methodname = "getAllProductIds"
        args = []
        p_list = [self.chain, contract, contract_methodname, return_type, args]
        request = prepare_top_section(method_nm, p_list, self.url3)
        resp1 = SendRequest.send_request(request)
        # results_d, rstr = resp1.get("result")
        print(resp1)
        return resp1


if __name__ == "__main__":
    prods_obj = GetContractProdIds()
    # old july: contract_id = "SPEXdKRT4yJrChYu5KfusRJrLMpJ8qRmitSHxe"
    contract_id = "SPEXdKRT4zmkrCMcwQKfWEQfmCCKSboHp4TCdC"  #new aug10
    ## contract_id = "SPEXdKRT4zmkrCMcwQKfWEQfmCCKSboHp4TCdC"  #new aug10
    g = prods_obj.get_contract_prod_ids(contract_id)
    print(g)

# #      async getAllProductIds() {
#           let RET_TYPE = "() return String";
#           let METHOD_D = "invokeView";
#           let REQUEST_TYPE = "getAllProductIds"
#           let LASTLIST = [];
#
#           let ID_D = 900033;
#           let PARAMS = [CHAINID_w, CONT_ADDY_w, REQUEST_TYPE, RET_TYPE, LASTLIST];

#valueofasset, gaslimit, gas=25