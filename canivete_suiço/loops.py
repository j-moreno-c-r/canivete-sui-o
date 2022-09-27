nome = "holland"

print(nome, len(nome))

i = 0

while i < len(nome):
    print(nome[i])
    i +=  1

#versão 1 /\
print(":=" * 35)

for i in range(len(nome)):
    print(nome[i])

#versão 2 /\
print(":=" * 35)

for c in nome:
    print(c)
#versão 3 /\

for c in enumerate(nome):
    print(c)
#versão 4
for  i, c in enumerate(nome):
    print(i, c)
    




