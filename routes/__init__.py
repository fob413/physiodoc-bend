from flask_restful import Api

# import controllers
from controllers import (
    SampleResource, AdminAuthenticationResource,
    PostResource
)

api = Api()

# add routes
api.add_resource(SampleResource, '/sample', '/sample/')
api.add_resource(AdminAuthenticationResource, '/api/v1/admin/login', '/api/v1/admin/login/')
api.add_resource(PostResource, '/api/v1/post', '/api/v1/post/')
