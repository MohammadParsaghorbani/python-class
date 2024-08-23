chr_list = []
result = []
wra = []
correct = []
charecct= []
cr = ""
wr = ""
char = str(input("chr: "))
for i in char:
    chr_list.append(i)
for i in chr_list:
    result.append(ord(i)*5+6)
for i in result:
    z = i-6
    x = z//5
    correct.append(x)
for i in correct:
    z = chr(i)
    charecct.append(z)
for i in charecct:
    cr += i
for i in result:
    z = chr(i)
    wra.append(z)
for i in wra:
    wr+=i
# print(chr_list)
# print(result)
print(wr)
# print(correct)
# print(charecct)
print(cr)
