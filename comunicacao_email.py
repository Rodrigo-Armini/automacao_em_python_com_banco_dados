from importlib.resources import contents
from operator import index

import yagmail
from comunicacao_banco import criar_conexao, cursor
import pandas as pd

with criar_conexao() as conn:
    cursor = conn.cursor()
    sql = '''SELECT * FROM cervejas'''
    df = pd.read_sql(sql, conn)

df = df.fillna('')
tabela = df.to_html(index=False, border=False, header=False)
df.to_csv('cervejas.csv')


# tabela = ''
# for produto in produtos:
#     tabela += f'''
#     <tr>
#         <td>{produto[1]}</td>
#         <td>{produto[2]}</td>
#         <td>{produto[3]}</td>
#         <td>{produto[4]}</td>
#         <td>{produto[5] if produto[5] else ""}</td>
#     </tr>
#         '''
# tabela += '</table>'
senha_app = 'qypd lhdx qxeb ydhq'
email = yagmail.SMTP('rodrigoarmini@gmail.com', senha_app)

email.send(
    to='rodrigoarmini@gmail.com',
    subject='Email com Yagmail',
    contents=tabela,
    attachments='cervejas.csv'
)