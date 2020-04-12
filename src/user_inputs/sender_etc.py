#!/usr/bin/python3.7
# a place to put your lists of accounts, etc.
# usage:  from src.user_inputs.input_singles import AddressSingles;  dict = AddressSingles.get_addresses()


def get_sender_etc_dict(machine):
    sender_etc_d = None
    if machine == 1:
        sender_etc_d = {
            'sender': 'TTbKRT4vrHMQdyQCATrdu6godeo1FJWSFVpk',
            'pw': 'nuls123456',
            'buyer': 'TTSETeCA3FWQ3Y32TCFEwJvzqGbxiXNxtkzPb3z',
            'contract': 'TTSETeCA3FWQ3Y32TCFEwJvzqGbxiXNxtkzPb3z'
            }

    elif machine == 0:
        sender_etc_d = {
            'sender': 'TTSETeCA3FWPueNuqEcKUNoxsuKZArhTA7Q2ccZ',
            'pw': 'xyzxyz123',
            'buyer': 'TTSETeCA3FeQmoc3i8393zZV9WWPU5FmMLQs317',
            'contract': 'TTSETeCA3FueL9cKCiDR8vAiRiGVtVCJksEsstM' #?
            }

    return sender_etc_d

