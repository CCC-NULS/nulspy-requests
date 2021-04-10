#!/usr/bin/python3.7

import json
from src.libs.master_setup import master_setup
from src.libs.setup_top import prepare_top_section
from src.libs.send_req import SendRequest
import datetime

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
        self.special = 0


    def add_up(self, response_dict2):
        resp_list_of_d = response_dict2.get("result").get("list")
        # print("-----------------------new query-----------\n" + "myurl:  " + self.myurl) print("method_name: " + str(method_name) + " method_type: " + str(method_type)) print("query: " + str(
        # request)) print(json.dumps(request.json, indent=2))
        bigtot = 0
        for anode in resp_list_of_d:
            tot_dep = anode.get("totalDeposit")

            agent_alias = anode.get("agentAlias")
            if not agent_alias:
                agent_alias = "NoName Node"
            newstr = agent_alias + ":  totalDeposit"
            print(newstr, tot_dep)
            bigtot += tot_dep

        print()  # print("--------query: ", method_name + " response: " + json.dumps(response_d) + " ------>\n\n")
        bt = bigtot / 100000000
        print("total staked: ", bigtot)
        f"{bt:,}"
        print(f"{bt:,}")

    # def prepare_top_plain(method, param_list, the_url, method_type='POST'):  # no method
    def doit(self, method_name, parameter_list, method_type='POST'):
        # request = prepare_top_section(method_name, parameter_list, self.myurl, method_type)  # 0 = get, 1=post
        request = prepare_top_section(method_name, parameter_list, self.myurl, method_type=method_type)

        response_tup = SendRequest.send_request(request)
        result_part = response_tup[0].get('result')
        result_addy = result_part.get('address')
        consensus_amt = result_part.get('consensusLock')
        totbal = result_part.get('totalBalance')  #big int
        totbal_int = int(totbal/100000000)  # reg int
        # print(f"{totbalint:,}" + "   " + temp_list[1])

        print(result_addy + " consensuslock: " + str(consensus_amt) + " totalbalance: " + str(f"{totbal_int:,}"))
        return response_tup, []

    def get_the_best_block(self, meth_type='POST'):
        method_nm = "getBestBlockHeader"
        param_list = [self.tchain_id]
        self.doit(method_nm, param_list, meth_type)

    def get_account(self, acct, meth_type='POST'):
        method_nm = "getAccount"
        # print("chainid:  ", self.tchain_id)
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

    def get_account_txs(self, addy='addresshere', meth_type='POST', tx_type=0):
        method_nm = "getAccountTxs"
        # "params": [chainId, pageNumber, pageSize, address, txType, startHeight, endHeight],
        # params above are incomplete - it wants 9 items
        starth = 3737222
        endh = 3737239
        # pi = 1         # page index
        # pss = 10       # item count displayed in each page 1-1000
        # ttype = 0           # type=0 is all transactions  16=call contract
        param_list = [1, 0, 100, addy, 16, starth, endh, 2, 1]   # this works!!!   # [chainId,pageNumber,pageSize,address,txType,isHidden]
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
        self.doit(method_nm, param_list, method_type=meth_type)  # four=1 for 8004 or 18004

    def get_chain_cmd_public(self, meth_type='POST', method_nm="info"):  # now works best with 18004 docker wallet pro new code
        param_list = [self.tchain_id]
        self.doit(method_nm, param_list, meth_type)  # four=1 for 8004 or 18004

    def get_chain_cmd4(self, method_nm="info", meth_type='POST'):  # now works best with 18004 docker wallet pro new code
        param_list = [self.tchain_id]
        self.doit(method_nm, param_list, meth_type)  # four=1 for 8004 or 18004

    def get_getConsensusNodes(self, meth_type='POST'):
        self.special = 1
        method_nm = "getConsensusNodes"
        param_list = [self.tchain_id, 1, 99, 0]  # [chainId,pageNumber,pageSize,type],
        self.doit(method_nm, param_list, meth_type)  # [self.tchain_id], 'POST' are defaults

    def get_prikey(self, myacct, pw, meth_type='POST'):
        # [2, "tNULSeBaMhcccH1KeXhMpH5y3pvtRzatAiuMJk", "abcd1111"],
        myacct= "tNULSeBaMpxUVQLW9J3AzbjFsQVRpC5RAnxVKz"
        pw = "kathy123"
        # method_nm = "getPriKey"
        param_list = [2, myacct, pw]
        self.doit("getPriKey", param_list, meth_type)  # [self.tchain_id], 'POST' are defaults

    def getcoininfo(self, meth_type='POST'):  # consensusTotal
        param_list = [self.tchain_id]
        self.doit("getCoinInfo", param_list, meth_type)  # [self.tchain_id], 'POST' are defaults

    # def getchaininfo(self, chid=1, meth_type='POST'):
    #     param_list = [chid]
    #     self.doit("getCoinInfo", param_list, meth_type)  # [self.tchain_id], 'POST' are defaults

    def getdeposit(self, meth_type='POST'):
        param_list = [1]
        self.doit("getTotalDeposit", param_list, meth_type)  # [self.tchain_id], 'POST' are defaults

    def getaccounts(self, meth_type='POST'):  # 4=POST
        method_nm = "getaddresslist"  #getaddresslist
        page_number = 1
        page_size = 99999

        p_list = [self.tchain_id, page_number, page_size]
        request = prepare_top_section(method_nm, p_list, self.myurl, method_type=meth_type)
        response_tup = SendRequest.send_request(request)

        result_part = response_tup[0].get('result')
        result_addy = result_part.get('address')



