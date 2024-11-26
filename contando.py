#Bibliteca para escolha de números aleátorios.
import random  
dado4lados = [1,2,3,4,5,6] 
dado8lados = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
#Escolhendo qual idioma deseja. Usuário precisa digitar um desses idiomas. 
lingua = input('Portugues? English? ¿Espanhol? Francês? :').lower() #lower usado para caso usuário digite com letras  maiúsculas.
#Português.
if lingua == 'portugues':
 print('Você escolheu portugues') 
#Usando o while para repetir a pergunta de qual tipo de dado o usuário deseja. Ou se deseja sair. 
 while True: 
    print('1. 4 LADOS.')
    print('2. 8 LADOS.') 
    print('3.Sair.')
    
    escolha = input('Qual dado deseja :')
    if escolha == '1':
     print(f'Dado de 4 lados. E o número foi:{random.choice(dado4lados)}') 
    if escolha == '2': 
     print(f'Dado de 8 lados e o número foi:{random.choice(dado8lados)}')  
    if escolha == '3':
     print('Saindo.')
     break

#Escolha em inglês.
elif lingua == 'english':
  print('You chose inglês')
  while True: 
   print('1. 4 SIDES.')
   print('2. 8 SIDES.')
   print('3.Exit.')
   
   escolha = input('Qual dado deseja :') 
   if escolha == '1': 
    print(f'The result of data was:{random.choice(dado4lados)}') 
   if escolha == '2': 
    print(f'Dado de 8 lados e o número foi:{random.choice(dado8lados)}') 
   if escolha == '3':
    print('Exiting.')
    break

#Escolha do usuário em espanhol. 
elif lingua == 'espanhol':
  print('Tu elegiste español') 
  while True: 
   print('1. 4 LADOS.')
   print('2. 8 LADOS.') 
   print('3.Para Salir.')

   escolha = input('¿Qué datos quieres? :')
   if escolha == '1':
    print(f'Dados de 4 caras. Y el numero era:{random.choice(dado4lados)}') 
   if escolha == '2': 
    print(f'Dados de 8 caras. Y el numero era:{random.choice(dado8lados)}')  
   if escolha == '3':
    print('Partida.')
    break
#Escolha em francês. 
elif lingua == 'francês': 
  print('Vous avez choisi le français') 
  while True: 
    print('1. 4 CÔTÉS.')
    print('2. 8 CÔTÉS.') 
    print('3.Sortir.') 

    escolha = input('Quelles données souhaitez-vous :')
    if escolha == '1':
     print(f'Dés à 4 faces. Et le numéro était:{random.choice(dado4lados)}') 
    if escolha == '2': 
     print(f'Dés à 8 faces. Et le numéro était:{random.choice(dado8lados)}')  
    if escolha == '3':
     print('Sortie.')
     break
#Caso seja digitado algum idioma inexistente.  
else: 
    print('Lingua desconhecida. Non-existent language. Lenguaje inexistente. Langue inexistante. ')