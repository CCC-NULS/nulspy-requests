#!/usr/bin/python3.7

# setup:  enter list in input_lists

from src.libs.master_setup import master_setup, unpack_d, unpack_etc, ret_url
from src.libs.setup_top import get_top
from src.libs.send_req import SendRequest


# @Parameter(parameterName="chainId", requestType= @TypeDescriptor(value=int. class ), parameterDes = "链id"),
# @ Parameter(parameterName = "assetChainId", requestType = @ TypeDescriptor(value = int.class ), parameterDes = "资产链id"),
# @ Parameter(parameterName = "assetId", requestType = @ TypeDescriptor(value = int.class ), parameterDes = "资产id"),
# @ Parameter(parameterName = "address", parameterDes = "转出账户地址"),
# @ Parameter(parameterName = "toAddress", parameterDes = "转入账户地址"),

class Transfer(object):

    def __init__(self, machine=0, chainid=0, urltype='url3'):
        settings_main_dd, sender_etc_dd, self.receivers = master_setup(machine, chainid, urltype)
        self.cid, self.url = unpack_d(settings_main_dd)

        self.sender, self.pw = unpack_etc(sender_etc_dd)
        self.remark = "transfer"
        self.assetid = 1
        self.id = 999

    def transfer(self, base_amt, meth_type='POST'):      #ch assetid address toaddy pw amt rem
        method_nm = 'transfer'
        # assetChainId = self.cid
        asset_id = 1

        multiplier = 10**8
        amt = base_amt * multiplier
        # amt = 2000 * (10**8) - 2000
        amt = base_amt

        for receiver in self.receivers:
            print("doing this receiver: ", receiver)
            p_list = [self.cid, self.cid, self.sender, receiver, self.pw, base_amt, self.remark]
            request = get_top(method_nm, p_list, self.url, meth_type)
            resp1, rstr = SendRequest.send_request(request)
            print("resp1: ", rstr)


if __name__ == "__main__":
    c = Transfer(4, 4810, 'url4')  # 4 = westteam  # put machine here, 4=westteam  almost works with url4
    c.transfer(1, 'POST')   # 4 = POST

# transfer "SPEXdKRT4pz7ZhasM9pTK4fvGrJf8eod5ZqtXa" "SPEXdKRT4trozwzXj5n1d7vZ7NR9QqbUFh4KG7" 1


'''
chainId	int	chain id	yes
assetId	int	asset id	yes
address	string	Transfer out account address	Yes
toAddress	string	Transfer to account address	Yes
password	string	Transfer Account Password	Yes
amount	string	Transfer Amount	Yes
remark	string	Notes	Yes
#return value

'''