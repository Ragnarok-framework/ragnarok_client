from client import client_socket
from argparse import ArgumentParser

class Main:
	def main(self):
		""" Executing parse data """
		parser = ArgumentParser()
		parser.add_argument("-d", "--debug", dest="debug", required=False,
	                    help="to print debug messages, enable this option",
	                    action="store_true"
	                    )

		args = parser.parse_args()

		if args.debug:
		   print(args)
	    server = "localhost"
		client = Client.ClientSocket(args.debug)
		client.start_client(server)
if __name__ == '__main__':
   Main().main()
