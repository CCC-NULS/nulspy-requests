#!/usr/bin/python3.7


from src.libs.master_setup import master_setup, unpack_d, unpack_etc
from src.libs.setup_top import get_top
from src.libs.send_req import SendRequest
import json


class GetAccounts(object):

    def __init__(self, machine=0, chainid=0, urltype='url3'):
        settings_main_dd, sender_etc_dd, self.receivers = master_setup(machine, chainid, urltype)
        self.cid, self.url = unpack_d(settings_main_dd)
        self.sender, self.pw = unpack_etc(sender_etc_dd)
        self.remark = "get list of accounts"
        self.assetid = 1
        self.id = 999

    def getaccounts(self, meth_type='POST'):  # 4=POST, 3=GET
        method_nm = "getAccountList"
        length = 99999
        p_list = [self.cid, self.assetid, length]
        request = get_top(method_nm, p_list, self.url, meth_type)  # 0 = get, 1=post
        print("method_nm: " + str(method_nm) + "  meth_type: " + str(meth_type))
        print("query: " + str(request))
        json_formatted_str = json.dumps(request.json, indent=2)
        print(json_formatted_str)
        response_d = SendRequest.send_request(request)
        print("  ANSWER to query ", method_nm, " is: ")
        # print(urltype)
        print(" ---------> The response is: " + json.dumps(response_d) + " ---------> \n\n")
        return response_d


        # resp1, rstr = SendRequest.send_request(request)
        # results_d = resp1.get("result")
        # return results_d


if __name__ == "__main__":
    c = GetAccounts(3, 2)   # machine, chainid
    results = c.getaccounts()['list']

    for i in results:
        print("'" + i['address'] + "',")

    # print(dumps(res['list'][0], indent=2))

        #machine = 4     #   machine = 1   # 1 for west, 0 for kathy

# real accts:
# 'SPEXdKRT4kGmFz68ChyJrcjzFfggb8b1aNyaKh',   *
# 'SPEXdKRT4wqaQkYBM8bFm9PyyTumB6GgXSQ57G',  *
# 'SPEXdKRT4ja5aFgREi6HhnxcGPyVi8yfpDvSys',   *





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