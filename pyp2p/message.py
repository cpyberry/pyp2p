import struct


ENDIANNESS = ">"


class CreateMessage:
	def __init__(self, format_char="I"):
		"""Stores information to convert to byte length for sending various objects.

		Args:
			format_char (str, optional): Format of struct module for the message length to insert at the beginning. Defaults to "I".
		"""
		self.format = ENDIANNESS + format_char
