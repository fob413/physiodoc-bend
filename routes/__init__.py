from flask_restful import Api

# import controllers
from controllers import (
    SampleResource, AdminAuthenticationResource
)

api = Api()

# add routes
api.add_resource(SampleResource, '/sample', '/sample/')
api.add_resource(AdminAuthenticationResource, '/api/v1/admin/login', '/api/v1/admin/login/')
