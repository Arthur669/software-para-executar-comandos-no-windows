import os
while True:
 print("1- Verificar e reparar arquivos do sistema 2-desligar o computador 3-reiniciar o computador")
 print("4-sair 5- exibir informações sobre a configuração de rede do seu computador")
 print("6- listar os processos em execução no seu computador 7-limpar a tela")
 print("8-mudar a cor das letras para verde 9-mudar a cor das letras para verde claro")
 print("10-exibir informações detalhadas sobre o sistema operacional e o hardware do seu computador")
 print("11-verificar e corrigir erros no disco rígido ou em uma unidade de armazenamento")
 print("12-abrir o gerenciador de tarefas 13-exibir a versão do Windows instalado no computador")
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
 if comandos == "7":
    os.system("cls")
    print("-----------------------------------------")
 if comandos == "8":
    os.system("color 2")
    print("-----------------------------------------")
 if comandos == "9":
    os.system("color a")
    print("-----------------------------------------")
 if comandos == "10":
    os.system("systeminfo")
    print("-----------------------------------------")
 if comandos == "11":
    os.system("chkdsk")
    print("-----------------------------------------")
 if comandos == "12":
    os.system("taskmgr")
    print("-----------------------------------------")
 if comandos == "13":
    os.system("ver")
    print("-----------------------------------------")
