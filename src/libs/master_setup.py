from src.libs.setup_log import SetupLogging
import src.user_inputs.settings_main as settings

import src.user_inputs.sender_etc as sender_etc
import src.user_inputs.receiver_list as receiver_list


def master_setup(machine, cid):
    SetupLogging()
    settings_main_dd = settings.get_settings(machine, cid)
    sender_etc_dd = sender_etc.get_sender_etc_dict(machine)
    receivers = receiver_list.get_receiver_list()
    return settings_main_dd, sender_etc_dd, receivers


def unpack_d(settings_main_dd):
    cid = settings_main_dd.get('cid')
    url3 = settings_main_dd.get('url3')
    url4 = settings_main_dd.get('url4')
    print("cid: ", cid, " url3: ", url3, " url4: ", url4)
    return cid, url3, url4


def unpack_etc(sender_etc_dd):
    sender = sender_etc_dd.get('sender')
    pw = sender_etc_dd.get('pw')
    print("sender: ", sender, " pw: ", pw)
    return sender, pw
