
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
### - Tamanho fixo
* Todos os registros ocupam o mesmo número de bytes.
* Caso um campo não utilize todos bytes, preenche-se com caracteres especiais (#,%,&)
* Cada registro deve ser armazenado integralmente dentro de um único bloco.
### - Tamanho Variável
* Tamanho dos registros depende do conteúdo real.
* Quando não couber em um bloco usa-se as duas abordagens: 
#### Sem espalhamento
Movido integralmente ao próximo bloco.
#### Com espalhamento
 Parte do registro gravado no bloco atual, e o restante no bloco
## Saída esperada: 
Digite o tamanho máximo do bloco (em bytes): 500\
Quantos alunos gerar: 10\
1 - Tamanho fixo 2 - Tamanho variável: 1\
Bloco 0: 360 bytes (72.0%)   
Bloco 1: 360 bytes (72.0%)   
Bloco 2: 360 bytes (72.0%)   
Bloco 3: 360 bytes (72.0%)   
Bloco 4: 360 bytes (72.0%)   

Total de blocos: 5\
Blocos parcialmente usados: 5\
Eficiência total: 72.0%      
