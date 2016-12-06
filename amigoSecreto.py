# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal
"""
import random
import smtplib


def sendemail(from_addr, to_addr_list,
              subject, message,
              login, password,
              smtpserver='smtp.gmail.com:587'):
    header  = 'From: %s\n' % from_addr
    header += 'To: %s\n' % ','.join(to_addr_list)
    header += 'Subject: %s\n\n' % subject
    message = header + message
 
    server = smtplib.SMTP(smtpserver)
    server.starttls()
    server.login(login,password)
    problems = server.sendmail(from_addr, to_addr_list, message)
    server.quit()
    return problems


from_addr    = 'javier@javierpalmaespinosa.cl' 
subj         = 'Amigo Secreto RD -DdC' 
message      = 'Howdy from a python function' 
login        = '' #your gmail account 
password     = ''#your password



file = open('secretos.txt', 'r')
amigos = [[]*2] #array for storing each participant
for line in file:
    amigos.append(line.split(','))

amigos = filter(None, amigos) #remove empty elements


Juego = [[0 for x in range(3)] for y in range(len(amigos))] 

participantes = []          
for i in range(len(amigos)):
    participantes.append(amigos[i][0])
          
          
for i in range(0,len(amigos)):
    Juego[i][0] = amigos[i][0] #name giver
    Juego[i][1] = amigos[i][1].replace('\n','').replace(' ','') #email giver
    
    nombreAmigo = Juego[i][0]
    while(nombreAmigo==Juego[i][0]): #Not giving to himself
        if(len(participantes)!=1):
            nombreAmigo = participantes[random.randint(0,len(participantes)-1)] #take out the paper =)
        else:
            nombreAmigo = participantes[0] #last paper
        Juego[i][2] = nombreAmigo #asign the reciver to the giver
        participantes.pop(participantes.index(nombreAmigo)) #remove paper

#mail redaction

for i in range(0,len(amigos)):
    intro = 'Querid@ %s :\n' %Juego[i][0]
    cuerpo = 'Queremos contarte que para el juego del amigo secreto, te ha tocado regalarle a %s \n' %s Juego[i][2] 
    fin =  'Recuerda que debe ser de un valor de máximo $3000.- y debe ser entregado el día X a las XX\n'
    despedida = 'Que tengas un lindo dia'
    msje = intro + cuerpo + fin + despedida
    sendemail(from_addr, Juegos[i][2],subj, msje,login,password)

    

 
