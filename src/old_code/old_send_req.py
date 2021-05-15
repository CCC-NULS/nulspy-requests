#!/usr/bin/python3.7

import requests
import json


class SendRequest(object):

    @staticmethod
    def send_request(the_request):
        session = requests.Session()
        the_response = session.send(the_request)
        results_d = json.loads(the_response.text)
        return results_d, the_response.text
