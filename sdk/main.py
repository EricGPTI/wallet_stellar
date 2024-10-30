#from utils import get_faucet, get_ledger_by_sequence, get_transaction_by_hash
#from wallet import create_eric_wallet, create_bob_wallet
#from transfer import transfer_from
from stellar_sdk import Server, Keypair


print("# Start Payment from Eric to Bob with Amount 100XML")

print("# Configure the server for the Standalone network (local)")
server = Server(horizon_url="http://localhost:8085")


def create_eric_wallet():
    print("# Criando a carteira de Eric!")
    eric_keys = Keypair.random()
    print(f"Public Key: + {eric_keys.public_key}")
    print(f"Secret: + {eric_keys.secret}")

ERIC = create_eric_wallet()
