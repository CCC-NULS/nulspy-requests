#!/usr/bin/python3.7

from typing import List, Any
import src.user_inputs.settings_main as settings
from src.libs.setup_top import prepare_top_section
from src.libs.send_req import SendRequest
import datetime


# print transactions in each block - block by block. set start and end blocks.
class SimpleTransacts(object):
    def __init__(self, machine=4, chainid=1, urltype='url3'):
        # settings_main_dd, sender_etc_dd, self.receivers = self.master_setup(machine, chainid, urltype)
        settings_main_dd = settings.target_setup(machine, chainid, urltype)
        self.tchain_id = settings_main_dd.get('tchain_id')
        self.myurl = settings_main_dd.get('myurl')
        self.remark = "empty"
        self.assetid = 1
        self.id = 999
        self.special = 0

    def add_up(self, response_dict2):
        resp_list_of_d = response_dict2.get("result").get("list")
        bigtot = 0
        for anode in resp_list_of_d:
            tot_dep = anode.get("totalDeposit")

            agent_alias = anode.get("agentAlias")
            if not agent_alias:
                agent_alias = "NoName Node"
            newstr = agent_alias + ":  totalDeposit"
            print(newstr, tot_dep)
            bigtot += tot_dep

        print()
        bt = bigtot / 100000000
        print("total staked: ", bigtot)
        f"{bt:,}"
        print(f"{bt:,}")

    # def prepare_top_plain(method, param_list, the_url, method_type='POST'):  # no method
    def doit(self, method_name, parameter_list, method_type='POST'):
        request = prepare_top_section(method_name, parameter_list, self.myurl, method_type=method_type)
        response_tup = SendRequest.send_request(request)
        response_dict = response_tup[0]  # dict

        # this is for very first block, very first tx - this is where Nuls 1.0 vals were moved
        if method_name == 'getBlockByHeight':
            response_result = response_dict.get('result')
            result_tx_list = response_result.get('txList')

            biglist: List = []
            for transaction in result_tx_list:
                if transaction.get('type') < 456:
                    if True:
                        dtime: datetime = datetime.datetime.fromtimestamp(transaction.get('createTime'))
                        coin_tos_list: List[Any] = transaction.get('coinTos')  # list of dict TO
                        if coin_tos_list:
                            for coin_to_itm_dict in coin_tos_list:
                                coin_amt = int(coin_to_itm_dict.get('amount')/100000000)
                                coin_to = str(coin_to_itm_dict.get('address'))
                                biglist.append([coin_amt, coin_to])

            biglist.sort()
            for temp_list in biglist:
                temp_list0 = temp_list[0]  # for decimal
                print(f"{temp_list0:,}" + "   " + temp_list[1])

        if self.special == 1:
            self.add_up(response_dict)
        self.special = 0
        return response_tup, []

    def get_block_by_height(self, height='900000', meth_type='POST'):
        method_nm = "getBlockByHeight"
        param_list = [self.tchain_id, height]
        biglist, anotherlist = self.doit(method_nm, param_list, meth_type)
        return biglist, anotherlist

    def get_chain_info_cs(self):
        method_nm = "cs_getChainInfo"  # getChainInfo
        param_list = [self.tchain_id]
        self.doit(method_nm, param_list, 'POST')   # four=1 for 8004 or 18004


if __name__ == "__main__":  #  for test networks chain_id is 2
    # note in ver 2.5 everything is POST, never get, most are 8003, some 8004

    s1 = SimpleTransacts(1, 1, 'url3')   # machine=1 public1, chainid=1  west:  3,       nuls:1, 1
    for i in range(0, 2):  # block numbers
        print("on:", i)
        s1.get_block_by_height(i)
        print()


    # for i in range(2462843, 4122222):  # block numbers  2462843=Jun23-2020



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


