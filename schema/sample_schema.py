from marshmallow import Schema, fields


class SampleSchema(Schema):
    id = fields.Str(dump_only=True)
    sample = fields.Str(
        required=True,
        error_messages={'required': 'sample is required'}
    )
