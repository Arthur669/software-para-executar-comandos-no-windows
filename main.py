import subprocess
while True:
 print("1- Verificar e reparar arquivos do sistema")
 comandos = input("Digite o número do comando que preferir: ")
 if comandos == "1":
    subprocess.run(["cmd", "sfc /scannow"])
