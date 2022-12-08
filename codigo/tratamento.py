import pandas as pd 
from validate_docbr import CPF

path = '/content/drive/MyDrive/BaseNepotismo/Coleta/nepotismo.csv'

dataset = pd.read_csv(path,sep = ';',encoding='ISO-8859-1')

dataset['Nome'] = dataset['Nome'].replace({',': ' '}, regex=True)
dataset['Nome'] = dataset['Nome'].replace({'-': ' '}, regex=True)
dataset = dataset.replace({'  ': ' '}, regex=True)

dataset = dataset.replace({',':' '}, regex=True)
dataset = dataset.replace({"'":' '}, regex=True)


dataset = dataset.replace({None: ' '}, regex=True)

#Utiliza Regex para pegar o utimo conjunto de caracteres do nome depois do espaço
import re

def retornaSobrenome(nome): 

  Sobrenome = re.search("[^\/]\w+$", nome).group(0)
  #print(Sobrenome)
  return Sobrenome
