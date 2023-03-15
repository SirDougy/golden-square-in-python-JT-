# def say_hello(name):
#     print(f'hello '+ (name))
#     return "hello " + (name)


# # Intended output:
# #
# # > say_hello("kay")
# # => "hello kay"

# # print(say_hello('kay'))
# # say_hello('kay')


# def factorial(n):
#     product = n
#     #print(f"at the start product is {product}")
#     while n > 1:
#         n -= 1
#         #print(f"we multiply {product} by {n}")
#         product *= n
#         #print(f"we get {product}")

#     return product

# print(f"""
# Running: factorial(5)
# Expected: 120
# Actual: {factorial(5)}
# """)


def encode(text, key):
    cipher = make_cipher(key)

    ciphertext_chars = []
    for i in text:
        ciphered_char = chr(65 + cipher.index(i))
        ciphertext_chars.append(ciphered_char)

    return "".join(ciphertext_chars)


def decode(encrypted, key):
    cipher = make_cipher(key)

    plaintext_chars = []
    for i in encrypted:
        plain_char = cipher[65 - ord(i)]
        plaintext_chars.append(plain_char)

    return "".join(plaintext_chars)


def make_cipher(key):
    alphabet = [chr(i + 98) for i in range(1, 26)]
    cipher_with_duplicates = list(key) + alphabet

    cipher = []
    for i in range(0, len(cipher_with_duplicates)):
        if cipher_with_duplicates[i] not in cipher_with_duplicates[:i]:
            cipher.append(cipher_with_duplicates[i])

    return cipher

# When you run this file, these next lines will show you the expected
# and actual outputs of the functions above.
print(f"""
 Running: encode("theswiftfoxjumpedoverthelazydog", "secretkey")
Expected: EMBAXNKEKSYOVQTBJSWBDEMBPHZGJSL
  Actual: {encode('theswiftfoxjumpedoverthelazydog', 'secretkey')}
""")

print(f"""
 Running: decode("EMBAXNKEKSYOVQTBJSWBDEMBPHZGJSL", "secretkey")
Expected: theswiftfoxjumpedoverthelazydog
  Actual: {decode('EMBAXNKEKSYOVQTBJSWBDEMBPHZGJSL', 'secretkey')}
""")




print(f"""
 Running: factorial(3)
Expected: 6
  Actual: {factorial(3)}
""")

print(f"""
 Running: factorial(7)
Expected: 5040
  Actual: {factorial(7)}
""")

