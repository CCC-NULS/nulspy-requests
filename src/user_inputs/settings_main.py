#!/usr/bin/python3.7


def target_setup(machine=2, tchain_id=1, urltype='url3'):
    print("urltype: ", urltype)
    print("tchain_id: ", tchain_id)
    main_machine = ""
    myurl = None

    if machine == 2:
        main_machine = "https://public1.nuls.io"
        if urltype == 'url3':
            myurl = f"{main_machine}"
        elif urltype == 'url4':
            myurl = f"{main_machine}"
        else:
            myurl = f"{main_machine}"

    elif machine == 1:
        main_machine = "http://westteam.nulstar.com"
        port3 = "18013"
        port4 = "18014"
        if urltype == 'url3':
            myurl = f"{main_machine}:{port3}"
        elif urltype == 'url4':
            myurl = f"{main_machine}:{port4}"

    print("main_machine: ", main_machine)
    print("tchain_id: ", tchain_id)
    print("myurl: ", myurl)

    targ_dict = {"tchain_id": tchain_id, "myurl": myurl}  # mychain_id is usually 1, 4810 for SPEX
    print("final myurl: ", myurl)
    return targ_dict

















# main_machine = "https://public1.nuls.io"
# # main_machine = "http://beta.public1.nuls.io"
# # main_machine = "https://nulscan.io/jsonrpc"
# # main_machine = "http://westteam.nulstar.com"
# main_machine = "http://beta.public.nerve.network"
# # main_machine = "https://public.nerve.network"
#
# # main_machine = "http://beta.nervedex.com/"




    # port3 = "18003"
    # port4 = "18004"

    # machine2 = "http://127.2.0.1"
    # machine1 = "http://public1.pocm.nuls.io"
    # machine4 = "https://public1.nuls.io"  # use chain 2
    #
    # if machine == 0:
    #     if urltype == 'url3':
    #         myurl = f"{machine0}:{port3}"
    #     else:
    #         myurl = f"{machine0}:{port4}"
    #     target_setup_dd = {"mychain_id": mychain_id, "myurl": myurl}
    #     return target_setup_dd

    # if machine == 4:   # westteam  # still running 2.5
            # url44 = f"{machine4}:{port4}/jsonrpc"

    # elif machine == 42:   # westteam  # offline smart contract test
    #     port4 = "7772"
    #     myurl = f"{machine4}:{port4}"
    #                      # url44 = f"{machine4}:{port4}/jsonrpc"
    #     target_setup_dd = {"mychain_id": mychain_id, "myurl": myurl}
    #     print("myurl: ", myurl)
    #     return target_setup_dd


#no port required --  curl -s -X POST -H 'Content-Type: application/json' --data '{"jsonrpc":"2.0","method":"getChainInfo","params":[],"id":1234}' http://public2.nuls.io



    # elif machine == 3:  # public1.nuls.io   # https://public1.nuls.io works!!! must b: mychain_id:  1  myurl:  https://public1.nuls.io/jsonrpc
    #     ###  use no port, use POST for public1  also works for https://public.nerve.networks/jsonrpc


    #machine3 = "http://beta.nulscan.io/api"
   # machine1 = "http://public1.pocm.nuls.io"

    machine3775 = "http://beta.public1.nuls.io"
    machine37 = "http://beta.api.nuls.io"
    machine37777 = "http://beta.pocm.nuls.io"
    machine366 = "http://beta.nerve.network"
    #machine3 = "http://beta.wallet.nuls.io"  # use chain 2

    machine344 = "http://beta.public1.nuls.io"  # use chain 2
    machine3 = "https://public.nerve.network"
    #machine4 = "http://public2.nuls.io"
    machine354 = "https://westteam.nulstar.com:17004/jsonrpc"
    # machine4 = "http://westteam.nulstar.com"
    corsproxy = "https://westteam.nulstar.com:3002/"
    machine444555 = "https://westteam.nulstar.com:3002/http://westteam.nulstar.com"
    # machine1 = "http://public1.pocm.nuls.io"

    #machine4 = "https://cors-proxy.htmldriven.com/?url=http://public2.nuls.io:8004/jsonrpc"