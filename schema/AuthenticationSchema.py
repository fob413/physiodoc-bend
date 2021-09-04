from marshmallow import Schema, fields


class AuthenticationSchema(Schema):
    email = fields.Str(
        required=True,
        error_messages={'required': 'email is required'}
    )

    password = fields.Str(
        required=True,
        error_messages={'required': 'password is required'},
        load_only=True
    )
