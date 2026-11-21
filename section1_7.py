import random


def message_to_integer_blocks(message, block_size=256):
    data = message.encode('latin-1')

    # pad with zero bytes to a multiple of block_size
    padding = (-len(data)) % block_size
    data += b'\x00' * padding

    return [
        int.from_bytes(data[i:i + block_size], byteorder='big')
        for i in range(0, len(data), block_size)
    ]


def integer_blocks_to_message(blocks, block_size=256):
    data = b''.join(
        n.to_bytes(block_size, byteorder='big')
        for n in blocks
    )

    return data.decode('latin-1')


def test(trials=10000):

    for i in range(trials):
        block_size = random.randint(1, 256)
        message_length = random.randint(0, 2000)

        # generate a random latin-1 message (all values 0-255)
        message = ''.join(
            chr(random.randint(0, 255))
            for _ in range(message_length)
        )

        # encode and decode
        blocks = message_to_integer_blocks(message, block_size)
        recovered = integer_blocks_to_message(blocks, block_size)

        # verify reversibility
        # we may have added extra nulls, so strip these
        assert recovered.rstrip('\x00') == message.rstrip('\x00'), (
            f"Failed!\n"
            f"Original:  {message!r}\n"
            f"Recovered: {recovered!r}\n"
        )

    print(f"Passed {trials} trials")


if __name__ == "__main__":
    test() # it's fast enough
    # FYI: zero padding may add some extra null characters to the decrypted message
