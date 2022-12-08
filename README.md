# Projeto Para Analise de Nepotismo

## Base de dados 

1. nepotismo.csv
2. base_ibge.csv


Na base Nepotismo.csv continha o as colunas Nome,Cargo,Tipo Cargo,cpf,Cidade
Sendo que na coluna nome estava o nome completo da pessoa, e ela continha todos os tipos de cargos juntos

Foi proposto as seguintes etapas pelo Mentor

### 1) Obter os dados de csv em anexo. Demonstrar os tratamentos de dados implementados para atender aos seguintes critérios:

1. Separar os nomes e sobrenomes

2. Adicionar o código do municipio do IBGE 

3. Adicionar a Sigla do Estado

4. Validar a validade dos cpfs e no caso de cpf inválido não considerar o registro na análise


#### Analise Exploratória dos dados

Para alcançar os requisitos propostos primeiro realizamos uma análise exploratória da base de dados fornecida e desenvolvemos o seguinte modelo dimensional para conseguirmos atingir os objetivos com melhores resultados.

Segue o Modelo elaborado:

image.png



Divimos em duas etapas de tratamento, a primeira no código tratamento.ipynb e a segunda no código transformacao.ipynb, descreveresmo com detalhes cada uma delas a seguir.




#### Tratamento



#### Transformação


Na etapa de transformação ja recebemos os dados validados e tratados de qualquer erro de codificação ou valores vazios e nulos, e realizamos as tranformações necessárias para alcançar o modelo Dimensional para analise de nepotismo.








