import os
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from hdwallet import HDWallet
from hdwallet.symbols import BTC, BTCTEST
from hdwallet import utils
from hdwallet.utils import generate_entropy
from typing import Optional
import json
import qrcode
import shutil
from bit import PrivateKeyTestnet
from BitcoinPayment.settings import STATIC_URL
import os

COIN = BTCTEST


def get_qr_code(address):
    if not os.path.isfile("static_files/wallet/img/" + address + ".png"):
        img = qrcode.make('https://www.blockchain.com/btc-testnet/address/' + address)
        path = f"static_files/wallet/img/{address}" + ".png"
        img.save(path)


def create_raw_transaction(pk, target_address, amount):
    pk = PrivateKeyTestnet(wif=pk)
    try:
        r = pk.send([(target_address, amount, 'btc')])
        return f'{amount} BTC was sent on {target_address}'
    except Exception as ex:
        return ex.args[0]


def create_transaction(mnemonic, target_address, amount):
    wallet = create_wallet_from_mnemonic(mnemonic)
    private_key = wallet.wif()
    return create_raw_transaction(private_key, target_address, amount)


def create_wallet_from_path(path, symbol=COIN):
    # Derivation from path
    wallet = HDWallet(symbol)
    return wallet.from_path(path)


def create_wallet_from_mnemonic(mnemonic, symbol=COIN):
    if utils.is_mnemonic(mnemonic):
        wallet = HDWallet(symbol)
        wallet.from_mnemonic(mnemonic, language="english")
        return wallet
    else:
        raise Exception("Invalid mnemonic")


def create_wallet(symbol=COIN):
    STRENGTH: int = 128  # Default is 128
    LANGUAGE: str = "english"  # Default is english
    ENTROPY: str = generate_entropy(strength=STRENGTH)
    PASSPHRASE: Optional[str] = None  # "meherett"

    hdwallet: HDWallet = HDWallet(symbol)
    hdwallet.from_entropy(
        entropy=ENTROPY, language=LANGUAGE, passphrase=PASSPHRASE
    )
    return hdwallet


def print_information(wallet):
    if HDWallet == type(wallet):
        print(json.dumps(wallet.dumps(), indent=4, ensure_ascii=False))
    else:
        raise Exception("Invalid wallet")