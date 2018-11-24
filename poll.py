#File poll này để mô tả dữ liệu

from mongoengine import Document, StringField, ListField

class Poll(Document):
    user_input      = StringField()
    input_trans     = StringField()
    symnonyms       = ListField(StringField())
    symnonyms_trans = ListField(StringField())
    url_list        = StringField()
    # code?

