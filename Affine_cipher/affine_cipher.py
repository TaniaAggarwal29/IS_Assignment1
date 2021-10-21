def encrypt(a, b, msg):
    """
    :param a, b: key to be used to encrypt message
    :param msg: message to be encrypted
    :return: encrypted message
    """
    # empty string to store encrypted message
    result = ""

    # encryption
    for char in msg.upper():
        if char != ' ':
            x = ord(char) - ord('A')
            result += chr((a * x + b) % 26 + ord('A'))
        else:
            result += char

    return result


def decrypt(a, b, msg):
    """
    :param a, b: keys to be used to decrypt
    :param msg: decrypted message
    :return: decrypted message
    """
    a_inverse = 0
    result = ""
    for i in range(26):
        if (a * i) % 26 == 1:
            a_inverse = i
            break

    for char in msg:
        if char != " ":
            result += chr((a_inverse * (ord(char) + ord('A') - b) % 26) + ord('A'))
        else:
            result += char

    return result


# DRIVER CODE
def main():
    a = 17
    b = 10
    while True:
        print("\nMENU: \n1. Encode \n2. Decode \n3. Exit")
        choice = input("\nEnter your choice : ")

        if choice == '1':
            msg = input("Enter the message : ")
            en_msg = encrypt(a, b, msg)
            print(f"\nEncoded Message : {en_msg}")

        elif choice == '2':
            msg = input("Enter the encoded-message : ")
            d_msg = decrypt(a, b, msg)
            print(f"\nDecoded Message : {d_msg}")

        elif choice == '3':
            break

        else:
            print("\nInvalid Choice! Please enter 1 or 2 or 3.")


if __name__ == '__main__':
    main()
