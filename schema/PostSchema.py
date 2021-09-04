from marshmallow import Schema, fields


class PostSchema(Schema):
    id = fields.Str(dump_only=True)

    post_image_url = fields.Str()

    post = fields.Str(
        required=True,
        error_messages={'required': 'post is required'}
    )

    is_published = fields.Boolean(dump_only=True)

    created_at = fields.DateTime(dump_only=True)

    modified_at = fields.DateTime(dump_only=True)
