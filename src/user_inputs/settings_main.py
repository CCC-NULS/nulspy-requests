#!/usr/bin/python3.7


def get_settings(machine=0, cid=1, urltype='url3'):
    port3 = "8003"
    port4 = "8004"
    machine0 = "http://78.47.206.255"
    machine2 = "http://127.2.0.1"
    machine1 = "http://public1.pocm.nuls.io"
    machine3 = "http://public1.nuls.io"
    machine3 = "http://public2.nuls.io"
    machine3 = "http://beta.public1.nuls.io"  # use chain 2
    #machine3 = "http://beta.nulscan.io/api"   # is ok!!  sometimes...

    machine3775 = "http://beta.public1.nuls.io" # bad
    machine37 = "http://beta.api.nuls.io"  #bad
    machine37777 = "http://beta.pocm.nuls.io"  #bad
    machine3 = "http://beta.nerve.network"   # is ok!!
    machine3 = "http://beta.public1.nuls.io"  # use chain 2
    #machine3 = "http://beta.wallet.nuls.io"  # use chain 2

    machine4 = "http://westteam.nulstar.com"


    if machine == 0:
        if urltype == 'url3':
            url = f"{machine0}:{port3}"
        else:
            url = f"{machine0}:{port4}"
        settings_main_dd = {"cid": cid, "url": url}
        return settings_main_dd

    elif machine == 1:  # westteam
        if urltype == 'url3':
            url = f"{machine1}:{port3}"
        else:
            url = f"{machine1}:{port4}"
        settings_main_dd = {"cid": cid, "url": url}
        return settings_main_dd

    elif machine == 2:
        if urltype == 'url3':
            url = f"{machine2}:{port3}"
        else:
            url = f"{machine2}:{port4}"
        settings_main_dd = {"cid": cid, "url": url}
        return settings_main_dd

    elif machine == 3:
        if urltype == 'url3':
            url = f"{machine3}"
        else:
            url = f"{machine3}"
        settings_main_dd = {"cid": cid, "url": url}
        return settings_main_dd

    elif machine == 4:   # westteam  # still running 2.5
        port3 = "8003"
        port4 = "8004"
        if urltype == 'url3':
            url = f"{machine4}:{port3}"
        else:
            url = f"{machine4}:{port4}/jsonrpc"
                         # url44 = f"{machine4}:{port4}/jsonrpc"
        settings_main_dd = {"cid": cid, "url": url}
        print("url: ", url)
        return settings_main_dd

#no port required --  curl -s -X POST -H 'Content-Type: application/json' --data '{"jsonrpc":"2.0","method":"getChainInfo","params":[],"id":1234}' http://public2.nuls.io