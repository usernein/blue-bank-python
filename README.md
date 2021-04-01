# blue-bank-python
![bb](https://user-images.githubusercontent.com/29507335/113351651-8c269d00-9311-11eb-9529-073df170a292.jpeg)

Blue Bank é um banco fictício desenvolvidos pelos alunos da Blue EdTech. Este programa é a minha versão da interface do usuário, feita com Python, suor e lágrimas.

## Pontos feitos:
- Pedir usuário e senha
- Iniciar cadastro do novo usuário, pedindo idade, endereço e senha
- Em loop infinito, dar opções de navegação para o usuário, com opção de sair
- Operações de consulta, saque, depósito e transferência para outros usuários existentes (cezar e artur)
- Saldo inicial de 1000
- Só mostra o saldo após na consulta de dados após confirmação do usuário
- Senhas são guardadas em uma dict separada dos dados
- Validações:
  - Não permitir saque e transferência de valores maiores que o saldo do usuário, evitando saldo negativo
  - Não permitir transferência para usuários inexistentes
  - Se nome de usuário não existir, inicia um cadastro
  - Não permite uso de senhas menores que 6 caracteres
  - Não permite registro de usuários menores que 16 anos (e informa quanto tempo o usuário precisa esperar para tentar novamente)
- Não tem burocracia :)

## Como executar?
Clone este repositório com `git clone https://github.com/usernein/blue-bank-python`, entre na pasta e execute: `python3 main.py`.

Este programa requer que a versão do Python seja 3.6 ou superior.