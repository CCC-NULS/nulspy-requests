#!/usr/bin/python3.7

import json
from src.libs.master_setup import master_setup
from src.libs.setup_top import prepare_top_section
from src.libs.send_req import SendRequest


class SimpleRequests(object):

    def __init__(self, machine=4, chainid=1, urltype='url3'):
        settings_main_dd, sender_etc_dd, self.receivers = master_setup(machine, chainid, urltype)
        # machine is the server that is running the public blockchain api to query

        self.tchain_id = settings_main_dd.get('tchain_id')
        self.myurl = settings_main_dd.get('myurl')
        self.sender = sender_etc_dd.get('sender')
        self.pw = sender_etc_dd.get('pw')

        self.remark = "get list of accounts"
        self.assetid = 1
        self.id = 999

    def doit(self, method_name, parameter_list=[], method_type='POST'):
        request = prepare_top_section(method_name, parameter_list, self.myurl, method_type)  # 0 = get, 1=post
        print("running on this url:  " + self.myurl)

        response_tup = SendRequest.send_request(request)
        response_str = response_tup[1]  # str
        response_parsed = json.loads(response_str)
        print(json.dumps(response_parsed, indent=2, sort_keys=True))
                                                            # print("-----------------------new query-----------\n" + "myurl:  " + self.myurl) print("method_name: " + str(method_name) + " method_type: " + str(method_type)) print("query: " + str(request)) print(json.dumps(request.json, indent=2))
        print()                                                   # print("--------query: ", method_name + " response: " + json.dumps(response_d) + " ------>\n\n")
        return response_tup, []

    def get_the_best_block(self, meth_type='POST'):
        method_nm = "getBestBlockHeader"
        param_list = [self.tchain_id]
        self.doit(method_nm, param_list, meth_type)

    def get_account(self, acct, meth_type='POST'):
        method_nm = "getAccount"
        print("chainid:  ", self.tchain_id)
        param_list = [self.tchain_id, acct]
        self.doit(method_nm, param_list, meth_type)

    def get_account_ledger_list(self, acct, meth_type='POST'):
        method_nm = "getAccountLedgerList"
        param_list = [self.tchain_id, acct]
        self.doit(method_nm, param_list, meth_type)

    def get_account_contract_list(self, aclistt, meth_type='POST'):
        method_nm = "getContractListById"
        # params:  {"pageNumber": 1, "pageSize": 10, "totalCount": 9,
        param_list = [self.tchain_id, 1, 10, 99, [aclistt]]
        self.doit(method_nm, param_list, meth_type)

    def get_block_by_hash(self, tx_hash='x', meth_type='POST'):
        method_nm = "getBlockByHash"
        param_list = [self.tchain_id, tx_hash]
        self.doit(method_nm, param_list, meth_type)
        # 7875b8be73fa1e436b3f04a9b5ec913a7a306c0e8978c360b1778c8ee06a12ad
        # blockhash for block 262078

    def get_block_package_tx_count(self, meth_type='POST'):
        method_nm = "getBlockTxCount"
        param_list = [self.tchain_id, 900000, 900001]
        self.doit(method_nm, param_list, meth_type)

    def get_block_by_height(self, height='900000', meth_type='POST'):
        method_nm = "getBlockByHeight"
        param_list = [self.tchain_id, height]
        biglist, anotherlist = self.doit(method_nm, param_list, meth_type)
        return biglist, anotherlist

    def get_tx(self, tx_hash, meth_type='POST'):
        method_nm = "getTx"
        param_list = [self.tchain_id, tx_hash]
        self.doit(method_nm, param_list, meth_type)

    def get_tx_two(self, tx_hash=None, meth_type='POST'):
        if not tx_hash:
            tx_hash = 'b1e340841f8b5f7d1e2cf20ce6edb6d6f0122bfe299f00c975616d8459ab5ba0'
        method_nm = "getTx"
        param_list = [self.tchain_id, tx_hash]
        self.doit(method_nm, param_list, meth_type)
        # 2fc7919bf68919bac6e1a2b02d179dcbd2e8ca3d72a2e214b16312e83d86449b
        # blockhash for block 262078

    def get_block_header_list(self, meth_type='POST'):
        method_nm = "getBlockHeaderList"
        # [chainId,pageNumber,pageSize, isHidden, packedAddress],
        param_list = [self.tchain_id, 0, 100, False, 'NULSd6Hgeiej8U4JUtWrLTx9nNKFoyfSC3LdS']
        self.doit(method_nm, param_list, meth_type)

    def get_account_txs(self, address='addresshere', meth_type='POST'):
        method_nm = "getAccountTxs"
        # "params": [chainId, pageNumber, pageSize, address, txType, startHeight, endHeight],
        # params above are incomplete - it wants 9 items
        starth = 3737222
        endh = 3737239
        # pi = 1         # page index
        # pss = 10       # item count displayed in each page 1-1000
        # ttype = 0           # type=0 is all transactions  16=call contract
        param_list = [1, 0, 100, address, 16, starth, endh, 1, 1]   # this works!!!   # [chainId,pageNumber,pageSize,address,txType,isHidden]
        self.doit(method_nm, param_list, meth_type)
        # nine items worked sort of [1, 0, 10, address, 0, starth, endh, 1, 1]

    def get_chain_info_cs(self):
        method_nm = "cs_getChainInfo"  # getChainInfo
        param_list = [self.tchain_id]
        self.doit(method_nm, param_list, 'POST')   # four=1 for 8004 or 18004


    def get_chain_info_info(self, meth_type='POST'):  # now works best with 18004 docker wallet pro new code
        method_nm = "info"
        param_list = [self.tchain_id]
        self.doit(method_nm, param_list, meth_type)

    def get_chain_info_get(self, meth_type='POST'):  # now works best with 8004
        # method_nm = "getInfo"  # getChainInfo   # info works on westteam on 8004 'info', info works for new wallet-pro docker
        # method_nm = "getChainInfo"  # getChainInfo   # info works on westteam on 8004  'info'
        # method_nm = "getInfo"  # getChainInfo   # info works on westteam on 8004
        method_nm = "getChainInfo"  # getChainInfo   # info works on westteam on 8004 for SPEX only
        param_list = [self.tchain_id]
        self.doit(method_nm, param_list, meth_type)  # four=1 for 8004 or 18004

    def get_chain_cmd(self, method_nm="info", meth_type='POST'):  # now works best with 18004 docker wallet pro new code
        param_list = [self.tchain_id]
        self.doit(method_nm, param_list, meth_type)  # four=1 for 8004 or 18004

    def get_chain_cmd4(self, method_nm="info", meth_type='POST'):  # now works best with 18004 docker wallet pro new code
        param_list = [self.tchain_id]
        self.doit(method_nm, param_list, meth_type)  # four=1 for 8004 or 18004

    def get_getConsensusNodes(self, meth_type='POST'):
        method_nm = "getConsensusNodes"
        param_list = [self.tchain_id, 1, 99, 0]  # [chainId,pageNumber,pageSize,type],
        self.doit(method_nm, param_list, meth_type)  # [self.tchain_id], 'POST' are defaults

