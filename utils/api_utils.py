from pprint import pprint
import utils.api_response_utils as api_response_utils

# Import for creating a new vault account
from fireblocks.models.create_vault_account_request import CreateVaultAccountRequest

# Import for getting API users
from fireblocks.models.get_api_users_response import GetAPIUsersResponse 
from fireblocks.exceptions import ApiException

# Import for transactions
from fireblocks.models.transaction_request import TransactionRequest
from fireblocks.models.destination_transfer_peer_path import DestinationTransferPeerPath
from fireblocks.models.source_transfer_peer_path import SourceTransferPeerPath
from fireblocks.models.transfer_peer_path_type import TransferPeerPathType
from fireblocks.models.transaction_request_amount import TransactionRequestAmount

# Function to retrieve and print paginated vault accounts
def get_vault_accounts(fireblocks):
    try:
        future = fireblocks.vaults.get_paged_vault_accounts()
        api_response = future.result()  # Wait for the response
        print("Response from VaultsApi->get_paged_vault_accounts:\n")
        #pprint(api_response.raw_data)
        #pprint(api_response)
        api_response_utils.beautify_response(api_response)
        return api_response
    except Exception as e:
        print(f"Exception when calling VaultsApi->get_paged_vault_accounts: {e}\n")

def get_api_users(fireblocks):
    """*Lacking Permissions* Get all API users."""
    try:
        # Get Api users
        api_response = fireblocks.api_user.get_api_users()
        api_response = api_response.result()  # Wait for the response
        
        print("The response of ApiUserApi->get_api_users:\n")
        api_response_utils.beautify_response(api_response)
        return api_response
    except Exception as e:
        print("Exception when calling ApiUserApi->get_api_users: %s\n" % e)
        e.
        api_response_utils.handle_exception(e)

def get_users_workspace(fireblocks):
    try:
        # List users
        api_response = fireblocks.users.get_users().result()
        print("The response of UsersApi->get_users:\n")
        api_response_utils.beautify_response(api_response)
        return api_response
    except Exception as e:
        print("Exception when calling UsersApi->get_users: %s\n" % e)

def create_transaction(fireblocks):
    transaction_request: TransactionRequest = TransactionRequest(
        asset_id="ETH",
        amount=TransactionRequestAmount("0.1"),
        source=SourceTransferPeerPath(
            type=TransferPeerPathType.VAULT_ACCOUNT,
            id="0"
        ),
        destination=DestinationTransferPeerPath(
            type=TransferPeerPathType.VAULT_ACCOUNT,
            id="1"
        ),
        note="Your first transaction!"
    )
    # or you can use JSON approach:
    #
    # transaction_request: TransactionRequest = TransactionRequest.from_json(
    #     '{"note": "Your first transaction!", '
    #     '"assetId": "ETH", '
    #     '"source": {"type": "VAULT_ACCOUNT", "id": "0"}, '
    #     '"destination": {"type": "VAULT_ACCOUNT", "id": "1"}, '
    #     '"amount": "0.1"}'
    # )
    try:
        # Create a new transaction
        future = fireblocks.transactions.create_transaction(transaction_request=transaction_request)
        api_response = future.result()  # Wait for the response
        print("The response of TransactionsApi->create_transaction:\n")
        beautify_response(api_response)
        return(api_response)
        # to print just the data:                pprint(api_response.data)
        # to print just the data in json format: pprint(api_response.data.to_json())
    except Exception as e:
        print("Exception when calling TransactionsApi->create_transaction: %s\n" % e)

# Function to create a new vault account
def create_vault_account(fireblocks,vault_name):
    create_vault_account_request: CreateVaultAccountRequest = CreateVaultAccountRequest(
                                    name=vault_name,
                                    hidden_on_ui=False,
                                    auto_fuel=False
                                    )
    try:
        # Create a new vault account
        future = fireblocks.vaults.create_vault_account(create_vault_account_request=create_vault_account_request)
        api_response = future.result()  # Wait for the response
        print("The response of VaultsApi->create_vault_account:\n")
        beautify_response(api_response)
        # to print just the data:                pprint(api_response.data)
        # to print just the data in json format: pprint(api_response.data.to_json())
    except Exception as e:
        print("Exception when calling VaultsApi->create_vault_account: %s\n" % e)