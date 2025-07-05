# Sistema de Gerenciamento de Eventos

Este projeto é um sistema simples para cadastro, gerenciamento e consulta de eventos e participantes, feito em Python puro para terminal.

## Funcionalidades
- Cadastro, listagem, edição e remoção de eventos
- Cadastro, busca, edição e remoção de participantes
- Inscrição de participantes em eventos
- Estatísticas de temas e participantes mais ativos
- Interface de menu interativo no terminal

## Estrutura dos Arquivos
- `main.py`: Ponto de entrada do sistema
- `menu.py`: Menu principal e navegação
- `func_evento.py`: Funções para manipulação de eventos
- `func_user.py`: Funções para manipulação de participantes
- `menu_evento.py`: Menu de opções para um evento específico
- `estatisticas.py`: Geração de estatísticas no terminal
- `data.py`: Exemplo de dados de eventos e participantes

## Como usar
1. Execute o arquivo `main.py`:
   ```
   python main.py
   ```
2. Siga as instruções do menu para cadastrar eventos, participantes, consultar informações e visualizar estatísticas.

## Exemplo de dados
O arquivo `data.py` contém exemplos de eventos e participantes para facilitar testes e demonstrações. Para usar esses dados no sistema, importe-os nos arquivos `func_evento.py` e `func_user.py` conforme necessário.

## Requisitos
- Python 3.10 ou superior (para suporte ao `match-case`)

## Observações
- Todos os dados são mantidos em memória enquanto o programa está em execução.
- Não há persistência automática dos dados ao fechar o programa.
