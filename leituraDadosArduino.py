# -*- coding: utf-8 -*-
"""
Created on Tue Feb 22 13:32:38 2022

@author: hbuzzi
"""

import serial
import json
from datetime import datetime

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

conexao = conectarSerial()

if conexao!="":
    dicionario={} #Dicionário das medições
    cont=0 #Contador de medições
    while cont<10: #Realiza 10 medições
        resposta=conexao.readline() #le a informação escrita pelo println (printline), logo, readline
        dicionario[str(datetime.now())]=[resposta.decode('utf-8')[0:3]]
        #Faz um dicionário onde a identificação é o horário da medição, e o valor é a medição escrita como utf-8 (apenas 3 digítos pq o sensor só le de 100 a 999)
        print(resposta.decode('utf-8')[0:3]) #Printa o valor lido no terminal
        cont+=1 #Aumenta o contator de medições
    with open('Sensor.json', "w") as arq: #Cria um arquivo Sensor para salvar as informações
        json.dump(dicionario, arq) #Salva as informações do sensor
    conexao.close() #Termina a conexão
    print("Conexão encerrada")
else:
    print("Sem portas disponíveis")