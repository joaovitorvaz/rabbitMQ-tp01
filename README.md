# rabbitMQ

Repositório para o Trabalho Prático I da disciplina Sistemas Distribuídos. Neste projeto rodamos uma API do Twitter utilizando RabbitMQ sobre 5 nós/máquinas virtuais, sendo estes criados através do Google Kubernetes Engine.

## Configuração
1. Após iniciar o Google Cloud Shell, clonamos este repositório.
2. Utilizando do comando `cd`, vamos para dentro da pasta rabbitMQ.
3. Rodamos o docker com os comandos:
```
docker pull lucifer8591/rabbitmq-server:3.7.17
docker run lucifer8591/rabbitmq-server:3.7.17
docker-compose up -d
```
4. Configuramos o node com `npm install`.

## Utilização
Existem duas possibilidades de uso para a aplicação disponível aqui: uma é utilizando a API do Twitter para enviar um número n de tweets para um canal receptor, e a outra é para enviar uma mensagem qualquer. Destaca-se, porém, que para ambos os casos é necessário utilizar os arquivos na pasta `rotas`.

**1. Twitter**

Neste caso utilizamos o tipo de envio crawler. Para receber, utilizamos o comando `node receiver.js ${porta} ${@conta}`, sendo que:
- ${porta}: refere-se a porta 0 (localhost) ou 5672 (porta padrão do cluster).
- ${@conta}: nome de usuário da conta que se deseja extrair os tweets. Ou seja, é o nome depois do @. É possível inserir mais de uma conta (fila) para ser aceita.

Um exemplo seria `node receiver.js 5672 maisa`, este comando abrindo a porta e aguardando mensagens que venham da conta @maisa. Portanto, caso você envie de uma conta diferente, os tweets não irão ser recebidos.

Já para enviar, utilizamos o comando `node emitter.js crawler ${porta} ${@conta} ${quantidade}`, sendo que:
- ${porta} e ${@conta} são iguais as utilizadas para receber.
- ${quantidade}: número de tweets que se deseja extrair.

Um exemplo deste comando seria `node emitter.js crawler 5672 "maisa" 10`, que iria enviar para a porta 5672 10 tweets da conta @maisa. 

**2. Mensagem**

Neste caso, por outro lado, temos apenas o envio e recebimento de mensagens normais. Assim, utilizamos do tipo de envio normal. Para receber, o comando a ser utilizado é `node receiver.js ${porta} ${fila}`, tendo:
- ${porta}: refere-se a porta 0 (localhost) ou 5672 (porta padrão do cluster).
- ${@fila}: nome das filas que são aceitas pelo recebedor. 

Já para enviar, tem-se o comando `node emitter.js normal ${porta} ${fila} ${mensagem}`, tendo:
- ${porta} e ${fila} são iguais as utilizadas para receber. 
- ${mensagem}: texto da mensagem a ser enviada. 
