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

	def send_str(self, data: str, encoding="utf-8") -> None:
		message = self.create_message.create_message_str(data, encoding)
		self.sock.send(message)
