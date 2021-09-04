import os

from flask import g, request
from flask_restful import Resource
from marshmallow import ValidationError

from helper import response_message, validate_request
from schema import SampleSchema


class SampleResource(Resource):

    def get(self):
        return response_message(
            'success',
            200,
            'Successfully hit this endpoint'
        )

    @validate_request()
    def post(self):
        data = request.get_json()
        sample_schema = SampleSchema()

        try:
            validated_data = sample_schema.load(data)
        except ValidationError as err:
            return response_message(
                'fail',
                400,
                'Validation Error',
                err.messages
            )

        # run a background service
        from scheduler import sched, say_hi
        sched.add_job(
            say_hi
        )

        return response_message(
            'success',
            200,
            'Successfully hit this endpoint',
            validated_data
        )
