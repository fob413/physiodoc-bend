from functools import wraps

from flask import request, g, jsonify
from flask_jwt import jwt

from helper import response_message
from models import AdminUser


def validate_request():
    """ This method validates the Request payload.
    Args
        expected_args(tuple): where i = 0 is type and i > 0 is argument to be
                            validated
    Returns
      f(*args, **kwargs)
    """

    def real_validate_request(f):
        @wraps(f)
        def decorated(*args, **kwargs):
            if not request.json:
                return response_message(
                    'fail',
                    400,
                    'Request must be a valid JSON'
                )
            return f(*args, **kwargs)

        return decorated

    return real_validate_request


def token_validation(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        # check that the Authorization header is set
        authorization_token = request.headers.get('Authorization')
        if not authorization_token:
            response = jsonify({
                "status": "fail",
                "data": {
                    "message": "Bad request. Header does not contain"
                            " authorization token"
                }
            })
            response.status_code = 400
            return response

        # validates the word bearer is in the token
        if 'bearer ' not in authorization_token.lower():
            response = jsonify({
                "status": "fail",
                "data": {
                    "message": "Invalid Token. The token should begin with"
                            " 'Bearer '"
                }
            })
            response.status_code = 400
            return response

        unauthorized_response = jsonify({
            "status": "fail",
            "data": {
                "message": "Unauthorized. The authorization token supplied"
                        " is invalid"
            }
        })
        unauthorized_response.status_code = 401
        expired_response = jsonify({
            "status": "fail",
            "data": {
                "message": "The authorization token supplied is expired"
            }
        })
        expired_response.status_code = 401

        try:
            # extracts token by removing bearer
            authorization_token = authorization_token.split(' ')[1]

            # decode token
            payload = jwt.decode(authorization_token, 'secret',
                                 options={"verify_signature": False})
        except jwt.ExpiredSignatureError:
            return expired_response
        except jwt.InvalidTokenError:
            return unauthorized_response

        expected_payload_format = {
            "id": "user_id"
        }

        # confirm that payload has required keys
        if ("id") not in payload.keys():
            return unauthorized_response
        else:
            # set current user in flask global variable, g
            g.user_id = payload["id"]
            g.current_user = AdminUser.get_by_id(g.user_id)
            g.token_info = payload

            # now return wrapped function
            return f(*args, **kwargs)
    return decorated


def validate_input_data(data, keys, resource=None):
    if not set(list(data.keys())) <= set(keys):
        return response_message(
            'fail',
            400,
            'No invalid field(s) allowed'
        )
