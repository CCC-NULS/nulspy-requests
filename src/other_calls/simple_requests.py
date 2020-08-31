#!/usr/bin/python3.7

import json
from src.libs.master_setup import master_setup, unpack_d
from src.libs.setup_top import get_top
from src.libs.send_req import SendRequest


class SimpleRequests(object):

    def __init__(self):
        machine = 4     #   machine = 1   # 1 for west

        settings_d, sender_etc_dd, self.receivers = master_setup(machine)
        self.chain, self.url3, self.sender, self.pw = unpack_d(settings_d, sender_etc_dd)
        self.url4 = settings_d.get('url4')
        self.remark = "transfer to account"
        self.asset = 1
        self.id = 99999
        
        self.emp_list = []

    def doit(self, method_nm, p_list, four=1):   #use url for url4
        if four:
            url = self.url4
        else:
            url = self.url3
        request = get_top(method_nm, p_list, url)
        response_d = SendRequest.send_request(request)
        print("query: " + str(request))
        print("  ANSWER to query ", method_nm, " is: ")
        print(url)
        print(" ---------> The response is: " + json.dumps(response_d) + " ---------> \n\n")
        return response_d

    def get_the_best_block(self):
        method_nm = "getBestBlockHeader"
        p = [self.chain]
        self.doit(method_nm, p)

    def get_chain_info(self):
        method_nm = "get_info"  # getChainInfo
        self.chain = 1
        p = []
        self.doit(method_nm, p, four=1)

    def get_account(self, acct):
        method_nm = "getAccount"
        p = [self.chain, acct]
        self.doit(method_nm, p)

    def get_accountLedgerList(self, acct):
        method_nm = "getAccount"
        p = [self.chain, acct]
        self.doit(method_nm, p)

    def get_accountContractList(self, aclistt):
        method_nm = "getContractListById"
        # params:  {"pageNumber": 1, "pageSize": 10, "totalCount": 9,
        p = [self.chain, 1, 10, 99, aclistt]
        return self.doit(method_nm, p)

    def get_tx(self, tx_hash):
        method_nm = "getTx"
        p = [self.chain, tx_hash]
        self.doit(method_nm, p)

    def get_AccountTxs(self):
        method_nm = "getAccountTxs"
        #"params": [chainId, pageNumber, pageSize, address, txType, startHeight, endHeight],
        #    "params":[chainId,pageNumber,pageSize,address,txType,startHeight, endHeight],
        # params above are incomplete - it wants 9 items
        address = 'addresshere'
        starth = 409112
        endh = 3041625
        pi = 1         # page index
        pss = 10       # item count displayed in each page 1-1000
        ttype = 0           # type=0 is all transactions  16=call contract
        p = [1, 0, 100, address, 16, starth, endh, 1, 1]   #this works!!!   # [chainId,pageNumber,pageSize,address,txType,isHidden]
        self.doit(method_nm, p, four=1)
                # nine items worked sort of [1, 0, 10, address, 0, starth, endh, 1, 1]

if __name__ == "__main__":
    s = SimpleRequests()
    # s.get_account('xyz')
    s.get_AccountTxs()
    # s.get_cmds()

# get this block block 154731

    # aclist = ['SPEXdKRT4u1Y38BVnjxCcnY33E5y3e3rfnwNv3']
    #
    # res = s.get_accountContractList(aclist)[0].get('result').get('list')
    # print("contractAdddress                        creater                                 alias  balance of contract")
    # for i in res:
    #     mystr = i.get('contractAddress') + ", " + i.get('creater') + ", " + i.get('alias') + ", " + str(i.get('balance'))
    #     print(mystr)

    # aclist = ['SPEXdKRT4iLwhSaXEhLDR4YNL9WkKsPRjKWb4z',
    #             'SPEXdKRT4pz7ZhasM9pTK4fvGrJf8eod5ZqtXa',
    #             'SPEXdKRT4u1Y38BVnjxCcnY33E5y3e3rfnwNv3',
    #             'spexdKRT4yQDZXwNJJQn3HbAGBR4p8QMKvZBVC']

# {
# # 	"jsonrpc": "2.0",
# # 	"method": "getAccountTxs",
# # 	"params": [
# # 		1,    #chainid
# # 		0,    # start page
# # 		10,   # how many per page
# # 		"NULSd6account..............",  #account addy
# # 		0,        # unknown
# # 		409112,   # starting block height
# # 		3041625,  # ending block height
# # 		1,        # maybe asset id
# # 		1         # another id
# # 	],
# # 	"id": 900001    # the made up id we send
# # # }