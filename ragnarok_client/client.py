import socket
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import dh
from cryptography.hazmat.primitives.kdf.hkdf import HKDF
import json

class ClientSocket:
	""" Generator for Client sided sockets with DH encryption """
	def __init__(self, debug_flag):
		self.__dh = DiffieHellman.DH()
		self.__debug_flag = debug_flag

	def init_diffie_hellman(self, socket):
		""" Initiating diffie-hellman for crypthographical security in the tcp/ip client """
		socket.send("connected".encode())

		# Definiton of starter primes and public secret
		first_step = socket.recv(1024)

		if self.__debug_flag:
			print(first_step)

		# Parsing dh keys in json data for better debugging
		json_data = json.loads(first_step.decode())
		json_data = json_data["dh_key_exchange"]

		self.__dh.base = int(json_data["base"])
		self.__dh.shared_prime = int(json_data["prime"])
		public_secret = int(json_data["public_secret"])

		# Generator for public secret
		calculated_public_secret = str(self.__dh.calculate_public_secret())
		second_step = "{"
		second_step += "\"dh_key_exchange\":"
		second_step += "{"
		second_step += "\"step\": {},".format(2)
		second_step += "\"public_secret\": {}".format(calculated_public_secret)
		second_step += "}}"
		socket.send(second_step.encode())

		# Calculation of shared public secret
		self.__dh.calculate_shared_secret(public_secret)

	def start_client(self, ip):
		""" Initiation of transport layer for a secure connection between client and server
		sock defines the open port in the network """
		# Initiation of transport layer for a secure connection between client and server
		# sock defines the open port in the network
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		try:
			sock.connect((ip, 50000));
			# Key exchange bettween client and server using Diffie-Hellman
			self.init_diffie_hellman(sock)
			print("The secret key is {}".format(self.__dh.key))

		finally:
			# Termination of program
			print("sex")
			sock.close()
