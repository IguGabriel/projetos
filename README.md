"Guia do Programa de Avaliação de Empresas

Obs:
--Tudo entre * não é obrigatório para o funcionamento do programa--

Introdução
Este programa foi desenvolvido para permitir que os usuários avaliem empresas e compartilhem suas opiniões com a comunidade. Com uma interface simples e intuitiva, você pode facilmente avaliar empresas, comentar sobre elas e ler avaliações de outros usuários.

Instalação

Para instalar o programa, siga estas etapas:

- Certifique-se de ter o Django instalado no seu ambiente Python.
- Clone o repositório do programa para o seu diretório de trabalho.
- Execute python manage.py migrate para criar as tabelas do banco de dados.
- Inicie o servidor com python manage.py runserver.

Tela Inicial

*Por favor, tente avaliar sem estar logado para testar o redirecionamento.*

Você já vai se deparar com as empresas e suas descrições:

Se não tiver uma conta, fique à vontade para clicar em cadastrar. Caso contrário, acesse a página de login no navegador. Insira seu nome de usuário e senha. Clique em “Entrar” para acessar sua conta.

*Por favor, coloque o nome ou a senha errados propositalmente para ver todas funcionalidades.*

Avaliando Empresas

Para avaliar as empresas, você tem a opção de apenas ler a descrição e já avaliar na página principal ou selecionar a empresa que queira votar, e fique à vontade para ler os comentários (só não deixe que influencie sua decisão). Na página da empresa ou na Tela inicial, escolha uma nota entre 1 (ruim) e 5 (ótimo), escreva um comentário sobre sua experiência e clique no botão “Avaliar” para publicar sua avaliação.

Logout

Para efetuar o logout, volte para a página principal e simplesmente clique em logout.

(Infelizmente, não ficou 100% do jeito que eu queria, mas posso dizer que é o máximo que consigo fazer nesse espaço de tempo.)

Aqui vão alguns exemplos de ideias que eu tinha, mas não foram implementadas por causa da minha incapacidade/tempo:

Estilização

Além das cores, eu queria trabalhar com imagens/logo de cada marca. Gostaria de que a forma de avaliação fosse mais estilizada em formas de estrelas e com o uso do JavaScript.

Funcionalidades


Minha vontade era colocar uma personalização para cada login. O usuário teria sua foto de perfil e mudaria de acordo com seu gosto. Queria ter adicionado uma opção de resposta de comentários, assim tendo uma interação entre os usuários.
