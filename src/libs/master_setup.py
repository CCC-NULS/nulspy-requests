from src.libs.setup_top import setup_logging
import src.user_inputs.settings_main as settings
import src.user_inputs.sender_etc as sender_etc
import src.user_inputs.receiver_list as receiver_list


def master_setup(machine, cid, urltype='url3'):
    # setup_logging()
    settings_main_dd = settings.get_settings(machine, cid, urltype)
    sender_etc_dd = sender_etc.get_sender_etc_dict(machine)
    receivers = receiver_list.get_receiver_list()
    return settings_main_dd, sender_etc_dd, receivers


def unpack_d(settings_main_dd):
    cid = settings_main_dd.get('cid')
    url = settings_main_dd.get('url')
    print("inside unpack_d:settings_main_dd: cid: ", cid, " url: ", url)
    return cid, url


def unpack_etc(sender_etc_dd):
    sender = sender_etc_dd.get('sender')
    pw = sender_etc_dd.get('pw')
    print("sender: ", sender, " pw: ", pw)
    return sender, pw


def ret_url(self, urltype="url3"):
    url = self.url4
    if urltype == "url3":
        print("url type: 8003")
        url = self.url3
    else:
        print("url type: 8004")
    print("url is: ", url)
    return url
