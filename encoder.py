import random

def encode(phrase: str) -> list:
    code = []
    key = []
    for letter in phrase:
        o_value = ord(letter)
        num = random.randint(-20, 20)
        n_value = o_value + num
        n_letter = chr(n_value)
        code.append(n_letter)
        key.append(num)

    return [code, key]

def decode(phrase: list, key: list) -> str:
    decoded_phrase = ''
    for k, l in zip(key, phrase):
        o_value = ord(l) - int(k)
        o_letter = chr(o_value)
        decoded_phrase += o_letter
    return decoded_phrase

if __name__ == "__main__":
    x = encode(input('word: '))
    print(x)
    print(decode(list(x[0]), list(x[1])))