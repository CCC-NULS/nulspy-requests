#!/usr/bin/python3.7


from src.libs.master_setup import master_setup, unpack_d
from src.libs.setup_top import get_top
from src.libs.send_req import SendRequest
from json import dumps

class GetAccounts(object):

    def __init__(self, machine=4, chainid=2):
        #machine = 4     #   machine = 1   # 1 for west, 0 for kathy

        settings_d, sender_etc_dd, self.receivers = master_setup(machine, chainid)
        self.chain, self.url3, self.sender, self.pw = unpack_d(settings_d, sender_etc_dd)
        self.url4 = settings_d.get('url4')
        self.remark = "get list of accounts"
        # self.chain = chainid
        self.asset = 1
        self.id = 99999

    def getaccounts(self):
        method_nm = "getAccountList"
        length = 99999
        self.asset = 2
        p_list = [self.chain, self.asset, length]
        request = get_top(method_nm, p_list, self.url3)
        resp1, rstr = SendRequest.send_request(request)
        results_d = resp1.get("result")
        return results_d


if __name__ == "__main__":
    c = GetAccounts(4, 4810)
    res = c.getaccounts()['list']

    for i in res:
        print("'" + i['address'] + "',")

    # print(dumps(res['list'][0], indent=2))

# 'SPEXdKRT4sX9XTHvyP5qBKsZGihgUVdNVmWihL',
# 'SPEXdKRT5ANiZNnLuRuFSKsqY4nX4twQ88vhb5',
# 'SPEXdKRT4wqaQkYBM8bFm9PyyTumB6GgXSQ57G',
# 'SPEXdKRT4vwmpHZiufc7SWSW69AFw6x39uJZZE',
# 'SPEXdKRT4ja5aFgREi6HhnxcGPyVi8yfpDvSys',
# 'SPEXdKRT4yvkvyWr4iGamMDKGzhiGgkjDYtZfR',
# 'SPEXdKRT54LQChhXy491qdJ1vXXAjjXNUSY2km',
# 'SPEXdKRT4kGmFz68ChyJrcjzFfggb8b1aNyaKh',
# 'SPEXdKRT51rgzKMchGYbNQ5pkDGuFjy7xaxJEZ',
# 'SPEXdKRT5AavVv9Czg7XbRgo8EaVe5aX5ypoTJ',