
# App Converter — Redes de Computadores I

Aplicação web desenvolvida em Python e Flask para converter
números entre os sistemas decimal, binário, hexadecimal e octal.

## Funcionalidades

- Decimal para binário, hexadecimal e octal.
- Binário para decimal, hexadecimal e octal.
- Hexadecimal para binário, decimal e octal.
- Octal para binário, decimal e hexadecimal.
- Validação de algarismos conforme a base escolhida.
- Exibição do resultado em uma janela modal.

## Tecnologias

- Python 3
- Flask
- HTML5
- CSS3
- JavaScript

## Requisitos

- Python 3 instalado.
- pip.
- Navegador web.
- Git, para clonar e versionar o projeto.

## Como executar

1. Clone o repositório.
2. Entre na pasta do projeto.
3. Crie um ambiente virtual:

   Windows:

   ```powershell
   py -m venv .venv
   ```

4. Ative o ambiente virtual:

   ```powershell
   .\.venv\Scripts\Activate.ps1
   ```

5. Instale as dependências:

   ```powershell
   python -m pip install -r requirements.txt
   ```

6. Execute a aplicação:

   ```powershell
   python app.py
   ```

7. Acesse http://127.0.0.1:5000 no navegador.

## Implementação

Os métodos de conversão são implementados no arquivo
`conversoes.py`, sem utilizar as funções prontas `bin()`,
`hex()` e `oct()`.

## Integrantes

Preencha esta seção com os nomes reais dos integrantes
e as respectivas contribuições.
