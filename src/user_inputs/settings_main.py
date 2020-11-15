#!/usr/bin/python3.7


def get_settings(machine):
    port3 = "18003"
    port4 = "8004"
    chain = 2
    machine0 = "http://78.47.206.255"
    machine2 = "http://127.2.0.1"
    machine399 = "http://public1.pocm.nuls.io"
    machine3 = "http://public1.nuls.io"
    machine3 = "http://public1.nuls.io"
    machine3 = "https://wallet.nuls.io"

    machine377 = "http://beta.wallet.nuls.io" #bad
    machine3775 = "http://beta.public1.nuls.io" # bad
    machine37 = "http://beta.api.nuls.io"  #bad
    machine37777 = "http://beta.pocm.nuls.io"  #bad
    machine344 = "http://beta.nulscan.io"  #bad
    machine3 = "http://public2.nuls.io"
    machine3 = "https://nuls.io"
    machine3 = "http://beta.nulscan.io"   # is ok!!  sometimes...
    machine3 = "http://beta.nerve.network"   # is ok!!
    machine3 = "https://wallet.nerve.network"

 #   curl -X POST -p 8003 - H 'Content-Type: application/json' -data '{"jsonrpc":"2.0","method":"getBestBlockHeader","params":[2], "id":1234}' http://beta.public1.nuls.io

    machine3 = "http://beta.public1.nuls.io"  # use chain 2
    machine3 = "http://beta.public1.nuls.io"  # use chain 2
    machine4 = "http://westteam.nulstar.com"
    #machine3 = "http://beta.nulscan.io/api"   # is ok!!  sometimes...


    if machine == 0:
        chain0 = 24442
        url30 = f"{machine0}:{port3}"
        url40 = f"{machine0}:{port4}/jsonrpc"
        settings_d = {"chain": chain0, "url3": url30, "url4": url40}
        return settings_d

    elif machine == 1:  # westteam
        chain1 = chain    # space exploration
        url31 = f"{machine1}:{port3}"
        url41 = f"{machine1}:{port4}/jsonrpc"
        settings_d = {"chain": chain1, "url3": url31, "url4": url41}
        return settings_d

    elif machine == 2:
        chain2 = chain
        url32 = f"{machine2}"
        # url32 = f"{machine2}:{port3}"
        url42 = f"{machine2}"
        # url42 = f"{machine2}:{port4}/jsonrpc"
        settings_d = {"chain": chain2, "url3": url32, "url4": url42}
        return settings_d

    elif machine == 3:
        port3 = "8003"
        port4 = "8004"
        chain3 = 2
        # url33 = f"{machine3}:{port3}"
        # url43 = f"{machine3}:{port4}/jsonrpc"
        # # url33 = f"{machine3}:{port3}"
        url33 = f"{machine3}"
        url43 = f"{machine3}"
        # settings_d = {"chain": chain3, "url3": url33, "url4": url43}
        settings_d = {"chain": chain3, "url3": url33, "url4": url43}
        return settings_d

    elif machine == 4:   # westteam
        chain4 = 4810
        port3 = "8003"
        port4 = "8004"
        url34 = f"{machine4}:{port3}"
        url44 = f"{machine4}:{port4}/jsonrpc"
        settings_d = {"chain": chain4, "url3": url34, "url4": url44}
        return settings_d

#no port required --  curl -s -X POST -H 'Content-Type: application/json' --data '{"jsonrpc":"2.0","method":"getChainInfo","params":[],"id":1234}' http://public2.nuls.io