#!/usr/bin/env python3

import random


def Encrypt(E, N, plaintext):
    Cipher = [(ord(char) ** E) % N for char in plaintext]
    return Cipher


def Decrypt(D, N, ciphertext):
    Plain = [chr((char ** D) % N) for char in ciphertext]
    return Plain


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


def prime_finder():
    num = random.randrange(10, 100)
    for i in range(2, num):
        if num % i == 0:
            return prime_finder()
    return num


P = prime_finder()
Q = prime_finder()
N = P * Q
Phi = (P - 1) * (Q - 1)

public_keys = []
for i in range(2, Phi):
    if gcd(i, Phi) == 1 and gcd(i, N) == 1:
        public_keys.append(i)
    if len(public_keys) >= 100:
        break

E = random.choice(public_keys)
del (public_keys)

private_keys = []
i = 2

while len(private_keys) < 5:
    if i * E % Phi == 1:
        private_keys.append(i)
    i += 1

D = random.choice(private_keys)
del (private_keys)

print(f"Public Key:({E}, {N})\nPrivate Key: ({D}, {N})")

messege = input("Enter The messege you want to send: ").strip()

Ciphertext = Encrypt(E, N, messege)
Plaintext = Decrypt(D, N, Ciphertext)

print("OriginalMessage---------->", messege)
print("Ciphertext     ---------->", "".join(map(chr, Ciphertext)))
print("Plaintext      ---------->", ''.join(Plaintext))