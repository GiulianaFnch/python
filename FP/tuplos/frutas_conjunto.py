# criar conjunto com 3 itens
frutas = {"maçã", "banana", "uva"}

# adicionar um item
frutas.add("laranja")

# adicionar vários itens
frutas.update(["manga","pera"])

# remover um item
frutas.remove("banana")

if "maçã" in frutas:
    print("Maçã está no conjunto de frutas.")
print(frutas)