if __name__ == "__main__":
    # s = SimpleRequests(4, 4810, 'url4')   # machine, chainid  west:  4, 4810
    # note in ver 2.5 everything is POST, never get, most are 8003, some 8004

    #s = SimpleRequests(1, 1, 'url4')   # machine, chainid  west:  4, 4810
    # s.get_account('SPEXdKRT4pz7ZhasM9pTK4fvGrJf8eod5ZqtXa', 'POST',)
    # s.getBlockHeaderList()
    # s.get_block_by_height(900000)
    # s.get_the_best_block('GET')
    # s.get_tx(nerve_tx_felip60, 'POST')  # post- get-
    # s.get_chain_info('POST')  # post- get-
    # s.get_the_best_block()
    # s.get_chain_info_test()
    # s.get_coin_info()
    # s.get_block_by_height(900000)
    # s.getBlockHeaderList()
    # s.get_the_best_block('GET')

    # s.get_the_best_block()
    # s.get_consensus_node_ct()
    # s.get_block_by_height(900000)
    #s.get_chain_info_cs()

    # s.get_chain_cmd("getVersion")
    s1 = SimpleRequests(1, 1, 'url3')   # machine=1 public1, chainid=1  west:  3,       nuls:1, 1

    s3 = SimpleRequests(3, 1, 'url3')  # machine=1 public1, chainid=1  west:  3,       nuls:1, 1
#  (self, machine=4, chainid=1, urltype='url4'):
    #s4 = SimpleRequests(4, 1, 'url4')   # machine=4, chainid=1  west: 3,       nuls:1, 1
    #s1.get_chain_info_get()
    #s3.get_chain_info_get()

    #s1.get_chain_cmd(method_nm="consensusInfo")
    #s1.get_chain_cmd4(method_nm="getChainInfo")

    print()
    # s3.get_block_by_height(3900000)  ## works
    # s1.get_block_by_height(4000000)  # works
    #s1.get_the_best_block()
    s3.get_the_best_block()

    #
    # s4.get_chain_cmd("getBestBlockHeader")
    #s3.get_chain_cmd("getAllAddressPrefix")  # works
    #s3.get_getConsensusNodes()  # works

    # s.get_chain_cmd("cs_getRoundInfo")
    # s.get_chain_cmd("cs_getRoundInfo")
    # s.get_chain_info_cs()


    # parta = response_d[0]  # dict myresults = parta['result'] myresult_txlist = myresults['txList'] answerlist = [] donetxs = [] for txdict in myresult_txlist: if txdict['coinTos']: thehash =
    # txdict['hash'] theheight = txdict['height'] tremark = txdict['remark'] tvalue = txdict['value'] possible_nuls_addys = txdict['coinTos'] for addy in possible_nuls_addys: if thehash not in
    # donetxs: answerlist.append([theheight, addy['address'], thehash,  tvalue, tremark])
    #                 donetxs.append(thehash)


