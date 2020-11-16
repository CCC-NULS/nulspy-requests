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
        print(the_request.body)
        return results_d, response.text

# works  transfer "SPEXdKRT4pz7ZhasM9pTK4fvGrJf8eod5ZqtXa" "SPEXdKRT4trozwzXj5n1d7vZ7NR9QqbUFh4KG7" 1
# SPEXdKRT4pz7ZhasM9pTK4fvGrJf8eod5ZqtXa
