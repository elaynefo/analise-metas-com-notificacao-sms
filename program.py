import pandas as pd
from twilio.rest import Client

# Include your Account SID from twilio.com/console
account_sid = " "
# Include your Auth Token from twilio.com/console
auth_token  = " "
client = Client(account_sid, auth_token)


lista_meses = ['janeiro', 'fevereiro','março','abril','maio']

for mes in lista_meses:
    tabela_vendas = pd.read_excel(f'{mes}.xlsx')
    if (tabela_vendas['Vendas'] > 55000).any():
        vendedor = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendedor'].values[0]
        vendas =  tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendas'].values[0]
        print(f'No mês de {mes} a meta foi batida! Vendedor: {vendedor} vendeu R$ {vendas: .2f}. Parabens!')
        message = client.messages.create(
            to="+5511000000000",
            from_="+00000000000",
            body=f'No mês de {mes} a meta foi batida! Vendedor: {vendedor} vendeu R$ {vendas: .2f}. Parabens!')
        print(message.sid)