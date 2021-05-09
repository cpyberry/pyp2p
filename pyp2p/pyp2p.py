"""
Copyright 2021 cpyberry
https://github.com/cpyberry/pyp2p

cpyberry
email: cpyberry222@gmail.com
github: https://github.com/cpyberry
"""


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

	def send_int(self, data: int, format_char="I") -> None:
		message = self.create_message.create_message_int(data, format_char)
		self.sock.send(message)

	def send_dict(self, data: dict, encoding="utf-8") -> None:
		message = self.create_message.create_message_dict(data, encoding)
		self.sock.send(message)

	def send_object(self, data: Any) -> None:
		message = self.create_message.create_message_object(data)
		self.sock.send(message)

	def recv_str(self, encoding="utf-8") -> str:
		content = self.recv_content()
		parsed_message = ParseMessage.parse_message_str(content, encoding)
		return parsed_message

	def recv_int(self, format_char="I") -> int:
		content = self.recv_content()
		parsed_message = ParseMessage.parse_message_int(content, format_char)
		return parsed_message

	def recv_dict(self, encoding="utf-8") -> dict:
		content = self.recv_content()
		parsed_message = ParseMessage.parse_message_dict(content, encoding)
		return parsed_message

	def recv_object(self) -> Any:
		content = self.recv_content()
		parsed_message = ParseMessage.parse_message_object(content)
		return parsed_message

	def recv_content(self) -> bytes:
		packed_length = self.sock.recv(struct.calcsize(self.format_char))
		length = struct.unpack(ENDIANNESS + self.format_char, packed_length)[0]
		content = self.sock.recv(length)
		return content
