# -*- coding: utf-8 -*-
"""
Created on Tue Feb 22 12:50:01 2022

@author: hbuzzi
"""

import serial

def conectarSerial(conexao = "Default"):
    if conexao == "Default": #Caso o usuário não saiba a porta que está conectado o arduíno
        for porta in range(10): #Percorre as 10 portas Serial do sistema operacional
            try: #tenta
                conexao = serial.Serial("COM"+str(porta), 115200, timeout=0.5) #No windows é COM1, COM2, etc..., então ele tenta criar a conexao Serial com a porta usando baud 115200
                print("Conectado na porta:", conexao.portstr) #Printa a conexão se der certo
                break #Sai do Loop pois já encontrou o Arduino
            except serial.SerialException:
                pass
    elif (conexao > 0 and conexao <10): #Se o usuário já fornecer o número da Porta
        conexao = serial.Serial("COM"+str(conexao), 115200, timeout=0.5)
        print("Conectado na porta:", conexao.portstr) #Printa a conexão se der certo
    return conexao #Retorna a conexao

conexao= conectarSerial()
    
if conexao!="": #Se tem conexão
    acao=input("Digite:\n<L> para Ligar\n<D> para Desligar:").upper() #Entrada do usuário
    while acao=="L" or acao=="D":
        if acao=="L":
            conexao.write(b'1') #Manda o binário 1 para acender o LED
        else:
            conexao.write(b'0') #Manda o binário 0 para apagar o LED
        acao = input("Digite:\n<L> para Ligar\n<D> para Desligar:").upper() #Pega um novo input do usuário
    conexao.close() #Se ele escolher algo fora de L e D sai do programa, logo fecha a conexao
    print("Conexao encerrada")
else:
    print("Sem portas disponíveis")