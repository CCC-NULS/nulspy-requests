#!/usr/bin/python3.7


def get_settings(machine=0, cid=1):
    port3 = "8003"
    port4 = "8004"
    machine0 = "http://78.47.206.255"
    machine2 = "http://127.2.0.1"
    machine1 = "http://public1.pocm.nuls.io"
    machine3 = "http://public1.nuls.io"
    machine3 = "http://public2.nuls.io"
    machine3 = "http://beta.public1.nuls.io"  # use chain 2
    machine3 = "http://beta.public1.nuls.io"  # use chain 2
    #machine3 = "http://beta.nulscan.io/api"   # is ok!!  sometimes...

    machine3775 = "http://beta.public1.nuls.io" # bad
    machine37 = "http://beta.api.nuls.io"  #bad
    machine37777 = "http://beta.pocm.nuls.io"  #bad
    machine3 = "http://beta.nerve.network"   # is ok!!

    machine4 = "http://westteam.nulstar.com"


    if machine == 0:
        url30 = f"{machine0}:{port3}"
        url40 = f"{machine0}:{port4}/jsonrpc"
        settings_main_dd = {"cid": cid, "url3": url30, "url4": url40}
        return settings_main_dd

    elif machine == 1:  # westteam
        url31 = f"{machine1}:{port3}"
        url41 = f"{machine1}:{port4}/jsonrpc"
        settings_main_dd = {"cid": cid, "url3": url31, "url4": url41}
        return settings_main_dd

    elif machine == 2:
        url32 = f"{machine2}"
        url42 = f"{machine2}"
        settings_main_dd = {"cid": cid, "url3": url32, "url4": url42}
        return settings_main_dd

    elif machine == 3:
        url33 = f"{machine3}"   # running new no ports nec
        url43 = f"{machine3}"
        settings_main_dd = {"cid": cid, "url3": url33, "url4": url43}
        return settings_main_dd

    elif machine == 4:   # westteam  # still running 2.5
        port3 = "8003"
        port4 = "8004"
        url3 = f"{machine4}:{port3}"
        url4 = f"{machine4}:{port4}"
        # url44 = f"{machine4}:{port4}/jsonrpc"
        settings_main_dd = {"cid": cid, "url3": url3, "url4": url4}
        return settings_main_dd

#no port required --  curl -s -X POST -H 'Content-Type: application/json' --data '{"jsonrpc":"2.0","method":"getChainInfo","params":[],"id":1234}' http://public2.nuls.io