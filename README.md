Arthur Bergami Lucas (570679), Davi Martins Herculano (572699), Felipe Braga Terzella(573529), Marcos Vinícios Corrêa dos Santos(571080), Victor Lopes Tavares da Fonseca (571315)

# Motor Lógico tf3

## Descrição do Projeto

Este projeto foi desenvolvido em Python com o objetivo de simular um **motor lógico para gerenciamento e agendamento de peneiras esportivas para a Pelé academia**.

O sistema permite que jogadores realizem cadastro, escolham suas posições em campo, acompanhem o status de suas convocações e visualizem informações sobre as peneiras nas quais foram escalados.

Além disso, funcionários autorizados podem criar novas peneiras, definir informações do evento e gerar automaticamente equipes masculinas e femininas com base nos jogadores cadastrados e suas respectivas posições.

---

## Objetivo

Automatizar o processo de:

* Cadastro de jogadores;
* Autenticação de usuários;
* Escolha de posição em campo;
* Agendamento de peneiras;
* Formação automática de equipes;
* Consulta de convocações e informações da peneira.

---

## Tecnologias Utilizadas

* Python 3
* Estruturas de dados com dicionários
* Funções
* Estruturas condicionais (`if`, `match-case`)
* Laços de repetição (`while`, `for`)

---

# Funcionalidades do Sistema

## Área do Jogador

### 1. Criar Conta

O jogador pode criar uma conta informando:

* Nome
* CPF
* Gênero biológico
* Senha

Após o cadastro, seus dados ficam armazenados em memória durante a execução do programa.

---

### 2. Login

Após criar a conta, o jogador pode realizar login utilizando:

* CPF
* Senha

---

### 3. Escolher Posição

Após o login, o jogador pode selecionar sua posição em campo.

Posições disponíveis:

1. Goleiro
2. Zagueiro
3. Lateral
4. Ala
5. Volante
6. Meio campo
7. Meia atacante
8. Ponta
9. Centro avante

O sistema permite alterar a posição posteriormente mediante confirmação.

---

### 4. Consultar Status da Peneira

O jogador pode verificar:

* Nome
* CPF
* Posição escolhida
* Se foi convocado para alguma peneira
* Local da peneira
* Data
* Horário
* Time em que foi escalado

---

## Área do Funcionário

Funcionários possuem acesso administrativo para gerenciamento das peneiras.

### Login de Funcionário

Credenciais disponíveis para testes:

#### Funcionário 1

**Login:** Claudio

**Senha:** 12345

#### Funcionária 2

**Login:** Ana

**Senha:** Abacate

---

## Funcionalidades do Funcionário

### 1. Agendar Peneira

O funcionário informa:

* Data da peneira
* Horário de início
* Horário de término
* Quantidade de jogos masculinos
* Quantidade de jogos femininos
* Local do evento

Após o cadastro, o sistema cria automaticamente uma nova peneira.

---

### 2. Visualizar Peneiras

Permite consultar:

* Local
* Data
* Horários
* Times gerados
* Jogadores escalados
* Vagas em aberto

Quando não houver jogador disponível para determinada posição, o sistema exibe:

```
EM FALTA DE JOGADOR
```

---

# Formação Automática dos Times

O sistema gera automaticamente equipes masculinas e femininas.

Para cada time criado, são buscados jogadores que:

* Possuam o gênero correspondente;
* Não tenham sido convocados anteriormente;
* Possuam a posição necessária.

Quando um jogador é selecionado:

* Seu CPF é associado ao time;
* Seu status passa a indicar a peneira para a qual foi convocado.

---

# Estrutura de Dados

## Jogadores

Os jogadores são armazenados em um dicionário contendo:

```python
{
    "CPF": {
        "nome": "...",
        "genero": "...",
        "senha": "...",
        "posicao": "...",
        "status_da_peneira": ...
    }
}
```

---

## Funcionários

```python
{
    "Claudio": "12345",
    "Ana": "Abacate"
}
```

---

## Peneiras

```python
{
    "peneira 1": {
        "dia da peneira": "...",
        "horario inicio": "...",
        "horario fim": "...",
        "local": "...",
        "times": {...}
    }
}
```

---

# Observação Importante para Testes

O banco de dados inicial do sistema já contém jogadores cadastrados para todas as posições, exceto **Centro Avante**.

Por esse motivo, para que um novo cadastro seja selecionado rapidamente durante a geração dos primeiros times, recomenda-se:

1. Criar uma nova conta de jogador;
2. Fazer login;
3. Escolher a posição **Centro Avante**;
4. Em seguida, acessar uma conta de funcionário e criar uma peneira.

Dessa forma, o jogador recém-cadastrado terá grande chance de ser convocado automaticamente para um dos primeiros times gerados.

---

# Fluxo de Execução

## Menu Principal

```text
1 - Jogador
2 - Funcionário
0 - Sair
```

### Jogador

```text
1 - Login
2 - Criar Conta
0 - Voltar
```

### Menu do Jogador

```text
1 - Escolher posição
2 - Ver status e convite para peneira
0 - Sair
```

### Menu do Funcionário

```text
1 - Agendar peneira
2 - Ver peneiras atuais
0 - Sair
```

---

# Como Executar

1. Instale o Python 3.
2. Salve o código em um arquivo `.py`.
3. Execute no terminal:

```bash
python nome_do_arquivo.py
```

4. Utilize uma das contas de funcionário disponibilizadas neste README para criar peneiras e testar o sistema.

