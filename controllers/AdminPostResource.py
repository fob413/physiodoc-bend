from flask import g, request
from flask_restful import Resource
from marshmallow import ValidationError

from helper import token_validation, response_message
from schema import PostSchema
from models import Post


class AdminPostResource(Resource):

    @token_validation
    def post(self):
        data = request.get_json()

        post_schema = PostSchema()

        try:
            validated_data = post_schema.load(data)
        except ValidationError as err:
            return response_message(
                'fail',
                400,
                'Validation Error',
                err.messages
            )

        new_post = Post(
            post=validated_data.get('post'),
            admin_user_id=g.user_id,
            post_image_url=validated_data.get('post_image_url', None)
        )

        try:
            new_post.save()
        except:
            return response_message(
                'fail',
                500,
                'Interval Server Error when attempting to save post'
            )

        return response_message(
            'success',
            201,
            'Successfully created post as draft',
            post_schema.dump(new_post)
        )
