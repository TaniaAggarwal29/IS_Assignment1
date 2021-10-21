def encode(msg, key):
    """
    :param msg: message to be encrypted
    :param key: key to be used to encrypt message
    :return: encrypted message
    """
    # empty string to store encrypted message
    result = ""

    # encryption
    for char in msg:
        if char.isupper():
            result += chr((ord(char) + key - 65) % 26 + 65)
        else:
            result += chr((ord(char) + key - 97) % 26 + 97)

    return result


def decode(msg, key):
    """
    :param msg: message to be decrypted
    :param key: key to be used to be decrypted
    :return: decrypted message
    """
    return encode(msg, 26-key)


# DRIVER CODE
def main():
    # input key
    key = int(input("Enter Key: "))
    
    while True:
        print("\nMENU: \n1. Encode \n2. Decode \n3. Exit")
        choice = input("\nEnter your choice : ")

        if choice == '1':
            msg = input("Enter the message : ")
            en_msg = encode(msg, key)
            print(f"\nEncoded Message : {en_msg}")

        elif choice == '2':
            msg = input("Enter the encoded-message : ")
            d_msg = decode(msg, key)
            print(f"\nDecoded Message : {d_msg}")

        elif choice == '3':
            break

        else:
            print("\nInvalid Choice! Please enter 1 or 2 or 3.")


if __name__ == '__main__':
    main()
