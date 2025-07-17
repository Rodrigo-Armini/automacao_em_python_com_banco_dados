import pymysql

def criar_conexao():
    return pymysql.connect(
    host='shuttle.proxy.rlwy.net',
    user='root',
    password='tkmCmInnSXDKrdoBYSUdRVFDLPFEauUV',
    port=31437,
    database='railway'
)

with criar_conexao() as conn:
    cursor = conn.cursor()
    sql = '''
    CREATE TABLE IF NOT EXISTS cervejas (
        id INT PRIMARY KEY AUTO_INCREMENT,
        descricao VARCHAR(255) NOT NULL,
        estilo VARCHAR(255) NOT NULL,
        codigo VARCHAR(255) NOT NULL,
        valor DECIMAL (10,2) NOT NULL,
        valorCaixa DECIMAL(10,2));
    '''
    cursor.execute(sql)
    conn.commit()
    cursor.close()