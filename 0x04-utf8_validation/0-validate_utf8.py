#!/usr/bin/python3
"""An algorithm to validate if data is a valid UTF-8 encoded data"""


def validUTF8(data):
    # Variable to track the number of consecutive leading '1' bits
    num_consecutive_ones = 0

    # Iterate through each integer in the data set
    for byte in data:
        # Check the 8th bit (from the left)
        eighth_bit = (byte & 0b10000000) >> 7

        if num_consecutive_ones == 0:
            # Count consecutive leading '1' bits in the first byte
            while (byte & (0b10000000 >> num_consecutive_ones)) != 0:
                num_consecutive_ones += 1

            # Validate the number of bytes for the current character
            if num_consecutive_ones == 1 or num_consecutive_ones > 4:
                return False

            # Decrement num_consecutive_ones for the current character
            num_consecutive_ones = max(num_consecutive_ones - 1, 0)

        else:
            # For continuation bytes, check if the 8th bit is '1'
            # and the 7th bit is '0'
            if eighth_bit == 1 and ((byte & 0b01000000) >> 6) == 0:
                num_consecutive_ones -= 1
            else:
                return False

    # Check if all characters are validated
    return num_consecutive_ones == 0