#!/usr/bin/python3.7

import json
from src.libs.master_setup import master_setup, unpack_d, unpack_etc
from src.libs.setup_top import get_top, setup_logging
from src.libs.send_req import SendRequest


class SimpleRequests(object):

    def __init__(self, machine=0, chainid=0, urltype='url3'):
        settings_main_dd, sender_etc_dd, self.receivers = master_setup(machine, chainid, urltype)
        self.cid, self.url = unpack_d(settings_main_dd)
        self.sender, self.pw = unpack_etc(sender_etc_dd)
        self.remark = "get list of accounts"
        self.assetid = 1
        self.id = 999

    def doit(self, method_nm, p_list, method_type='POST'):  
        request = get_top(method_nm, p_list, self.url, method_type)  # 0 = get, 1=post
        response_d = SendRequest.send_request(request)

        print("-----------------------new query-----------\n" + "url:  " + self.url)
        print("method_nm: " + str(method_nm) + " method_type: " + str(method_type))
        print("query: " + str(request))
        print(json.dumps(request.json, indent=2))
        print("--------query: ", method_nm + " response: " + json.dumps(response_d) + " ------>\n\n")
        return response_d

    def get_the_best_block(self, meth_type='POST'):
        method_nm = "getBestBlockHeader"
        self.doit(method_nm, [self.cid], meth_type)

    def get_chain_info(self, meth_type='POST'):   # now works best with 8004
        method_nm = "getInfo"  # getChainInfo   # info works on westteam on 8004  'info'
        # method_nm = "getChainInfo"  # getChainInfo   # info works on westteam on 8004
            # method_nm = "getInfo"  # getChainInfo   # info works on westteam on 8004
        self.doit(method_nm, [self.cid], meth_type)   # four=1 for 8004 or 18004

    def get_account(self, acct, meth_type='POST'):
        method_nm = "getAccount"
        print("chainid:  ", self.cid)
        p = [self.cid, acct]
        self.doit(method_nm, p, meth_type)

    def get_account_ledger_list(self, acct, meth_type='POST'):
        method_nm = "getAccountLedgerList"
        p = [self.cid, acct]
        self.doit(method_nm, p, meth_type)

    def get_account_contract_list(self, aclistt, meth_type='POST'):
        method_nm = "getContractListById"
        # params:  {"pageNumber": 1, "pageSize": 10, "totalCount": 9,
        p = [self.cid, 1, 10, 99, [aclistt]]
        self.doit(method_nm, p, meth_type)

    def get_block_by_hash(self, tx_hash='x', meth_type='POST'):
        method_nm = "getBlockByHash"
        p = [self.cid, tx_hash]
        self.doit(method_nm, p, meth_type)
        # 7875b8be73fa1e436b3f04a9b5ec913a7a306c0e8978c360b1778c8ee06a12ad
        # blockhash for block 262078

    def get_block_package_tx_count(self, meth_type='POST'):
        method_nm = "getBlockTxCount"
        p = [self.cid, 900000, 900001]
        self.doit(method_nm, p, meth_type)

    def get_block_by_height(self, height='900000', meth_type='POST'):
        method_nm = "getBlockByHeight"
        p = [self.cid, height]
        self.doit(method_nm, p, meth_type)

    def get_tx(self, tx_hash, meth_type='POST'):
        method_nm = "getTx"
        p = [self.cid, tx_hash]
        self.doit(method_nm, p, meth_type)

    def get_tx_two(self, tx_hash=None, meth_type='POST'):
        if not tx_hash:
            tx_hash = 'b1e340841f8b5f7d1e2cf20ce6edb6d6f0122bfe299f00c975616d8459ab5ba0'
        method_nm = "getTx"
        p = [self.cid, tx_hash]
        self.doit(method_nm, p, meth_type)
        # 2fc7919bf68919bac6e1a2b02d179dcbd2e8ca3d72a2e214b16312e83d86449b
        # blockhash for block 262078

    def get_block_header_list(self, meth_type='POST'):
        method_nm = "getBlockHeaderList"
        #  [chainId,pageNumber,pageSize, isHidden, packedAddress],
        p = [1, 0, 100, False, 'NULSd6Hgeiej8U4JUtWrLTx9nNKFoyfSC3LdS']
        self.doit(method_nm, p, meth_type)


    def get_account_txs(self, address='addresshere', meth_type='POST'):
        method_nm = "getAccountTxs"
        #"params": [chainId, pageNumber, pageSize, address, txType, startHeight, endHeight],
        # params above are incomplete - it wants 9 items
        starth = 409112
        endh = 3041625
        pi = 1         # page index
        pss = 10       # item count displayed in each page 1-1000
        ttype = 0           # type=0 is all transactions  16=call contract
        p = [1, 0, 100, address, 16, starth, endh, 1, 1]   #this works!!!   # [chainId,pageNumber,pageSize,address,txType,isHidden]
        self.doit(method_nm, p, meth_type)
                # nine items worked sort of [1, 0, 10, address, 0, starth, endh, 1, 1]

if __name__ == "__main__":
    s = SimpleRequests(3, 2, 'url3')   # machine, chainid  west:  4, 4810
    # s.SimpleRequests(2, 'POST')   # 4 = POST
    # note in ver 2.5 everything is POST, never get, most are 8003, some 8004

    s.get_account('SPEXdKRT4pz7ZhasM9pTK4fvGrJf8eod5ZqtXa', 'POST',)
    s.get_account_txs('SPEXdKRT4kGmFz68ChyJrcjzFfggb8b1aNyaKh', 'POST',)
    #s.getBlockHeaderList()
    s.get_block_by_height(900000)
    s.get_the_best_block('POST')
    s.get_chain_info('POST')  # post-4 or get-3
