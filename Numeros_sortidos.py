#Biblioteca slepp para dar o efeito de espera
#Biblioteca tqdm(efeito de carregamento)

from time import sleep
from tqdm import tqdm
import time

nome = input("Digite o seu nome:")
print(f"Seja Bem Vindo {nome}!, Iniciando o programa, Aguarde...;")
sleep(3)
for i in tqdm(range(10)):
    time.sleep(0.5)

import random

numeros = random.sample(range(1,60),12)
print(f'Os Seus números da Sorte são: {numeros}')