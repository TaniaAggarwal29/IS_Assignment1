import operator

words = 'B TJNQMF NFTTBHF'
T = 'ETAOINSHRDLCUMWFGYPBVKJXQZ'


def get_key(iteration: int, ch: str) -> int:  # getting the key
    return ord(ch) - ord(T[iteration])


def decryption(message, key):
    decrypted_text = ""
    for ch in message:
        if ch.isspace():
            decrypted_text += " "
        else:
            decrypted_text += chr(((ord(ch) - ord('A') - key) % 26) + ord('A'))  # trying all combinations
    return decrypted_text


def frequency_attack(message: str, attempts: int):
    frequency = {}
    for ch in message:
        if ch in frequency:
            frequency[ch] += 1
        else:
            frequency[ch] = 1

    sorted_x = sorted(frequency.items(), key=operator.itemgetter(1), reverse=True)  # sorting the items

    for i in range(attempts):
        if i == len(sorted_x):
            break
        key = get_key(i, sorted_x[i][0])  # retrieving key
        print(decryption(message, key))   # printing possible message


def main():

    encrypted_word = input("Enter the encrypted message: ")
    attempts = int(input("Enter the number of attempts you wanna try: "))
    print("First {} possible plain texts are : ".format(attempts))
    frequency_attack(encrypted_word, attempts)


if __name__ == '__main__':
    main()
