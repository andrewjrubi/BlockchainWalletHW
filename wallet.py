import subprocess
import json
from constants import *

def derive_wallets(coin):
    command = f'./derive -g --mnemonic="{mnemonic}" --cols=path,address,privkey,pubkey --format=json --coin="{coin}" --numderive= 3'   
    p = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
    (output, err) = p.communicate()
    p_status = p.wait()
    docs = json.loads(output)
    return docs

coins = {ETH: derive_wallets(ETH), 
         BTCTEST: derive_wallets(BTCTEST)}
print(coins)
