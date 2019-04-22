"""AWS view module."""
import nexmo
import json
import urllib
import logging
import validatesns
from flask import Blueprint, request
from flask import current_app as app

from notifyme.responses import success_response, error_response

aws_blueprint = Blueprint('aws', __name__)

@aws_blueprint.route('/alert', methods=['POST'])
def alert():
    """
    Recieves alert from AWS SNS topic
    """
    # logging.debug("Request Headers %s", request.headers)
    data = request.get_json(force=True)
    # logging.debug(data)

    try:
        validatesns.validate(data)
    except validatesns.ValidationError as err:
        return error_response(dict(code=403, message=err.args))

    client = nexmo.Client(key=app.config['NEXMO_KEY'], secret=app.config['NEXMO_SECRET'])
    if data['Type'] == 'Notification':
        client.send_message({
            'from': app.config['NEXMO_FROM'],
            'to': app.config['NEXMO_TO'],
            'text': '\n'.join([data['Subject'], data['Message']]),
        })

    if data['Type'] == 'SubscriptionConfirmation':
        urllib.request.urlopen(data['SubscribeURL']).read()
        client.send_message({
            'from': app.config['NEXMO_FROM'],
            'to': app.config['NEXMO_TO'],
            'text': 'Subscribed to ' + data['TopicArn'],
        })

    # if data['Type'] == 'UnsubscribeConfirmation':
    #     pass         

    return success_response()

