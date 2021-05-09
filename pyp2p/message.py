"""
Copyright 2021 cpyberry
https://github.com/cpyberry/pyp2p

cpyberry
email: cpyberry222@gmail.com
github: https://github.com/cpyberry
"""


import json
import pickle
import struct
from typing import Any


ENDIANNESS = ">"


class CreateMessage:
	def __init__(self, format_char="I"):
		"""Stores information to convert to byte length for sending various objects.

		Args:
			format_char (str, optional): Format of struct module for the message length to insert at the beginning. Defaults to "I".
		"""
		self.format = ENDIANNESS + format_char

	def prepend_message_length(self, data: bytes) -> bytes:
		"""add message length

		Args:
			data (bytes): data to which you want to add the message length

		Returns:
			bytes: data with message length prepend
		"""
		length = len(data)
		message = struct.pack(self.format, length) + data
		return message

	def create_message_str(self, data: str, encoding="utf-8") -> bytes:
		data_bytes = data.encode(encoding)
		message = self.prepend_message_length(data_bytes)
		return message

	def create_message_int(self, data: int, format_char="I") -> bytes:
		data_bytes = struct.pack(ENDIANNESS + format_char, data)
		message = self.prepend_message_length(data_bytes)
		return message

	def create_message_dict(self, data: dict, encoding="utf-8") -> bytes:
		message = self.create_message_str(json.dumps(data), encoding)
		return message

	def create_message_object(self, data: Any) -> bytes:
		data_bytes = pickle.dumps(data)
		message = self.prepend_message_length(data_bytes)
		return message


class ParseMessage:
	"""parse recved binary from client or server
	"""

	@staticmethod
	def parse_message_str(data: bytes, encoding="utf-8") -> str:
		parsed_message = data.decode(encoding)
		return parsed_message

	@staticmethod
	def parse_message_int(data: bytes, format_char="I") -> int:
		parsed_message = struct.unpack(ENDIANNESS + format_char, data)[0]
		return parsed_message

	@classmethod
	def parse_message_dict(cls, data: bytes, encoding="utf-8") -> dict:
		parsed_message_str = cls.parse_message_str(data, encoding)
		parsed_message_dict = json.loads(parsed_message_str)
		return parsed_message_dict

	@staticmethod
	def parse_message_object(data: bytes) -> Any:
		parsed_message = pickle.loads(data)
		return parsed_message
