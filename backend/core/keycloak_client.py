from keycloak import KeycloakOpenID
from core.config import APP_CONFIG


keycloak_openid = KeycloakOpenID(
    server_url=APP_CONFIG.KEYCLOAK_SERVER_URL,
    client_id=APP_CONFIG.KEYCLOAK_CLIENT_ID,
    realm_name=APP_CONFIG.KEYCLOAK_REALM,
    client_secret_key=APP_CONFIG.KEYCLOAK_CLIENT_SECRET
)
