import json


app_name = r'django_rest_auth_embedded'
base_url = r'/'


with open(app_name + r'/swagger.json', 'r') as swagger_file:
    swagger_paths = json.load(swagger_file)['paths']
end_point = {
    name: {
        'url': path[1:],
        'name': name,
    }
    for name in ('registration',
                 'login',
                 'logout',
                 'auth_info',
                 )
    for path in swagger_paths
    if name == swagger_paths[path]['x-name']
}
