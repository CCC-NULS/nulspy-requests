#!/usr/bin/python3.7

# setup:  enter list in input_lists

from src.libs.master_setup import master_setup, unpack_d
from src.libs.setup_top import get_top
from src.libs.send_req import SendRequest


# @Parameter(parameterName="chainId", requestType= @TypeDescriptor(value=int. class ), parameterDes = "链id"),
# @ Parameter(parameterName = "assetChainId", requestType = @ TypeDescriptor(value = int.class ), parameterDes = "资产链id"),
# @ Parameter(parameterName = "assetId", requestType = @ TypeDescriptor(value = int.class ), parameterDes = "资产id"),
# @ Parameter(parameterName = "address", parameterDes = "转出账户地址"),
# @ Parameter(parameterName = "toAddress", parameterDes = "转入账户地址"),

class Transfer(object):

    def __init__(self, machine=4, chainid=4810):
        #machine = 4     #   machine = 1   # 4 for west,

        settings_d, sender_etc_dd, self.receivers = master_setup(machine, chainid)
        self.chain, self.url3, self.sender, self.pw = unpack_d(settings_d, sender_etc_dd)
        self.url4 = settings_d.get('url4')
        self.remark = 'xfer'
        self.asset = 1
        self.id = 99999

    def transfer(self, base_amt):      #ch assetid address toaddy pw amt rem
        method_nm = 'transfer'
        chainId = 2
        assetChainId = 1
        assetId = 1

        multiplier = 10**8
        amt = base_amt * multiplier
        #amt = 2000 * (10**8) - 2000

        for receiver in self.receivers:
            print("doing this receiver: ", receiver)
            #   p_list = [self.chain, self.asset, self.sender, receiver, self.pw, amt, self.remark]
            #2, 2, 1,
            #p_list = [chainId, assetChainId, self.sender, receiver, self.pw, amt, self.remark]
            p_list = [4810, 1, self.sender, receiver, self.pw, amt, self.remark]
            request = get_top(method_nm, p_list, self.url4)
            resp1, rstr = SendRequest.send_request(request)
            print("resp1: ", rstr)


if __name__ == "__main__":
    c = Transfer(4)   # put machine here, 4=westteam
    c.transfer()

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