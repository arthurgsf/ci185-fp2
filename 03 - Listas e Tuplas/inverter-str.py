txt = "123456"

l1 = list(txt)

txt2 = ""
while len(l1) > 0:
    txt2 += l1.pop()

print(txt2)