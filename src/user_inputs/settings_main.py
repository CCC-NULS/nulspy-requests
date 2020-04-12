#!/usr/bin/python3.7

 # 0=KathyUbuntu, 1=westteam


def get_settings(machine):
    if machine == 0:
        chain0 = 24442
        url30 = "http://78.47.206.255:18003"
        url40 = "http://78.47.206.255:18004/jsonrpc"
        settings_d = {"chain": chain0, "url3": url30, "url4": url40}
        return settings_d

    elif machine == 1:
        chain1 = 4810
        url31 = "http://westteam.nulstar.com:18003"
        url41 = "http://westteam.nulstar.com:18004/jsonrpc"
        settings_d = {"chain": chain1, "url3": url31, "url4": url41}
        return settings_d

    elif machine == 2:
        chain2 = 2
        url32 = "http://127.2.0.1:18003"
        url42 = "http://127.0.0.1:18004/jsonrpc"
        settings_d = {"chain": chain2, "url3": url32, "url4": url42}
        return settings_d

    elif machine == 3:
        chain2 = 2
        url32 = "http://beta.wallet.nuls.io:18003"
        url42 = "http://beta.wallet.nuls.io:18004/jsonrpc"
        settings_d = {"chain": chain2, "url3": url32, "url4": url42}
        return settings_d

        # beta.wallet.nuls.io: 47.244.186.65
    # http://apitn2.nulscan.io
    # https: // beta.wallet.nuls.io / api
