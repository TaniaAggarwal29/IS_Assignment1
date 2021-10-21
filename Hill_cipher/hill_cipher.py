key_matrix = [[0] * 2 for i in range(2)]
inverse_key_matrix = [[0] * 2 for i in range(2)]


def get_key_matrix(key):
    """
    :param key: key to be used for encryption
    :return: nothing. update global key_matrix

    Function creates a matrix from the key
    """
    k = 0
    for i in range(2):
        for j in range(2):
            key_matrix[i][j] = ord(key[k]) % 65
            k += 1


def get_inverse_key_matrix():
    """
    :return: nothing. updates the global inverse_key_matrix

    Function finds the modulo 26 inverse of the key_matrix
    """
    global inverse_key_matrix
    det = (key_matrix[0][0] * key_matrix[1][1] - key_matrix[0][1] * key_matrix[1][0]) % 26
    for i in range(26):
        if (det * i) % 26 == 1:
            det = i
            break
    inverse_key_matrix = [[key_matrix[1][1] * det % 26, -1 * key_matrix[0][1] * det % 26],
                          [-1 * key_matrix[1][0] * det % 26, key_matrix[0][0] * det % 26]]


def encrypt(msg):
    """
    :param msg: message to be encrypted
    :return: encrypted message
    """
    # string to store the encrypted message
    result = ""
    # remove white spaces
    msg = msg.replace(" ", "")

    # to make the message even-length
    if len(msg) % 2 != 0:
        msg += "0"

    k = 0
    # encryption
    while k < len(msg):
        vector = [ord(msg[k]) - ord('A') + 1, ord(msg[k + 1]) - ord('A') + 1]
        k += 2
        vector = [(key_matrix[0][0] * vector[0] + key_matrix[0][1] * vector[1]) % 26,
                  (key_matrix[1][0] * vector[0] + key_matrix[1][1] * vector[1]) % 26]
        cipher_text = [chr(vector[i] + ord('A') - 1) for i in range(2)]
        result += ''.join(cipher_text)
    return result


def decrypt(msg):
    """
    :param msg: message to be decrypted
    :return: decrypted message
    """

    # empty string to store decrypted message
    result = ""
    if len(msg) % 2 != 0:
        msg += "0"
    k = 0

    # decryption
    while k < len(msg):
        vector = [ord(msg[k]) - ord('A') + 1, ord(msg[k + 1]) - ord('A') + 1]
        k += 2
        vector = [(inverse_key_matrix[0][0] * vector[0] + inverse_key_matrix[0][1] * vector[1]) % 26,
                  (inverse_key_matrix[1][0] * vector[0] + inverse_key_matrix[1][1] * vector[1]) % 26]
        cipher_text = [chr(vector[i] + ord('A') - 1) for i in range(2)]
        result += ''.join(cipher_text)

    return result


def main():
    key = 'BBBC'
    get_key_matrix(key)
    get_inverse_key_matrix()

    while True:
        print("\nMENU: \n1. Encode \n2. Decode \n3. Exit")
        choice = input("\nEnter your choice : ")

        if choice == '1':
            msg = input("Enter the message : ")
            en_msg = encrypt(msg.upper())
            print(f"\nEncoded Message : {en_msg}")

        elif choice == '2':
            msg = input("Enter the encoded-message : ")
            d_msg = decrypt(msg.upper())
            print(f"\nDecoded Message : {d_msg}")

        elif choice == '3':
            break

        else:
            print("\nInvalid Choice! Please enter 1 or 2 or 3.")


if __name__ == '__main__':
    main()
