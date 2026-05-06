#!/usr/bin/env python3
resultat = ""

for i in range(97, 123):

    if i == 101 or i == 113:
        continue

    resultat += chr(i)

print(resultat)
