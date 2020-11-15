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
            'contract': 'TTSETeCA3FueL9cKCiDR8vAiRiGVtVCJksEsstM'  # ?
            }

    elif machine > 9:
        sender_etc_d = {
            'sender': 'TTSETeCA3FWPueNuqEcKUNoxsuKZArhTA7Q2ccZ',
            'pw': 'xyzxyz123',
            'buyer': 'TTSETeCA3FWPueNuqEcKUNoxsuKZArhTA7Q2ccZ',
            'contract': '' # ?
            }
    elif machine == 3:
        sender_etc_d = {
            'sender': 'tNULSeBaMpxUVQLW9J3AzbjFsQVRpC5RAnxVKz',  #  tNULSeBaMpxUVQLW9J3AzbjFsQVRpC5RAnxVKz
            'pw': 'kathy123',
            'buyer': 'tNULSeBaMjt1dKbRYDcCv6XDSeEots1Nfr42aM',
            'contract': '',  # ?
            }
    elif machine == 4:  # westteam
        sender_etc_d = {
            'sender': 'SPEXdKRT4wqaQkYBM8bFm9PyyTumB6GgXSQ57G',
            'pw': 'kathy123',
            'buyer': 'SPEXdKRT4wqaQkYBM8bFm9PyyTumB6GgXSQ57G',
            'contract': '',  # ?
        }
    return sender_etc_d

    # receiver_list = ['SPEXdKRT4ja5aFgREi6HhnxcGPyVi8yfpDvSys']  # westteam SPEXdKRT4ja5aFgREi6HhnxcGPyVi8yfpDvSys
       #westteam sender: SPEXdKRT4trozwzXj5n1d7vZ7NR9QqbUFh4KG7


# real accts:
# 'SPEXdKRT4kGmFz68ChyJrcjzFfggb8b1aNyaKh',   *
# 'SPEXdKRT4wqaQkYBM8bFm9PyyTumB6GgXSQ57G',  *
# 'SPEXdKRT4ja5aFgREi6HhnxcGPyVi8yfpDvSys',   *