# Projeto de Aprendizado Python

Um programa simples em Python com menu interativo para aprendizado da linguagem.

## Funcionalidades

- **Cadastro Simples**: Sistema para adicionar, listar e remover nomes
- **Calculadora de Média**: Calcula a média de notas e informa se o aluno foi aprovado (média >= 7)

## Requisitos

- Python 3.x

## Como Executar

1. Clone ou baixe o repositório
2. Abra o terminal na pasta do projeto
3. Execute o comando:

```bash
python main.py
```

## Navegação

Ao iniciar o programa, você verá um menu com as opções:

| Comando | Ação |
|---------|------|
| 0 | Sair do programa |
| 1 | Cadastro Simples |
| 2 | Calculadora de Média |

### Cadastro Simples
- Adicionar nomes
- Listar todos os nomes cadastrados
- Remover nomes da lista

### Calculadora de Média
- Informe a quantidade de notas
- Digite cada nota (entre 0 e 10)
- O programa calcula a média e informa se foi aprovado ou reprovado

## Estrutura do Projeto

```
├── main.py         # Menu principal
├── cadastro.py     # Módulo de cadastro de nomes
├── calc_media.py   # Módulo de cálculo de média
└── README.MD       # Este arquivo
```
