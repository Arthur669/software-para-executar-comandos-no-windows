import os
print("1- Atualizar o Windows")
comandos = input("Digite o número do comando que preferir: ")
if comandos == "1":
    os.system("sfc /scannow")