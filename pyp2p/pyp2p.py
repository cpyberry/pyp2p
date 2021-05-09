import socket
import struct
from typing import Any
from .message import CreateMessage, ParseMessage


ENDIANNESS = ">"


class Pyp2p:
	"""send and receive various objects
	"""

	def __init__(self, sock: socket.socket, format_char="I"):
		self.sock = sock
		self.format_char = format_char
		self.create_message = CreateMessage(format_char)
