s1 = input()
s2 = input()

maior = ""
menor = ""
if len(s1) > len(s2):
    maior = s1
    menor = s2
else:
    maior = s2
    menor = s1

s3 = []

for i in range(len(maior)):
    s3.append(s1[i])
    s3.append(s2[i])

print(str.join("", s3))