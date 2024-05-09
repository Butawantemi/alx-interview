#!/usr/bin/python3
"""  UTF-8 validation """

def validUTF8(data):
    """
    This function determines if a given data set
    represents a valid UTF-8 encoding.
    """
    # Initialize the number of bytes remaining in the current character sequence
    num_bytes = 0

    # Iterate through each byte in the data
    for byte in data:
        # Ensure each byte is treated as an unsigned 8-bit integer
        byte = byte & 255

        # If we're in the middle of a multi-byte sequence
        if num_bytes > 0:
            # Check if the byte is a continuation byte (starts with '10')
            if not (byte & 0b11000000 == 0b10000000):
                return False
            # Decrease the number of bytes remaining in the sequence
            num_bytes -= 1
        # If this is the start of a new character sequence
        else:
            # Determine the number of bytes in the sequence based on the leading bits
            if byte & 0b10000000 == 0:
                num_bytes = 0
            elif byte & 0b11100000 == 0b11000000:
                num_bytes = 1
            elif byte & 0b11110000 == 0b11100000:
                num_bytes = 2
            elif byte & 0b11111000 == 0b11110000:
                num_bytes = 3
            else:
                return False

    # If there are no incomplete character sequences remaining, the encoding is valid
    return num_bytes == 0
