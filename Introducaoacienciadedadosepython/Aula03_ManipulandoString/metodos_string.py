nome = "python"
print(nome.lower())
print(nome.upper())
print(nome.title())

#removendo espaçõs em branco

nome2 = "   Lucas    "
print(nome2.strip())
print(nome2.lstrip())
print(nome2.rstrip())

#junção e centralização

nome3 = "java"
print(nome3.center(10, "*"))
print(".".join(nome3))