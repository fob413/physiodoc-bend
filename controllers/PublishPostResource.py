from flask import g, request
from flask_restful import Resource

from helper import token_validation, response_message
from models import Post
from schema import PostSchema


class PublishPostResource(Resource):

    @token_validation
    def post(self, post_id):
        post = Post.get_by_id(post_id)
        if not post or post.admin_user_id != g.user_id:
            return response_message(
                'fail',
                404,
                'Post does not exist'
            )

        if not post.is_published:
            Post.update(
                post, **{
                    'is_published': True
                }
            )

        post_schema = PostSchema()

        return response_message(
            'success',
            200,
            'Post has been published successfully',
            post_schema.dump(post)
        )
