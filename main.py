from fireblocks.client import Fireblocks
from fireblocks.client_configuration import ClientConfiguration
from fireblocks.base_path import BasePath
from dotenv import load_dotenv
import os

import utils.api_utils as api_utils

def load_env_variables():
    """Load environment variables from the .env file and return them."""
    load_dotenv()
    base_path = os.getenv("FIREBLOCKS_BASE_PATH")
    api_key = os.getenv("FIREBLOCKS_API_KEY")
    secret_key_path = os.getenv("FIREBLOCKS_SECRET_KEY_PATH")
    
    # Display environment variables for verification
    print(f"Base Path: {base_path}")
    print(f"API Key: {api_key}")
    print(f"Secret Key Path: {secret_key_path}")
    
    return base_path, api_key, secret_key_path

def load_secret_key(secret_key_path):
    """Load secret key from the specified file path."""
    with open(secret_key_path, 'r') as key_file:
        secret_key = key_file.read()
    return secret_key

def build_client_configuration(api_key, secret_key, base_path):
    """Build and return the client configuration."""
    configuration = ClientConfiguration(
        api_key=api_key,
        secret_key=secret_key,
        base_path=BasePath.Sandbox  # or directly use a string URL like "https://sandbox-api.fireblocks.io/v1"
    )
    return configuration

if __name__ == "__main__":
    base_path, api_key, secret_key_path = load_env_variables()
    secret_key = load_secret_key(secret_key_path)
    configuration = build_client_configuration(api_key, secret_key, base_path)

    with Fireblocks(configuration) as fireblocks:
        # api_utils.get_vault_accounts(fireblocks)
        # create_vault_account(fireblocks,"First SDK Vault")
        # accounts_list = api_utils.get_vault_accounts(fireblocks)
        # print(accounts_list)
        #api_utils.create_transaction(fireblocks)
    

        ### Lacking permissions for the following
        api_utils.get_api_users(fireblocks)
        #beautify_api_response(api_utils.get_users_workspace(fireblocks))