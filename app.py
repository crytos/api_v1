""" Import flask and modules """
from flask import Flask, request

APP = Flask(__name__)

#user requests with thier details
REQUESTS = [{'id':1, 'date':'2018-8-12', 'request':'Request1', 'status':'pending', 'user':'josh'},
            {'id':2, 'date':'2018-8-10', 'request':'Request2', 'status':'accepted', 'user':'mary'},
            {'id':3, 'date':'2018-8-9', 'request':'Request3', 'status':'resolved', 'user':'nakki'},
            {'id':4, 'date':'2018-8-1', 'request':'Request4', 'status':'rejected', 'user':'josh'}]

@APP.route('/api/v1/users/requests/<request_id>', methods=['PUT'])
def modify_request(request_id):
    """ modifies a request """

    request_to_be_modified = [request for request in REQUESTS if request['id'] == int(request_id)]

    if request_to_be_modified:
        request_to_be_modified[0]['request'] = request.json['request']
        return "Request modified succesfully"

    return "Request not found!"

if __name__ == '__main__':
    APP.run(debug=True)
