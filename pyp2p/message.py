import json
import struct


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
		message = self.create_message_str(json.dumps(data))
		return message
