# Gerenciamento de Clientes Bancários

## Introdução

Com o aumento de clientes, uma instituição bancária percebeu a necessidade de um sistema robusto para gerenciar informações de seus clientes. Dado que o banco atende tanto a indivíduos (pessoas físicas) quanto a empresas (pessoas jurídicas), torna-se essencial ter um sistema eficaz para armazenar e recuperar informações desses dois tipos de clientes.

## Objetivos

1. **Inserir dados dos clientes:** O sistema deve ser capaz de inserir informações tanto de pessoas físicas quanto de pessoas jurídicas no banco de dados.
2. **Listar os clientes inseridos:** Após inserir os clientes, o sistema deve ser capaz de listar todos os clientes armazenados no banco de dados, diferenciando pessoas físicas de pessoas jurídicas.

## Estrutura do Projeto

O projeto consiste em um script Python que utiliza SQLite para gerenciamento do banco de dados. As funcionalidades incluem:

- Criação do banco de dados SQLite e das tabelas `pessoa_fisica` e `pessoa_juridica`.
- Inserção de dados de clientes com validação de CPF e CNPJ para garantir unicidade e integridade dos dados.
- Listagem de todos os clientes inseridos, categorizados como pessoas físicas e jurídicas.

## Pré-requisitos

- Python 3.x
- Biblioteca SQLite3 (inclusa na biblioteca padrão do Python)

