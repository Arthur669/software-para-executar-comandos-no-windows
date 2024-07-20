import os
while True:
 print("1- Verificar e reparar arquivos do sistema 2-desligar o computador 3-reiniciar o computador")
 print("4-sair 5- exibir informações sobre a configuração de rede do seu computador")
 print("6- listar os processos em execução no seu computador")
 print("-----------------------------------------------------------------------------------------")
 comandos = input("Digite o número do comando que preferir: ")
 if comandos == "1":
    os.system("sfc /scannow")
    print("-----------------------------------------")
 if comandos == "2":
    os.system("shutdown /s")
    print("-----------------------------------------")
 if comandos == "3":
    os.system("shutdown /r")
    print("-----------------------------------------")
 if comandos == "4":
   exit()
 print("-----------------------------------------")
 if comandos == "5":
    os.system("ipconfig")
    print("-----------------------------------------")
 if comandos == "6":
    os.system("tasklist")
    print("-----------------------------------------")
