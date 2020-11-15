#!/usr/bin/python3.7

import json
from src.libs.master_setup import master_setup, unpack_d
from src.libs.setup_top import get_top
from src.libs.send_req import SendRequest


class SimpleRequests(object):

    def __init__(self):
        machine = 3     #   machine = 1   # 1 for west  4=real nuls

        settings_d, sender_etc_dd, self.receivers = master_setup(machine)
        self.chain, self.url3, self.sender, self.pw = unpack_d(settings_d, sender_etc_dd)
        self.url4 = settings_d.get('url4')
        self.remark = "transfer to account"
        # self.asset = 1
        self.id = 99999
        
        self.emp_list = []

    def doit(self, method_nm, p_list, method_type=4):   #use url for url4
        url = self.url4
        if method_type == 3:
            url = self.url3
        request = get_top(method_nm, p_list, url, method_type)  # 0 = get, 1=post
        print("method_nm: " + str(method_nm) + "url: " + str(url))
        print("query: " + str(request))
        json_formatted_str = json.dumps(request.json, indent=2)
        print(json_formatted_str)
        response_d = SendRequest.send_request(request)
        print("  ANSWER to query ", method_nm, " is: ")
        print(url)
        print(" ---------> The response is: " + json.dumps(response_d) + " ---------> \n\n")
        return response_d

    def get_the_best_block(self):
        self.chain = 2
        meth_type = 4  # 4 = POST
        method_nm = "getBestBlockHeader"
        p = [self.chain]
        self.doit(method_nm, p, meth_type)

    def get_chain_info(self):   # now works best with 8004
        #method_nm = "info"  # getChainInfo   # info works on westteam on 8004
        method_nm = "getChainInfo"  # getChainInfo   # info works on westteam on 8004
        meth_type = 4  # 4 = POST
        self.chain = 2
        p = [self.chain]
        self.doit(method_nm, p, meth_type)   # four=1 for 8004 or 18004

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

    def get_BlockByHash(self, tx_hash=0):
        if not tx_hash:
            tx_hash = 'x'
        method_nm = "getBlockByHash"
        p = [self.chain, tx_hash]
        self.doit(method_nm, p)
        # 7875b8be73fa1e436b3f04a9b5ec913a7a306c0e8978c360b1778c8ee06a12ad
        # blockhash for block 262078

    def getBlockPackageTxCount(self):
        method_nm = "getBlockTxCount"
        p = [self.chain, 900000, 900001]
        self.doit(method_nm, p)

    def getBlockByHeight(self, height=0):
        if not height:
            height = '900000'
        method_nm = "getBlockByHeight"
        p = [self.chain, height]
        self.doit(method_nm, p)

    def getTx(self, tx_hash=0):
        if not tx_hash:
            tx_hash = '2fc7919bf68919bac6e1a2b02d179dcbd2e8ca3d72a2e214b16312e83d86449b'
        method_nm = "getTx"
        p = [self.chain, tx_hash]
        self.doit(method_nm, p)
        # 2fc7919bf68919bac6e1a2b02d179dcbd2e8ca3d72a2e214b16312e83d86449b
        # blockhash for block 262078

    def getBlockHeaderList(self):
        method_nm = "getBlockHeaderList"
        #  [chainId,pageNumber,pageSize, isHidden, packedAddress],
        p = [1, 0, 100, False, 'NULSd6Hgeiej8U4JUtWrLTx9nNKFoyfSC3LdS']
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
        self.doit(method_nm, p, 4)
                # nine items worked sort of [1, 0, 10, address, 0, starth, endh, 1, 1]

if __name__ == "__main__":
    s = SimpleRequests()
    # s.get_account('xyz')
    #s.get_AccountTxs()
    # s.get_cmds()
    # s.getBlockPackageTxCount()
    # s.getBlockByHeight(900000)
    #s.getTx()
    # s.getBlockHeaderList()
    s.get_the_best_block()

    s.get_chain_info()

#d07fc0d0f5e840b4fa8c924b4361faa0bc4c030e47a0402460c87eb2be97ee03


# ://public1.nuls.io' : 'http://beta.public1.nuls.io/',
# POCM test environment：[http://beta.pocm.nuls.io/](http://beta.pocm.nuls.io/)
#
#

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