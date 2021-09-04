from flask_restful import Resource

from helper import response_message
from models import Post
from schema import PostSchema


class UnitPostResource(Resource):

    def get(self, post_id):
        post = Post.find_first(**{
                'id': post_id,
                'is_published': True
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
