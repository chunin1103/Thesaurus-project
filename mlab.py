import mongoengine

# mongodb://<dbuser>:<dbpassword>@ds024778.mlab.com:24778/project_thesaurus
host = "ds024778.mlab.com"
port = 24778
db_name = "project_thesaurus"
user_name = "chunin1103"
password = "Neji1234!!"


def connect():
    mongoengine.connect(db_name, host=host, port=port, username=user_name, password=password)

def list2json(l):
    import json
    return [json.loads(item.to_json()) for item in l]


def item2json(item):
    import json
    return json.loads(item.to_json())