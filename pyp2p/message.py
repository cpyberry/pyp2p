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
