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
from BitcoinPayment.settings import STATIC_URL
import os

COIN = BTCTEST


def get_qr_code(address):
    if not os.path.isfile("static_files/wallet/img/" + address + ".png"):
        img = qrcode.make(address)
        path = f"static_files/wallet/img/{address}" + ".png"
        img.save(path)


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
    # Choose strength 128, 160, 192, 224 or 256
    STRENGTH: int = 128  # Default is 128
    # Choose language english, french, italian, spanish, chinese_simplified, chinese_traditional, japanese or korean
    LANGUAGE: str = "english"  # Default is english
    # Generate new entropy hex string
    ENTROPY: str = generate_entropy(strength=STRENGTH)
    # Secret passphrase for mnemonic
    PASSPHRASE: Optional[str] = None  # "meherett"

    # Initialize Bitcoin mainnet HDWallet
    hdwallet: HDWallet = HDWallet(symbol)
    # Get Bitcoin HDWallet from entropy
    hdwallet.from_entropy(
        entropy=ENTROPY, language=LANGUAGE, passphrase=PASSPHRASE
    )
    return hdwallet


def print_information(wallet):
    if HDWallet == type(wallet):
        print(json.dumps(wallet.dumps(), indent=4, ensure_ascii=False))
    else:
        raise Exception("Invalid wallet")