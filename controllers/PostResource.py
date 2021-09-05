from flask_restful import Resource
from flask import request
from marshmallow import ValidationError

from helper import response_message, get_pagination_data
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


class PostResource(Resource):

    def get(self):
        page = request.args.get('page', 1, type=int)
        per_page = request.args.get('per_page', 10, type=int)

        posts = Post.query.filter(
            Post.is_published==True
        ).paginate(page, per_page)

        post_schema = PostSchema()
        data = []

        for post in posts.items:
            data.append(post_schema.dump(post))

        return response_message(
            'success',
            200,
            'Posts retrieved successfully',
            {
                'posts': data,
                'paginate': get_pagination_data(posts)
            }
        )
