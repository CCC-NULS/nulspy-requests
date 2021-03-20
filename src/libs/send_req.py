#!/usr/bin/python3.7

import requests
import json


class SendRequest(object):

    @staticmethod
    def send_request(req):
        the_request = req.prepare()
        # the_request.set("path_url", 1)
        # the_request.set("path_url", "")
        session = requests.Session()
        the_response = session.send(the_request)
        results_d = json.loads(the_response.text)
        print(the_request.body)
        return results_d, the_response.text

# works  transfer "SPEXdKRT4pz7ZhasM9pTK4fvGrJf8eod5ZqtXa" "SPEXdKRT4trozwzXj5n1d7vZ7NR9QqbUFh4KG7" 1
# SPEXdKRT4pz7ZhasM9pTK4fvGrJf8eod5ZqtXa
