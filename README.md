# Discord Log Collector

Este é um simples script de bot para Discord escrito em Python que monitora um arquivo de log e envia as novas entradas de log para um canal especificado em um servidor do Discord.

## Pré-requisitos

Antes de executar o script, certifique-se de ter o seguinte instalado:

- Python 3.x
- Biblioteca [discord.py](https://discordpy.readthedocs.io/)
- Biblioteca [python-dotenv](https://pypi.org/project/python-dotenv/)

## Configuração

1. Clone o repositório ou faça o download do script para sua máquina local.
2. Instale as dependências necessárias executando o seguinte comando:
`pip install discord dotenv`

3. Crie um novo bot do Discord e obtenha seu token. Você pode seguir a documentação oficial do Discord sobre como criar um bot e obter seu token.
4. Crie um arquivo `.env` no mesmo diretório do script e adicione a seguinte linha, substituindo `SEU_TOKEN_AQUI` pelo token do bot obtido no passo anterior:
`TOKEN2=SEU_TOKEN_AQUI`

5. Defina a variável `log_file_path` para o caminho absoluto do arquivo de log que você deseja monitorar. Por exemplo:
`log_file_path = r"/caminho/para/seu/arquivo.log"`

6. Defina a variável `channel_id` para o ID do canal do Discord onde você deseja que as entradas de log sejam enviadas. Você pode ativar o Modo de Desenvolvedor no Discord e clicar com o botão direito do mouse no canal para copiar seu ID.

## Uso

Para iniciar o bot, execute o seguinte comando:
`python bot.py`
