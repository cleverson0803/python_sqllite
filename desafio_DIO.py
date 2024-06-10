import sqlite3

# Conectar ao banco de dados (ou criar um novo banco de dados se não existir)
conn = sqlite3.connect('banco.db')
cursor = conn.cursor()

# Criar tabelas
cursor.execute('''
CREATE TABLE IF NOT EXISTS pessoa_fisica (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    cpf TEXT NOT NULL UNIQUE
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS pessoa_juridica (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    cnpj TEXT NOT NULL UNIQUE
)
''')

conn.commit()

# Função para inserir dados de pessoa física
def inserir_pessoa_fisica(nome, cpf):
    try:
        cursor.execute('INSERT INTO pessoa_fisica (nome, cpf) VALUES (?, ?)', (nome, cpf))
        conn.commit()
        print(f'Pessoa Física {nome} inserida com sucesso.')
    except sqlite3.IntegrityError:
        print('Erro: CPF já existe no banco de dados.')

# Função para inserir dados de pessoa jurídica
def inserir_pessoa_juridica(nome, cnpj):
    try:
        cursor.execute('INSERT INTO pessoa_juridica (nome, cnpj) VALUES (?, ?)', (nome, cnpj))
        conn.commit()
        print(f'Pessoa Jurídica {nome} inserida com sucesso.')
    except sqlite3.IntegrityError:
        print('Erro: CNPJ já existe no banco de dados.')

# Função para listar todos os clientes
def listar_clientes():
    print('Pessoas Físicas:')
    cursor.execute('SELECT * FROM pessoa_fisica')
    for row in cursor.fetchall():
        print(row)
    
    print('\nPessoas Jurídicas:')
    cursor.execute('SELECT * FROM pessoa_juridica')
    for row in cursor.fetchall():
        print(row)

# Exemplo de uso
inserir_pessoa_fisica('João Silva', '12345678900')
inserir_pessoa_juridica('Empresa XYZ', '9876543210001')
listar_clientes()

# Fechar a conexão
conn.close()
