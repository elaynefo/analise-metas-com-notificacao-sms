# Análise de Metas com Notificação por SMS

Script para análise de vendas de mensais, com objetivo de identificar a meta batida e notificar a persona por SMS.

### Ferramentas usadas:
* API do twilio para envio do SMS
* Biblioteca do Pandas para leitura de arquivos de dados em Excel

### Objetivo/Funcionamento:

O script faz a leitura e capta as informações dos arquivos de vendas, inclui em tabelas e compara os valores de acordo com a meta estabelecida dentro da condicional.
Ao identificar um valor maior que a meta, dispara um SMS com o valor total da venda, o mês que a meta foi batida e o nome do vendedor.


Para correto funcionamento, é necessário incluir os dados da conta criada no twilio nos campos de autenticação:

```
account_sid = " " # Include your Account SID from twilio.com/console
auth_token  = " " # Include your Auth Token from twilio.com/console
client = Client(account_sid, auth_token)
```
**Configuração do SMS**
```
message = client.messages.create(
            to="+5511000000000", 
            from_="+00000000000", # Include your FROM_ from twilio.com/console 
            body=f'No mês de {variavel_mes} a meta foi batida! Vendedor: {variavel_vendedor} vendeu R$ {variavel_valor: .2f}. Parabens!')
```
