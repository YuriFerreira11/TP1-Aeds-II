
# Manipulação e Organização de Aquivos de Dados


Algoritmo desenvolvido como parte do trabalho do curso CSI104, Algoritmos e Estruturas de Dados II, tendo como objetivo a simulação de sistemas de gerenciamento de banco de dados.

## Objetivo
Compreender as implicações práticas no tamanho dos registros, limitação de blocos e métodos de alocação de dados em disco.
### Funcionalidades
* Geração de alunos: Usando a biblioteca **Faker** do python para criação de dados realistas.
* Blocos: Possui um tamanho máximo definido pelo usuário, sendo gerados em arquivos .dat
* Diferentes estratégias de organização: 1- Registros de tamanho fixo; 2 - Tamanho variável, tendo esse com duas variações, sendo contíguos e espalhados.
* Estatísticas: Exibição do uso dos blocos e eficiência de armazenamento
## Regras de Armazenamento
### 1. Tamanho fixo
* Todos os registros ocupam o mesmo número de bytes.
* Caso um campo não utilize todos bytes, preenche-se com caracteres especiais (#,%,&)
* Cada registro deve ser armazenado integralmente dentro de um único bloco.
### 1. Tamanho Variável
* Tamanho dos registros depende do conteúdo real.
* Quando não couber em um bloco usa-se as duas abordagens: 
#### Sem espalhamento
Movido integralmente ao próximo bloco.
#### Com espalhamento
 Parte do registro gravado no bloco atual, e o restante no bloco

