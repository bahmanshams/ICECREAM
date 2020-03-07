from bottle_jwt import JWTProviderPlugin
from settings import project_secret, jwt_ttl, authentication

jwt_plugin = JWTProviderPlugin(
    keyword='jwt',
    auth_endpoint='/auth',
    backend=authentication,
    fields=('username', 'password'),
    secret=project_secret,
    ttl=int(jwt_ttl)
)
