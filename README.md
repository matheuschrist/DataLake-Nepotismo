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


![image](https://user-images.githubusercontent.com/62062407/206534127-637a0763-a866-4755-b2c8-b206ef5250bd.png)


Optamos por organizar a modelagem com uma tabela Fato Central e duas Dimensões seguindo o modelo star schema proposto por Ralph Kimball, devido notarmos que o para locarlizarmos os casos possíveis de Nepotismo era necessario uma relação entre as pessoas que exerciam cargos indicados com as pessoas que exerciam cargos comicionados para isso decidimos separa quem foi indicado para estar na tabela fato e os indicadores na tabela dimensão os correlacionando pelos seus sobrenomes, onde seria identificados possívies casos de nepotismo e as que não houverem relação serão mantidas para meio informativo de quantidade e porcentagem de ocorência por região e Outras métricas que serão possíveis ser analisadas.

 
Para podermos analisarmos os casos por Estados e Municipos oprtamos por manter na tabela Fato apenas o código do IBGE e criarmos uma dimensão Localidade contendo esses campos para analise futura.



Divimos em duas etapas de tratamento, a primeira no código tratamento.ipynb e a segunda no código transformacao.ipynb, descreveresmo com detalhes cada uma delas a seguir.




#### Tratamento

Começamos fazendo a verificação da base de dados, com o comando dataset.describe() conseguir ter um resumo das estatísticas dos dados contidos na base coletada com isso percebemos que não havia valores  duplicados ou nulos, em seguida verificamos os tipos das variáveis armazanadas em busca de problemas de tipagem mas o interorator as indentificou todas como o Tipo Object que Seria o tipo textual em um DataFrame , após fazer esssa verificação e concluido que a base estaca apita para seguir para a próxima etapa foram feitas as alterações necessárias e os dados foram carregados em novos arquivos: dataset_ibge_tratado.csv,dataset_tratado.csv na pasta tratamento



#### Transformação


Na etapa de transformação ja recebemos os dados validados e tratados de qualquer erro de codificação ou valores vazios e nulos, e realizamos as tranformações necessárias para alcançar o modelo Dimensional para analise de nepotismo.

Primeiro realizamos a remoção de caracteres indesejados na base como virgulas, hífem e aspas, removemos também os espaços duplos.
Como foi proposto realizar a validação do CPF utilizamos uma blibliteca (https://pypi.org/project/validate-docbr/) que realiza a validação do CPF e caso ouvesses algum que não fosse válido o removemos do dataset.

Depois utilizamos Regex(expressões regulares) para separar o nome do sobrenome, para evitar problemas de pessoas que possíam nomes compostos como Pedro José por exemplo consideramos como sobrenome apenas o utlimo valor de caracteres no nome completo finalizando a etapa de separação dos nomes e sobrenomes realizamos um JOIN(Junção de duas tabelas) com o dataset base do IBGE para acrescentarmos a nossa base de dados os campos Código do IBGE, Estado e a sigla de cada estado feito isso separamos os esses valores em uma tabela chamada Dim_localidade como proposto no modelo dimensional elaborado deixando apenas a coluna Código do IBGE no nosso dataset que futuramento irá compor a nossa tabela Fact_indicados.
Porém antes realizamos a separação do dataset pelos Tipos de cargos ficando os que possuíam cargos indicados na tabela Fact_indicados e os de cargos Eleitos e Concusados na Dim_indicadores.

Feito essa separação começamos a validação dos possíveis casos de nepotismo , realizamos uma junção das tabelas Fact_indicados e Dim_indicadores pelo Sobrenome e por Cidade visando encontrar apenas os casos que ocorrem dentro das regiões vigentes da pessoa que indicou, para isso o método de junção que traz apenas as intececções contidas nas tabelas seguindo os paramentros passados, assim consigmos encontrar os possíveis casos de nepotismo feito isso criamos uma coluna que indicaria se aquele cadastro possui possível caso de Nepotismo e no outros que não foram encontrados esses requisitos Criamos uma coluna indicando que não possuia Nepotismo, feito toda essa identificação e separação dos cadastros do nosso dataset realizamos a junção das bases separadas para identificação e finalizamos o tratamento da dimensão Dim_indicadores e Fact_indicados para finalizar realizamos o carregamento de todas as tabelas conslídas no diretório porcessamento indicado que todos os dados já foram processados e estão pronto para ser consuimido para serem criados as análises nos mesmos.




### Visualização 

.... EM Construção ...




