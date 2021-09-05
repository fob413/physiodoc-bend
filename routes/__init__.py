from flask_restful import Api

# import controllers
from controllers import (
    SampleResource, AdminAuthenticationResource,
    AdminPostResource, PublishPostResource,
    UnitPostResource, AdminUnitPostResource,
    PostResource
)

api = Api()

# add routes
api.add_resource(SampleResource, '/sample', '/sample/')
api.add_resource(AdminAuthenticationResource, '/api/v1/admin/login', '/api/v1/admin/login/')
api.add_resource(AdminPostResource, '/api/v1/admin/post', '/api/v1/admin/post/')
api.add_resource(AdminUnitPostResource, '/api/v1/admin/post/<string:post_id>', '/api/v1/admin/post/<string:post_id>/')
api.add_resource(PublishPostResource, '/api/v1/admin/publish/<string:post_id>', '/api/v1/admin/publish/<string:post_id>/')
api.add_resource(UnitPostResource, '/api/v1/post/<string:post_id>', '/api/v1/post/<string:post_id>/')
api.add_resource(PostResource, '/api/v1/post', '/api/v1/post/')
