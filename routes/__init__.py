from flask_restful import Api

# import controllers
from controllers import (
    SampleResource, AdminAuthenticationResource,
    PostResource, PublishPostResource
)

api = Api()

# add routes
api.add_resource(SampleResource, '/sample', '/sample/')
api.add_resource(AdminAuthenticationResource, '/api/v1/admin/login', '/api/v1/admin/login/')
api.add_resource(PostResource, '/api/v1/post', '/api/v1/post/')
api.add_resource(PublishPostResource, '/api/v1/publish/<string:post_id>', '/api/v1/publish/<string:post_id>/')
