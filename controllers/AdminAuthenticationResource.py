import os

from flask import g, request
from flask_restful import Resource
from marshmallow import ValidationError
from flask_jwt import jwt

from helper import response_message
from schema import AuthenticationSchema
from models import AdminUser


class AdminAuthenticationResource(Resource):

    def post(self):
        data = request.get_json()
        authentication_schema = AuthenticationSchema()

        try:
            validated_data = authentication_schema.load(data)
        except ValidationError as err:
            return response_message(
                'fail',
                400,
                'Validation Error',
                err.messages
            )

        # validate recruiter exists
        admin_user = AdminUser.find_first(**{'email': validated_data['email'].lower()})
        if not admin_user:
            return response_message(
                'fail',
                400,
                'Invalid email or password.'
            )

        if not admin_user.check_password(validated_data['password']):
            return response_message(
                'fail',
                400,
                'Invalid email or password.'
            )

            # generate token
            token_date = datetime.datetime.utcnow()
            payload = {
                "id": admin_user.id,
                "stamp": str(token_date),
                "exp": datetime.datetime.utcnow() + datetime.timedelta(days=1)
            }
            _token = jwt.encode(payload, os.getenv("TOKEN_KEY"), algorithm='HS256').decode('utf-8')

        return response_message(
            'success',
            200,
            'Successfully hit this endpoint',
            _token
        )
