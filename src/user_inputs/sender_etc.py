#!/usr/bin/python3.7
# a place to put your lists of accounts, etc.
# usage:  from src.user_inputs.input_singles import AddressSingles;  dict = AddressSingles.get_addresses()


def get_sender_etc_dict(machine):
    sender_etc_d = None
    if machine == 1:
        sender_etc_d = {
            'sender': 'SPEXdKRT4vPJW8DCGUDkGH34Wc6AV9qoWjNhDx',  # owner of contract
            'pw': 'kathy123',
            'buyer': 'SPEXdKRT4nfcKKVqSt1XLdJYMp2H1nwy3oZ1nJ',
            'contract': 'SPEXdKRT4yJrChYu5KfusRJrLMpJ8qRmitSHxe'  # july 22
            }

    elif machine == 0:
        sender_etc_d = {
            'sender': 'TTSETeCA3FWPueNuqEcKUNoxsuKZArhTA7Q2ccZ',
            'pw': 'xyzxyz123',
            'buyer': 'TTSETeCA3FeQmoc3i8393zZV9WWPU5FmMLQs317',
            'contract': 'TTSETeCA3FueL9cKCiDR8vAiRiGVtVCJksEsstM' #?
            }

    return sender_etc_d