if __name__ == "__main__":  #  for test networks chain_id is 2
    # note in ver 2.5 everything is POST, never get, most are 8003, some 8004

    s1 = SimpleRequests(1, 1, 'url3')   # machine=1 public1, chainid=1  west:  3,       nuls:1, 1
    ntcaccts = ['NULSd6HgjGMkrh5mbmWPMxaTzgpZBctSQBizG',  # consensuslock: 2000000000000 totalbalance: 2000085969280
                'NULSd6Hgi8DVA1evHpuojzMpedHgsYojYaKBe',  # consensuslock: 2000000000000 totalbalance: 2000009711110
                'NULSd6HgaA7qFUw3jVkcqRD1iggzoffEigJRe',  # consensuslock: 0 totalbalance: 0  now in: xFZx
                'NULSd6HgVnuWDhVzdUcGScoS4erce4jYtWL8w',  # consensuslock: 0 totalbalance: 0  now in: xFZx
                'NULSd6HgbM6hYM2RRNjK4JQmnoLdS96NV77aV',  # consensuslock: 0 totalbalance: 0  now in: xFZx
                'NULSd6HgcKLvyoqUdqcTUe8oDjKUK25v8Cqff',  # consensuslock: 2000000000000 totalbalance: 2000009900000
                'NULSd6HgcX2oV8tb7utfJJN9G3x9Tjj5YcdXA',  # consensuslock: 0 totalbalance: 0
                'NULSd6Hge1jAwN3JXpMu1XA8RN33WnaJHCHVB',  # consensuslock: 20,000.00000000 totalbalance: 2000009900000
                'NULSd6Hge4zpeVW7GPDnsCgPDVHnxakHEXRXE',  # consensuslock: 20,000.00000000 totalbalance: 2000009900000
                'NULSd6HgectFiZCqoUzpEB4okDBALx4BJBfKd',  # consensuslock: 20,000.00000000 totalbalance: 2000009900000
                'NULSd6HgftfyNoKhzDzvAUHCA2vgnjCBUuf7a',  # consensuslock: 0 totalbalance: 20000.09900000
                'NULSd6HgcfGtsmm79QDoBK1MAjqNmm3rgKXSj',  # consensuslock: 0 totalbalance: 250328829
                'NULSd6HgjAc2pXyBi6P4EVMC6MAmnn5Ei5SgL',  # consensuslock: 0 totalbalance: 15253.76695481
                'NULSd6HgjDZmLMbZSmH9tqb6smdzZHCxsCRD3',  # consensuslock: 0 totalbalance: 0
                'NULSd6HgYhGUZYApGnB3PLwa6Ji5GLJDtt6LZ',  # consensuslock: 0 totalbalance: 20000.09300000
                'NULSd6Hh84g7u61ntrWhrdEMjXvM9STRPxFZx',  # consensuslock: 4,299,999.00000000 totalbalance: 7,702,713.12653025
                'NULSd6Hh76ja8dHkTdYvTJS9gEAygiU1uLRGR',  # consensuslock: 0 totalbalance: 12,076,898.96243277
                'NULSd6HgXY3zLvEoCRUa6yFXwpnF8gqrDeToT',
                ]
    # new acct : NULSd6Hh84g7u61ntrWhrdEMjXvM9STRPxFZx 7.8 mils

    # for i in ntcaccts:
    #     s1.get_account(i)

    #s1.getaccounts()
    s1.get_account('NULSd6Hh76ja8dHkTdYvTJS9gEAygiU1uLRGR')

    # s.get_account('SPEXdKRT4pz7ZhasM9pTK4fvGrJf8eod5ZqtXa', 'POST',)
    # s.getBlockHeaderList()
    # s.get_consensus_node_ct()
    # s.get_block_by_height(900000)
    # s.get_chain_cmd("getVersion")



                          # s1.get_block_by_height("100")


    #s3 = SimpleRequests(3, 9, 'url3')   # machine=1 public1, chainid=1  west:  3,       nuls:1, 1


    # ---- westteam:
    #s3.nerve_chaininfo()  # nerve only: getHeaderByHeight   # works

    #myacct="tNULSeBaMpxUVQLW9J3AzbjFsQVRpC5RAnxVKz"
    #pw = "kathy123"
    # s1.get_prikey(myacct, pw)
    #s3.getcoininfo()
    #s3.getdeposit()

    #s1.get_chain_cmd(method_nm="consensusInfo")
    #s1.get_chain_cmd4(method_nm="getChainInfo")

    print()



    # int COIN_BASE = 1;						//coinBase reward
    # int TRANSFER = 2;						//transfer
 	# int ACCOUNT_ALIAS = 3;					//set account alias
   	# int REGISTER_AGENT = 4;					//register consensus node
   	# int DEPOSIT = 5;						//stake to join consensus
    # int CANCEL_DEPOSIT = 6;					//cancel staking
    # int YELLOW_PUNISH = 7;					//yellow card punishment
    # int RED_PUNISH = 8;						//red card punishment
    # int STOP_AGENT = 9;						//unregister consensus node
    # int CROSS_CHAIN = 10;					//cross-chain transfer
	# int REGISTER_CHAIN_AND_ASSET = 11;		//register chain
    # int DESTROY_CHAIN_AND_ASSET = 12;		//destroy chain
    # int ADD_ASSET_TO_CHAIN = 13;			//add asset to chain
   	# int REMOVE_ASSET_FROM_CHAIN = 14;		//remove asset from chain
    # int CREATE_CONTRACT = 15;				//create contract
    # int CALL_CONTRACT = 16;					//call contract
    # int DELETE_CONTRACT = 17;				//delete contract
    # int CONTRACT_TRANSFER = 18;				//contract transfer
    # int CONTRACT_RETURN_GAS = 19;			//contract for returning fee
    # int CONTRACT_CREATE_AGENT = 20;			//contract for registering consensus node
	# int CONTRACT_DEPOSIT = 21;				//contract for staking to join consensus
 	# int CONTRACT_CANCEL_DEPOSIT = 22;		//contract for canceling staking
 	# int CONTRACT_STOP_AGENT = 23;			//contract for unregistering consensus node


















    # s3.get_block_by_height(3900000)  ## works
    #s1.get_block_by_height(4000000)  # works
    #s1.get_the_best_block()
    #s1.getcoininfo()
    #s3.get_the_best_block()

    #
    # s4.get_chain_cmd("getBestBlockHeader")
    #s3.get_chain_cmd("getAllAddressPrefix")  # works
    # s3.get_getConsensusNodes()  # works
    # s1.get_getConsensusNodes()  # works
    #s1.get_chain_cmd_public(method_nm="getCoinInfo")
    # s.get_chain_cmd("cs_getRoundInfo")
    # s.get_chain_cmd("cs_getRoundInfo")
    # s.get_chain_info_cs()


    # parta = response_d[0]  # dict myresults = parta['result'] myresult_txlist = myresults['txList'] answerlist = [] donetxs = [] for txdict in myresult_txlist: if txdict['coinTos']: thehash =
    # txdict['hash'] theheight = txdict['height'] tremark = txdict['remark'] tvalue = txdict['value'] possible_nuls_addys = txdict['coinTos'] for addy in possible_nuls_addys: if thehash not in
    # donetxs: answerlist.append([theheight, addy['address'], thehash,  tvalue, tremark])
    #                 donetxs.append(thehash)


