# my_var = 5
# Obs: else-ul nu este bun cfm coding style-ului
# (in loc de print-uri la fiecare ramura)
# Solutie:

# msg = "Nicio conditie nu este respectata"
# if my_var < 6:
#     # msg = "Set instructiuni 1"
#     msg, msg1 = "Set instructiuni 1", my_var;
# elif my_var > 10:
#     msg = "Set instructiuni 2"
# print(msg, my_var)

# De la 0 la n - 1
# for i in range(10):
#     print(f'Set instructiuni {i}')

# variabila = "Ana are mere"
# List comprehension
# lista = [i for i in variabila]
# print(lista)

# for item, value in enumerate(variabila):
#     print(f"{item} => {value}")

# dictionar
# dictionar = {"key1" : "value2", "key2":"value2"}
# La iterare -> doar cheile
# pt chei -> dictionar.keys()
# for key, value in dicionar.items()
# for item in dictionar.items():
#     # print(key, value)
#     item0, item1 = item     # -> pt parametri multiplii de iesire
#     print(item0, item1)

# variabila = (1,)
# Obs: daca pun ',' este tuplu; daca nu, este int (!!! - interviu)
# print(type(variabila))

# Ghilimele simple vs duble
# pt ghilimele in interiorul aceluiasi tip de ghilimele -> escapare cu \
# variabila = "Ana \"are\" mere"
# print(variabila)
