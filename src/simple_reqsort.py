#!/usr/bin/python3.7

import json
from typing import List, Any

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
        #print("running on this url:  " + self.myurl)
        #print(json.dumps(request.json))

        response_tup = SendRequest.send_request(request)
        response_str = response_tup[1]  # str
        response_parsed = json.loads(response_str)
        # print(response_str)
        #print(json.dumps(response_parsed, indent=2, sort_keys=True))

        # for consensus only
        response_dict = json.loads(response_str)
        #  # temp only: - -  - - --  --- --  --  --- - --  --- - --April 1 2021  --- - --  --- -
        big = 0

        if method_name == 'getBlockByHeight':
            response_result = response_dict.get('result')
            result_tx_list = response_result.get('txList')
            biglist = []
            if big == 1:
                for transaction in result_tx_list:
                    print()
                    print("----------------------------")
                    print("height: ", transaction.get('height') +" txData: ", transaction.get('txData'))
                    print("value: ", transaction.get('value') + "size: ",  transaction.get('size'))
                    print("coinFroms: " + str(transaction.get('coinFroms')))
                    print("coinTos: " + str(transaction.get('coinTos')) + "remark: " + str(transaction.get('remark')))

            for transaction in result_tx_list:
                if transaction.get('type') == 3:
                    transaction_val = transaction.get('value')
                    if transaction_val >= 2000000000:
                        part1, part2, to_addy, crtime = '', '', '', ''
                        dtime: datetime = datetime.datetime.fromtimestamp( transaction.get('createTime'))

                        coin_frm_list: List[Any] = transaction.get('coinFroms')  # list of dict
                        if coin_frm_list:  # list of dict FROM
                            for coinf_itm_dict in coin_frm_list:
                                print("  --coinFroms: " + str(coinf_itm_dict.get('address')) +
                                      " coinfrom amt: " + str(coinf_itm_dict.get('amount')) +
                                      " coinfrom locked: " + str(coinf_itm_dict.get('locked')))
                        coin_tos_list: List[Any] = transaction.get('coinTos')  # list of dict TO
                        if coin_tos_list:
                            for coin_to_itm_dict in coin_tos_list:
                                print("  --coinTos: " + str(coin_to_itm_dict.get('address')) +
                                      " cointo amt: " + str(coin_to_itm_dict.get('amount')) +
                                      " cointo locked: " + str(coin_to_itm_dict.get('locked')))

                        part1 = str(transaction.get('value')) + ";"
                        part2 = str(transaction.get('height')) + ";"
                        remarky = " remark:" + str(transaction.get('remark'))
                        timey = ";" + str(dtime)
                        newstr = part1 + part2 + str(to_addy) + ";" + timey + remarky
                        biglist.append(newstr)

        biglist.sort()
        for x in biglist:
            print(x)

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

    s1 = SimpleRequests(1, 1, 'url3')   # machine=1 public1, chainid=1  west:  3,       nuls:1, 1
    for i in range(0, 100):
        print("on:", i)
        s1.get_block_by_height(i)
        print()





