# Projeto Para Analise de Nepotismo

## Integrantes

Alyson Vargas \
Carlos\
Diogo dos Santos Freires\
João Victor Fritoli\
Matheus Christ de Andrade\
Patrick\
Rafael da Silva Lopes


## Base de dados 

1. nepotismo.csv
2. base_ibge.csv

Na base nepotismo.csv continha as colunas Nome, Cargo, Tipo, CPF e Cidade, no entanto, a coluna nome apresentava o nome e sobrenome da pessoa de maneira concatenada separadas por um espaço, a base fornecida também vinha com todos os tipos de cargos juntos

Tendo em vista disso, foi proposto as seguintes etapas pelo mentor

### 1) Obter os dados de csv em anexo. Demonstrar os tratamentos de dados implementados para atender aos seguintes critérios:

1. Separar os nomes e sobrenomes

2. Adicionar o código do municipio do IBGE 

3. Adicionar a Sigla do Estado

4. Validar a validade dos cpfs e no caso de cpf inválido não considerar o registro na análise

#### Analise Exploratória dos dados

Para alcançar os requisitos propostos primeiro realizamos uma análise exploratória da base de dados fornecida e desenvolvemos o seguinte modelo dimensional com o intuito de atingir os objetivos com melhores resultados.

Segue o Modelo elaborado:

![image](https://user-images.githubusercontent.com/62062407/206534127-637a0763-a866-4755-b2c8-b206ef5250bd.png)

Optamos em organizar a modelagem com uma tabela fato central e duas tabelas dimensões seguindo o modelo Star Schema proposto por Ralph Kimbal pois notamos que para encontrar os possíveis casos de Nepotismo era necessário uma relação entre as pessoas que exerciam cargos indicados com as pessoas que exerciam cargos comissionados para isso decidimos separar quem foi indicado para está na tabela fato e os indicadores na tabela dimensão os correlacionando pelo seus sobrenomes onde seriam identificados possíveis casos de nepotismo e as que não houve relação serão mantidas para meio informativo de quantidade e porcentagem de ocorrência por região e outras métricas que serão possíveis ser analisadas.

Para poder analisar os casos por estados e municípios optamos por manter na tabela fato apenas o código do IBGE e criamos uma dimensão Localidade contendo esses campos para análise futura.

O tratamento foi dividido em duas etapas, a primeira etapa no código tratamento.ipynb e a segunda no código transformação.ipynb, essas etapas serão descritas com mais detalhes nos tópicos abaixo.

#### Tratamento

Começamos fazendo a verificação da base de dados, com o comando dataset.describe() foi possível obter um resumo das estatísticas dos dados contidos na base coletada com isso percebemos que não havia valores duplicados ou nulos, em seguida verificamos os tipos das variáveis armazenadas em busca de problemas de tipagem mas o interorator as identificou todas como o tipo Object que seria o tipo textual em um DataFrame, após fazer essa verificação e concluído que a base estava apta para seguir para a próxima etapa foram feitas as alterações necessárias e os dados foram carregados em novos arquivos: dataset_ibge_tratado.csv,dataset_tratado.csv na pasta tratamento.

#### Transformação

Na etapa de transformação já recebemos os dados validados e tratados de quaisquer erros de codificação, valores vazios ou valores nulos, realizamos as transformações necessárias para alcançar o modelo dimensional para análise de nepotismo.

Primeiro realizamos a remoção de caracteres indesejados na base como virgulas, hífen e aspas, removemos também os espaços duplos. Como foi proposto realizar a validação do CPF utilizamos uma biblioteca do python (https://pypi.org/project/validate-docbr/) que foi responsável pela validação do CPF e em casos onde o CPF não foi válido ele foi removido do dataset.

Depois utilizamos Regex, que são expressões regulares, para separar o nome do sobrenome com o intuito de evitar problemas de pessoas que possuíam nomes compostos como Pedro José por exemplo, consideramos como sobrenome o último valor de caracteres no nome completo. Finalizando a etapa de separação dos nomes e sobrenomes realizamos um JOIN, junção entre duas tabelas, com o dataset base do IBGE para acrescentarmos a nossa base de dados os campos Código do IBGE, Estado e a Sigla de cada estado feito isso separamos esses valores em uma tabela chamada Dim_localidade como proposto no modelo dimensional elaborado deixando apenas a coluna Código do IBGE no nosso dataset que futuramente irá compor a nossa tabela Fact_indicados. Porém antes realizamos a separação do dataset pelos Tipos de cargos ficando os que possuíam cargos indicados na tabela Fact_indicados e os de cargos Eleitos e Concursados na Dim_indicadores.

Feito essa separação começamos a validação dos possíveis casos de nepotismo, realizamos uma junção das tabelas Fact_indicados e Dim_indicadores pelo Sobrenome e por Cidade visando encontrar apenas os casos que ocorrem dentro das regiões vigentes da pessoa que indicou, para isso o método de junção que traz apenas as intersecções contidas nas tabelas seguindo os parâmetros passados, assim conseguimos encontrar os possíveis casos de nepotismo feito isso criamos uma coluna responsável por indicar se aquele cadastro possui possível caso de Nepotismo, em outros casos onde não foram encontrados os requisitos para ocorrência de Nepotismo criamos uma coluna indicando que não possuía Nepotismo, feito toda essa identificação e separação dos cadastros do nosso dataset realizamos a junção das bases separadas para identificação e finalizamos o tratamento da dimensão Dim_indicadores e Fact_indicadores. 

Para finalizar realizamos o carregamento de todas as tabelas concluídas no diretório de processamento indicando que todos os dados foram processados e estão prontos para serem consumidos e para criar a análise deles.

### Visualização 

Com base na disponibilização dos dados e no tratamento obtido foi utilizado o Power BI como ferramenta de visualização, optamos por utilizar no DashBoard um mapa que é capaz de mostra as localidades onde há casos possíveis de nepotismo.

Utilizamos também um gráfico de barras onde ele traz informações de quantidade de nepotismo por Estados, utilizamos também quatro cartões que são responsáveis por trazer informações resumidas de casos de nepotismo como quantidade total e estado com mais casos de nepotismo.

Resultado obtido: 

![image](https://user-images.githubusercontent.com/70177188/207368747-68308966-af8b-40ef-a654-20013c57040d.png)

