"""app.py"""
from flask import Flask, request

APP = Flask(__name__)

#user requests with thier details
REQUESTS = [{'id':1, 'date':'2018-8-12', 'request':'Request1', 'status':'pending', 'user':'josh'},
            {'id':2, 'date':'2018-8-10', 'request':'Request2', 'status':'accepted', 'user':'mary'},
            {'id':3, 'date':'2018-8-9', 'request':'Request3', 'status':'resolved', 'user':'nakki'},
            {'id':4, 'date':'2018-8-1', 'request':'Request4', 'status':'rejected', 'user':'josh'}]

@APP.route('/api/v1/users/requests', methods=['POST'])
def create_new_request():
    """ adds a new request """

    if request.json['request'] and request.json['user']:

        request_to_be_added = {
            'id':5,
            'date':'2018-9-12',
            'request':request.json['request'],
            'status':request.json['status'],
            'user':request.json['user']
        }

        REQUESTS.append(request_to_be_added)
        return "Request added!"

    return "Invalid request"

if __name__ == '__main__':
    APP.run(debug=True)
