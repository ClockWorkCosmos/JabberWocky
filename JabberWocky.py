import os
import sys
import random as r
import time as t

counter = int(0)
generated_keychr = int(0)
magic_number = int(0)
filename = str("")
encryption_key = str("")
master_key = str("`h_armd[|df{lxvszjxg~{nu^10")
decrypted_content = str("")
encrypted_content = str("")
contents = str("")
pause_rate = float(1.5)

while True:
	for x in range(0, 10):
    		print(" ")

	print(".....................        .....................")
	print("..................    ..:::.    ..................")
	print(".................  ^JP#&&@&#GY!.  ................")
	print("................ :P@@@BP55PG&@@B!  ...............")
	print("............... ^#@@P^.     :J@@@?  ..............")
	print("..............  G@@P    ..    ?@@&: ..............")
	print(".............. ^@@@! ........ :&@@~ ..............")
	print("............   ^@@@^          :&@@!   ............")
	print("........... .~?5@@@5JJJJJJJJJJY@@@5?~. ...........")
	print(".......... ^B@@@@@@@@@@@@@@@@@@@@@@@@G^ ..........")
	print(".........  5@@@@@@@@@@@@@@@@@@@@@@@@@@Y ..........")
	print(".........  5@@@@@@@@@@#Y??Y#@@@@@@@@@@5  .........")
	print(".........  5@@@@@@@@@#:    :#@@@@@@@@@5 ..........")
	print(".........  5@@@@@@@@@&~    ~&@@@@@@@@@5 ..........")
	print(".........  5@@@@@@@@@@@?  ?@@@@@@@@@@@5 ..........")
	print(".........  5@@@@@@@@@@@~  !@@@@@@@@@@@5 ..........")
	print(".........  5@@@@@@@@@@#:::^&@@@@@@@@@@5 ..........")
	print(".........  P@@@@@@@@@@@&&&&@@@@@@@@@@@5 ..........")
	print(".......... ?@@@@@@@@@@@@@@@@@@@@@@@@@@7 ..........")
	print("..........  !PB####################B5~  ..........")
	print("...........   ......................   ...........")
	print(".............                        .............")
	print(" ")
	print("JabberWocky: Secure Storage Locker Utility")
	print("-----------------------------")
	print(" ")
	print("1. Encrypt")
	print("2. Decrypt")
	print("3. Generate New Key")
	print("4. Create Custom Key")
	print("5. Load Key")
	print("6. Exit")
	print(" ")
	
	option = int(input(">> Select: "))
	if option == 1:
		filename = str(input(">> Open: "))

		with open(filename, "r+", encoding="utf-8") as f:
			contents = str(f.read())
			print(contents)

			contents = [*contents]
			encryption_key = [*encryption_key]
			master_key = [*master_key]
			counter = 0
			for x, _ in enumerate(contents):
				contents[x] = ord(contents[x])
				
				encryption_key[counter] = ord(encryption_key[counter])
				master_key[counter] = ord(master_key[counter])
				
				if contents[x] > 127:
					contents[x] = contents[x]
				else:
					encrypted_content += str(chr(contents[x]+encryption_key[counter]+master_key[counter]))
				
				contents[x] = chr(contents[x])
				encryption_key[counter] = chr(encryption_key[counter])
				master_key[counter] = chr(master_key[counter])

				if counter == int(len(encryption_key)) - 1:
					counter = 0
				else:
					counter += 1

			contents = ''.join(contents)
			encryption_key = ''.join(encryption_key)
			master_key = ''.join(master_key)
			
			f.close()

		filename = str(input(">> Save as: "))
		with open(filename, "w+", encoding="utf-8") as f:
			f.write(encrypted_content)
			encrypted_content = ""
			f.close()
	elif option == 2:
		filename = str(input(">> Open: "))

		with open(filename, "r+", encoding="utf-8") as f:
			contents = str(f.read())
			print(contents)
				
			contents = [*contents]
			encryption_key = [*encryption_key]
			master_key = [*master_key]
			counter = 0
			for x, _ in enumerate(contents):
				contents[x] = ord(contents[x])
				
				encryption_key[counter] = ord(encryption_key[counter])
				master_key[counter] = ord(master_key[counter])
				
				if contents[x] <= 1:
					contents[x] = contents[x]
				else:
					if contents[x]-encryption_key[counter] < 0:
						decrypted_content += str(chr(contents[x]))
					else:
						decrypted_content += str(chr(contents[x]-encryption_key[counter]-master_key[counter]))
				
				contents[x] = chr(contents[x])
				encryption_key[counter] = chr(encryption_key[counter])
				master_key[counter] = chr(master_key[counter])

				if counter == int(len(encryption_key)) - 1:
					counter = 0
				else:
					counter += 1

			contents = ''.join(contents)
			encryption_key = ''.join(encryption_key)
			master_key = ''.join(master_key)
			
			f.close()

		filename = str(input(">> Save as: "))
		with open(filename, "w+", encoding="utf-8") as f:
			f.write(decrypted_content)
			decrypted_content = ""
			f.close()
				
	elif option == 3:
		encryption_key = ""

		for x in range(0, 25):
			generated_keychr = r.randint(89, 128)
			encryption_key += chr(generated_keychr)
			
		magic_number = r.randint(0, 10)
		encryption_key += str(magic_number)

		print("Key: ", encryption_key)
		filename = str(input(">> Save as: "))

		encryption_key = [*encryption_key]
		for x, _ in enumerate(encryption_key):
			if ord(encryption_key[x]) > 127:
				encryption_key[x] = ord(encryption_key[x])
			else:
				encryption_key[x] = ord(encryption_key[x]) + 2
			encryption_key[x] = chr(encryption_key[x])
		encryption_key = str(''.join(encryption_key))

		with open(filename, "w", encoding="utf-8") as f:
			f.write(str(encryption_key))
			f.close()

	elif option == 4:
		encryption_key = ""
		encryption_key = str(input(">> Custom key: "))
		filename = str(input(">> Save as: "))

		encryption_key = [*encryption_key]
		for x, _ in enumerate(encryption_key):
			if ord(encryption_key[x]) > 127:
				encryption_key[x] = ord(encryption_key[x])
			else:
				encryption_key[x] = ord(encryption_key[x]) + 2
			encryption_key[x] = chr(encryption_key[x])
		encryption_key = str(''.join(encryption_key))

		with open(filename, "w", encoding="utf-8") as f:
			f.write(str(encryption_key))
			f.close()

	elif option == 5:
		filename = str(input(">> Load key: "))

		with open(filename, "r", encoding="utf-8") as f:
			encryption_key = f.read()
			f.close()

		encryption_key = [*encryption_key]
		for x, _ in enumerate(encryption_key):
			if ord(encryption_key[x]) < 1:
				encryption_key[x] = ord(encryption_key[x])
			else:
				encryption_key[x] = ord(encryption_key[x]) - 2
			encryption_key[x] = chr(encryption_key[x])
		encryption_key = str(''.join(encryption_key))
		print(">> Using: ", encryption_key, " from ", filename)
	elif option == 6:
		break
	else:
		print(">> Error: INVALID SELECTION (1-6)")

	t.sleep(pause_rate)

exit()
	


	
	

