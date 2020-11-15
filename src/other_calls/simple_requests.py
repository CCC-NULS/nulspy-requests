#!/usr/bin/python3.7

import json
from src.libs.master_setup import master_setup, unpack_d, unpack_etc
from src.libs.setup_top import get_top
from src.libs.send_req import SendRequest


class SimpleRequests(object):

    def __init__(self, machine=0, chainid=0):
        settings_main_dd, sender_etc_dd, self.receivers = master_setup(machine, chainid)
        self.cid, self.url3, self.url4 = unpack_d(settings_main_dd)
        self.sender, self.pw = unpack_etc(sender_etc_dd)
        self.remark = "get list of accounts"
        self.assetid = 1
        self.id = 999

    def doit(self, method_nm, p_list, method_type=4, urltype="url3"):   #use url for url4
        url = self.url4
        if urltype == "url3":
            print("url type: 8003")
            url = self.url3
        else:
            print("url type: 8004")

        print("url is: ", url)

        request = get_top(method_nm, p_list, url, method_type)  # 0 = get, 1=post
        print("method_nm: " + str(method_nm) + "  method_type: " + str(method_type))
        print("query: " + str(request))
        json_formatted_str = json.dumps(request.json, indent=2)
        print(json_formatted_str)
        response_d = SendRequest.send_request(request)
        print("  ANSWER to query ", method_nm, " is: ")
        print(urltype)
        print(" ---------> The response is: " + json.dumps(response_d) + " ---------> \n\n")
        return response_d

    def get_the_best_block(self, meth_type=4, urltype='url3'):
        method_nm = "getBestBlockHeader"
        p = [self.cid]
        self.doit(method_nm, p, meth_type, urltype)

    def get_chain_info(self, meth_type=4, urltype='url3'):   # now works best with 8004
        method_nm = "getInfo"  # getChainInfo   # info works on westteam on 8004  'info'
        if meth_type == 3:
            method_nm = "getChainInfo"  # getChainInfo   # info works on westteam on 8004
            # method_nm = "getInfo"  # getChainInfo   # info works on westteam on 8004
        p = [self.cid]
        self.doit(method_nm, p, meth_type, urltype)   # four=1 for 8004 or 18004

    def get_account(self, acct, meth_type=4, urltype='url3'):
        meth_type = 4  # 4 = POST   3=GET
        method_nm = "getAccount"
        print("chainid:  ", self.cid)
        p = [self.cid, acct]
        self.doit(method_nm, p, meth_type, urltype)

    #def get_accountList(self):
        # see program file with this name


    def get_accountLedgerList(self, acct, meth_type=4, urltype='url3'):
        method_nm = "getAccountLedgerList"
        p = [self.cid, acct]
        self.doit(method_nm, p, meth_type, urltype)

    def get_accountContractList(self, aclistt, meth_type=4, urltype='url3'):
        method_nm = "getContractListById"
        # params:  {"pageNumber": 1, "pageSize": 10, "totalCount": 9,
        p = [self.cid, 1, 10, 99, aclistt]
        self.doit(method_nm, p, meth_type, urltype)

    def get_tx(self, tx_hash, meth_type=4, urltype='url3'):
        method_nm = "getTx"
        p = [self.cid, tx_hash]
        self.doit(method_nm, p, meth_type, urltype)

    def get_BlockByHash(self, tx_hash=0, urltype='url3'):
        if not tx_hash:
            tx_hash = 'x'
        method_nm = "getBlockByHash"
        p = [self.cid, tx_hash]
        self.doit(method_nm, p, urltype)
        # 7875b8be73fa1e436b3f04a9b5ec913a7a306c0e8978c360b1778c8ee06a12ad
        # blockhash for block 262078

    def getBlockPackageTxCount(self, urltype='url3'):
        method_nm = "getBlockTxCount"
        p = [self.cid, 900000, 900001]
        self.doit(method_nm, p, urltype)

    def getBlockByHeight(self, height=0, urltype='url3'):
        if not height:
            height = '900000'
        method_nm = "getBlockByHeight"
        p = [self.cid, height]
        self.doit(method_nm, p, urltype)

    def getTx(self, tx_hash=0, urltype='url3'):
        if not tx_hash:
            tx_hash = '2fc7919bf68919bac6e1a2b02d179dcbd2e8ca3d72a2e214b16312e83d86449b'
        method_nm = "getTx"
        p = [self.cid, tx_hash]
        self.doit(method_nm, p, urltype)
        # 2fc7919bf68919bac6e1a2b02d179dcbd2e8ca3d72a2e214b16312e83d86449b
        # blockhash for block 262078

    def getBlockHeaderList(self, urltype='url3'):
        method_nm = "getBlockHeaderList"
        #  [chainId,pageNumber,pageSize, isHidden, packedAddress],
        p = [1, 0, 100, False, 'NULSd6Hgeiej8U4JUtWrLTx9nNKFoyfSC3LdS']
        self.doit(method_nm, p, urltype)


    def get_AccountTxs(self, urltype='url3'):
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
        self.doit(method_nm, p, 4, urltype)
                # nine items worked sort of [1, 0, 10, address, 0, starth, endh, 1, 1]

if __name__ == "__main__":
    s = SimpleRequests(4, 4810)   # machine, chainid  west:  4, 4810
    s.get_account('SPEXdKRT4kGmFz68ChyJrcjzFfggb8b1aNyaKh', 'url3')
    #s.get_AccountTxs('SPEXdKRT4kGmFz68ChyJrcjzFfggb8b1aNyaKh')
    # s.get_cmds()
    # s.getBlockPackageTxCount()
    # s.getBlockByHeight(900000)
    #s.getTx()
    s.get_the_best_block(4, 'url3')
    s.get_accountLedgerList('SPEXdKRT4kGmFz68ChyJrcjzFfggb8b1aNyaKh')

    s.get_chain_info(4, 'url3')  # post-4 or get-3
    s.get_accountContractList(4, 'url4')  # post-4 or get-3

#":"getAccountTxs","params":[4810,1,5,"SPEXdKRT4qzoF5iR4ZPJMJUrh3tqihUZy7pS4q",0,-1,-1],"id":932}
#
#2020-11-15 03:24:29,768 DEBUG [grizzly-http-server-1] - io.nuls.controller.ApiCallController.apiPost(ApiCallController.java:49):do POST , path : ,data:{"jsonrpc":"2.0","method":"getAccount","params":[4810,"SPEXdKRT4qzoF5iR4ZPJMJUrh3tqihUZy7pS4q"],"id":405}


# real accts:
# 'SPEXdKRT4kGmFz68ChyJrcjzFfggb8b1aNyaKh',   *
# 'SPEXdKRT4wqaQkYBM8bFm9PyyTumB6GgXSQ57G',  *
# 'SPEXdKRT4ja5aFgREi6HhnxcGPyVi8yfpDvSys',   *

# 'SPEXdKRT4yvkvyWr4iGamMDKGzhiGgkjDYtZfR',
# 'SPEXdKRT54LQChhXy491qdJ1vXXAjjXNUSY2km',

# 'SPEXdKRT51rgzKMchGYbNQ5pkDGuFjy7xaxJEZ',
# 'SPEXdKRT4sX9XTHvyP5qBKsZGihgUVdNVmWihL',
# 'SPEXdKRT5ANiZNnLuRuFSKsqY4nX4twQ88vhb5',
# 'SPEXdKRT4vwmpHZiufc7SWSW69AFw6x39uJZZE',

# 'SPEXdKRT5AavVv9Czg7XbRgo8EaVe5aX5ypoTJ',









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