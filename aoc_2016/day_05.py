import hashlib

input = "cxdnnyjw"

password = ["."] * 8
n = 0
found = True

while (found):
	test = input + str(n)
	m = hashlib.md5()
	m.update(bytes(test,"ascii"))
	dig = m.hexdigest()
	if dig[:5] == "00000":
		pos = int(dig[5],16)
		if pos<8:
			if password[pos] == ".":
				password[pos] = dig[6]
				found = ("." in password)
		print("".join(password))
	n += 1