from functools import wraps

from flask import request

from helper import response_message


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
