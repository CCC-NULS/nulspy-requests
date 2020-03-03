#!/usr/bin/python3.7

import requests
import json


class SendRequest(object):

    @staticmethod
    def send_request(req):
        the_request = req.prepare()
        session = requests.Session()
        response = session.send(the_request)
        results_d = json.loads(response.text)

        # print("request is: ", str(the_request.body))
        # print()
        return results_d, response.text
