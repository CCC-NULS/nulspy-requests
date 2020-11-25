#!/usr/bin/python3.7


def get_settings(machine=0, cid=1, urltype='url3'):
    port3 = "8003"
    port4 = "8004"
    port4 = "17004"

    machine0 = "http://78.47.206.255"
    machine2 = "http://127.2.0.1"
    machine1 = "http://public1.pocm.nuls.io"
    machine3 = "http://beta.public1.nuls.io"  # use chain 2
    #machine3 = "http://beta.nulscan.io/api"

    machine3775 = "http://beta.public1.nuls.io"
    machine37 = "http://beta.api.nuls.io"
    machine37777 = "http://beta.pocm.nuls.io"
    machine366 = "http://beta.nerve.network"
    #machine3 = "http://beta.wallet.nuls.io"  # use chain 2

    machine344 = "http://beta.public1.nuls.io"  # use chain 2
    machine3 = "http://westteam.nulstar.com"
    machine3 = "https://public.nerve.network"
    machine3443 = "https://public1.nuls.io"
    machine354 = "https://westteam.nulstar.com:17004/jsonrpc"


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
            url = f"{machine3}"
            #url = f"{machine3}:{port3}"
        settings_main_dd = {"cid": cid, "url": url}
        return settings_main_dd

    elif machine == 3999:  # westteam
        if urltype == 'url3':
            url = f"{machine3}"
        else:
            url = f"{machine3}"
            #url = f"{machine3}:{port3}"
        settings_main_dd = {"cid": 4810, "url": url}
        return settings_main_dd


    elif machine == 300:  # public1.nuls.io   # https://public1.nuls.io works!!! must b: cid:  1  url:  https://public1.nuls.io/jsonrpc
        ###  use no port, use POST for public1  also works for https://public.nerve.networks/jsonrpc
        if urltype == 'url3':
            url = f"{machine3}/jsonrpc"
        else:
            url = f"{machine3}/jsonrpc" \
                f""
        settings_main_dd = {"cid": cid, "url": url}
        return settings_main_dd

    elif machine == 3:  # public1.nuls.io   # https://public1.nuls.io works!!! must b: cid:  1  url:  https://public1.nuls.io/jsonrpc
        ###  use no port, use POST for public1  also works for https://public.nerve.networks/jsonrpc
        if urltype == 'url3':
            url = f"{machine3}/jsonrpc"
            #url = f"{machine3}"
        else:
            url = f"{machine3}/jsonrpc"
            #url = f"{machine3}"
        settings_main_dd = {"cid": cid, "url": url}
        return settings_main_dd

    elif machine == 33:
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