from flask import g, request
from flask_restful import Resource
from marshmallow import ValidationError

from helper import token_validation, response_message, validate_input_data
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


class AdminUnitPostResource(Resource):

    @token_validation
    def get(self, post_id):
        post = Post.find_first(**{
                'id': post_id,
                'admin_user_id': g.user_id
            }
        )

        if not post:
            return response_message(
                'fail',
                404,
                'Post does not exist'
            )

        post_schema = PostSchema()

        return response_message(
            'success',
            200,
            'Post retrieved successfully',
            post_schema.dump(post)
        )

    @token_validation
    def put(self, post_id):
        post = Post.find_first(**{
                'id': post_id,
                'admin_user_id': g.user_id,
                'is_published': False
            }
        )

        if not post:
            return response_message(
                'fail',
                404,
                'Post does not exist'
            )

        data = request.get_json()

        keys = [
            'post_image_url',
            'post'
        ]
        if validate_input_data(data, keys):
            return validate_input_data(data, keys)

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

        Post.update(
            post, **validated_data
        )

        return response_message(
            'success',
            200,
            'Successfully updated post'
        )
