from django.shortcuts import render
from django.http import HttpResponse
from account.models import CustomUser
from . import HDwallet
from wallet.models import Wallet
import requests


def index(request):
    user = CustomUser.objects.get(id=request.user.id)
    if not user.has_wallet:
        context = {'has_wallet': user.has_wallet}
        return render(request, '../templates/wallet/wallet.html', context)
    else:
        address = user.wallet.address
        request_str = 'https://api.blockcypher.com/v1/btc/test3/addrs/' + address
        #request_str = 'https://api.blockcypher.com/v1/btc/test/addrs/' + address
        response = requests.get(request_str).json()
        if 'address' in response:
            qr = HDwallet.get_qr_code(address)
            balance = int(response['balance']) / 100000000.0
            unconfirmed_balance = response['unconfirmed_balance'] / 100000000.0
            qr_path = '../../static/wallet/img/' + address + ".png"
            context = {'error': False, 'balance': balance, 'unconfirmed_balance': unconfirmed_balance, 'address': address, 'qr_path': qr_path, 'has_wallet': user.has_wallet}
        else:
            context = {'error': True, 'has_wallet': user.has_wallet}
        return render(request, '../templates/wallet/wallet.html', context)


def create_wallet(request):
    user = CustomUser.objects.get(id=request.user.id)
    if not user.has_wallet:
        wallet = HDwallet.create_wallet()
        wallet_data = Wallet()
        wallet_data.address = wallet.p2pkh_address()
        wallet_data.public_key = wallet.public_key()
        wallet_data.is_activated = True
        wallet_data.save()
        user.wallet = wallet_data
        seed = wallet.mnemonic()
        context = {'seed': seed, 'has_wallet': user.has_wallet}
        user.has_wallet = True
        user.save()
    else:
        context = {'has_wallet': user.has_wallet}
    return render(request, '../templates/wallet/create_wallet.html', context)