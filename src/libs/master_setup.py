import src.user_inputs.settings_main as settings
import src.user_inputs.sender_etc as sender_etc
import src.user_inputs.receiver_list as receiver_list


def master_setup(machine, tchain_id, urltype='url3'):
    # setup_logging() here
    settings_main_dd = settings.target_setup(machine, tchain_id, urltype)
    sender_etc_dd = sender_etc.get_sender_etc_dict(machine)
    receivers = receiver_list.get_receiver_list()
    return settings_main_dd, sender_etc_dd, receivers

