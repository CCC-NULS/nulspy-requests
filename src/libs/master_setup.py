from src.libs.setup_log import SetupLogging
# from src.libs.setup_top import get_top
# from src.libs.send_req import SendRequest
import src.user_inputs.settings_main as settings

import src.user_inputs.sender_etc as sender_etc
import src.user_inputs.receiver_list as receiver_list


def master_setup(machine):
    SetupLogging()
    settings_d = settings.get_settings(machine)
    sender_etc_dd = sender_etc.get_sender_etc_dict(machine)
    receivers = receiver_list.get_receiver_list()
    return settings_d, sender_etc_dd, receivers


def unpack_d(settingsd, sender_etc_dd):
    chain = settingsd.get('chain')
    url3 = settingsd.get('url3')
    # sender = sender_etc_dd.get('tNULSeBaMjt1dKbRYDcCv6XDSeEots1Nfr42aM')
    # pw = sender_etc_dd.get('dev123dev')
    sender = sender_etc_dd.get('sender')
    pw = sender_etc_dd.get('pw')
    print("sender: ", sender)
    # print("url3: ", url3)
    print("chain: ", chain)
    print("pw: ", pw)
    return chain, url3, sender, pw
