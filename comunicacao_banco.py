import pymysql

def criar_conexao():
    return pymysql.connect(
    host='yamanote.proxy.rlwy.net',
    user='root',
    password='iqFvNndbKPPSBPtEAKMIkmhrryoqRWTA',
    port=14821,
    database='railway'
)