#Caesar cipher
import sys
import string

#nhap chuoi ma hoa
s = raw_input().strip(" ")
#buoc dich chuyen
k = int(raw_input().strip())

#bang ma ascii hoa va thuong
alphabet_lower = string.ascii_lowercase
alphabet_upper = string.ascii_uppercase

length_alpha = len(alphabet_lower)

encrypt_string = list(s)

for i in range(len(s)):
    if s[i].islower():
        index_s = alphabet_lower.index(s[i])
        encrypt_string[i] = alphabet_lower[(index_s + k) % length_alpha]

    if s[i].isupper():
        index_s = alphabet_upper(s[i])
        encrypt_string[i] = alphabet_upper[(index_s + k) % length_alpha]

print " ".join(encrypt_string)
